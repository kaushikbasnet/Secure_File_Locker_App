import os
from pathlib import Path
import customtkinter as ctk
from tkinter import filedialog, messagebox
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.backends import default_backend

MAGIC = b"SFLK"
VERSION = b"\x01"
SALT_SIZE = 16
NONCE_SIZE = 12
KDF_ITERS = 200_000


# KEY DERIVATION + CRYPTO FUNCTIONS

def derive_key(password: bytes, salt: bytes, length: int = 32) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=length,
        salt=salt,
        iterations=KDF_ITERS,
        backend=default_backend()
    )
    return kdf.derive(password)


def encrypt_file(path: Path, password: bytes) -> Path:
    salt = os.urandom(SALT_SIZE)
    key = derive_key(password, salt)
    aesgcm = AESGCM(key)
    nonce = os.urandom(NONCE_SIZE)

    data = path.read_bytes()
    ciphertext = aesgcm.encrypt(nonce, data, None)

    out_path = path.with_suffix(path.suffix + ".sflk")

    with out_path.open("wb") as f:
        f.write(MAGIC)
        f.write(VERSION)
        f.write(salt)
        f.write(nonce)
        f.write(ciphertext)

    return out_path


def decrypt_file(path: Path, password: bytes) -> Path:
    with path.open("rb") as f:
        header = f.read(4)
        if header != MAGIC:
            raise ValueError("Invalid file format.")

        version = f.read(1)
        salt = f.read(SALT_SIZE)
        nonce = f.read(NONCE_SIZE)
        ciphertext = f.read()

    key = derive_key(password, salt)
    aesgcm = AESGCM(key)

    try:
        plaintext = aesgcm.decrypt(nonce, ciphertext, None)
    except Exception:
        raise ValueError("Wrong password or file tampered.")

    out_path = path.with_suffix("")
    out_path.write_bytes(plaintext)

    return out_path


# PASSWORD STRENGTH CHECKER

def password_strength(pw: str):
    score = 0

    if len(pw) >= 8:
        score += 1
    if any(c.islower() for c in pw):
        score += 1
    if any(c.isupper() for c in pw):
        score += 1
    if any(c.isdigit() for c in pw):
        score += 1
    if any(c in "!@#$%^&*()-_=+[]{};:,.<>?/|\\`~" for c in pw):
        score += 1

    return score


# MODERN UI APPLICATION

class SecureFileLockerUI(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Secure File Locker – Modern UI")
        self.geometry("550x480")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.selected_file = None

        # Title
        title = ctk.CTkLabel(self, text="Secure File Locker",
                             font=("Arial", 26, "bold"))
        title.pack(pady=15)

        # File selector
        self.file_label = ctk.CTkLabel(self, text="No file selected", text_color="gray")
        self.file_label.pack()

        choose_btn = ctk.CTkButton(self, text="Choose File", command=self.choose_file)
        choose_btn.pack(pady=10)

        # Password
        self.pw_entry = ctk.CTkEntry(self, placeholder_text="Enter Password", show="*",
                                     width=300)
        self.pw_entry.pack(pady=5)
        self.pw_entry.bind("<KeyRelease>", self.update_strength_meter)

        self.strength_bar = ctk.CTkProgressBar(self, width=300)
        self.strength_bar.set(0)
        self.strength_bar.pack(pady=5)

        self.strength_label = ctk.CTkLabel(self, text="Password Strength: ")
        self.strength_label.pack()

        # Confirm password (only used for encryption)
        self.confirm_entry = ctk.CTkEntry(self, placeholder_text="Confirm Password",
                                          show="*", width=300)
        self.confirm_entry.pack(pady=5)

        # Buttons
        enc_btn = ctk.CTkButton(self, text="Encrypt File", command=self.encrypt_gui)
        enc_btn.pack(pady=10)

        dec_btn = ctk.CTkButton(self, text="Decrypt File", fg_color="green",
                                command=self.decrypt_gui)
        dec_btn.pack()

        # Status
        self.status = ctk.CTkLabel(self, text="", text_color="#00bfff")
        self.status.pack(pady=10)

    # GUI Helpers

    def choose_file(self):
        file = filedialog.askopenfilename()
        if file:
            self.selected_file = Path(file)
            self.file_label.configure(text=f"Selected: {self.selected_file.name}",
                                      text_color="white")


    # ---------------- PASSWORD STRENGTH METER ----------------

    def update_strength_meter(self, event=None):
        pw = self.pw_entry.get()
        score = password_strength(pw)

        self.strength_bar.set(score / 5)

        if score <= 1:
            self.strength_label.configure(text="Password Strength: Weak", text_color="red")
        elif score == 2:
            self.strength_label.configure(text="Password Strength: Medium", text_color="orange")
        elif score == 3:
            self.strength_label.configure(text="Password Strength: Strong", text_color="yellow")
        elif score >= 4:
            self.strength_label.configure(text="Password Strength: Very Strong",
                                          text_color="lightgreen")

    # ---------------- Encryption / Decryption -----------------

    def encrypt_gui(self):
        if not self.selected_file:
            messagebox.showerror("Error", "Please select a file.")
            return

        pw = self.pw_entry.get()
        conf = self.confirm_entry.get()

        if pw != conf:
            messagebox.showerror("Error", "Passwords do not match.")
            return

        if len(pw) == 0:
            messagebox.showerror("Error", "Password cannot be empty.")
            return

        try:
            out = encrypt_file(self.selected_file, pw.encode())
            self.status.configure(text=f"Encrypted → {out.name}")
            messagebox.showinfo("Success", f"Encrypted file: {out}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def decrypt_gui(self):
        if not self.selected_file:
            messagebox.showerror("Error", "Please select a file.")
            return

        pw = self.pw_entry.get()

        if len(pw) == 0:
            messagebox.showerror("Error", "Password cannot be empty.")
            return

        try:
            out = decrypt_file(self.selected_file, pw.encode())
            self.status.configure(text=f"Decrypted → {out.name}")
            messagebox.showinfo("Success", f"Decrypted file: {out}")
        except Exception as e:
            messagebox.showerror("Error", str(e))


# ----------------------------------------------------------

def main():
    app = SecureFileLockerUI()
    app.mainloop()


if __name__ == "__main__":
    main()

