#  Secure File Locker Application

The **Secure File Locker Application** is a Python-based security tool designed to protect sensitive files using **AES-256-GCM authenticated encryption**. It provides a user-friendly graphical interface for securely encrypting and decrypting files with strong password-based protection, ensuring **confidentiality, integrity, and authenticity** of stored data. The application follows modern cryptographic best practices and is suitable for academic use, personal data protection, and lightweight professional scenarios.

---

##  Features

* AES-256-GCM authenticated encryption
* Secure password-based file protection
* Automatic initialization vector (IV) and authentication tag handling
* Password strength validation and error handling
* User-friendly graphical interface
* Cross-platform Python support
* Optional standalone executable via PyInstaller

---

##  Project Structure

```text
Secure_File_Locker_App/
├── .github/
│   └── workflows/
│       ├── python-ci.yml            # Continuous Integration workflow
│       └── security_scan.yml        # Automated security analysis
│
├── build/
│   └── secure_file_locker/          # PyInstaller build artifacts
│       ├── Analysis-00.toc
│       ├── EXE-00.toc
│       ├── PKG-00.toc
│       ├── PYZ-00.pyz
│       ├── PYZ-00.toc
│       ├── base_library.zip
│       ├── secure_file_locker.pkg
│       ├── warn-secure_file_locker.txt
│       └── xref-secure_file_locker.html
│
├── dist/
│   ├── secure_file_locker-1.0.0-py3-none-any.whl   # Built wheel package
│   └── secure_file_locker-1.0.0.tar.gz             # Source distribution
│
├── secure_file_locker.egg-info/    # Package metadata
│   ├── PKG-INFO
│   ├── SOURCES.txt
│   ├── dependency_links.txt
│   ├── entry_points.txt
│   ├── requires.txt
│   └── top_level.txt
│
├── secure_file_locker/
│   ├── __init__.py
│   ├── main.py                     # Application entry point
│   └── README.md                   # Module-level documentation
│
├── requirements.txt                # Project dependencies
├── setup.py                        # Package configuration
├── secure_file_locker.spec         # PyInstaller configuration
└── README.md                       # Project documentation
```

---

##  Getting Started Locally

### 1. Clone the Repository

```bash
git clone https://github.com/kaushikbasnet/Secure_File_Locker_App.git
cd Secure_File_Locker_App
```

---

### 2. Create and Activate a Virtual Environment (Recommended)

```bash
python -m venv venv
```

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run the Application

```bash
python -m secure_file_locker.main
```

---

##  Install from PyPI

The application is published on **PyPI** and can be installed directly using pip.

🔗 [https://pypi.org/project/secure-file-locker/](https://pypi.org/project/secure-file-locker/)

```bash
pip install secure-file-locker
```

Run the application after installation:

```bash
secure-file-locker
```

---

##  Run Using Docker (GHCR + Docker Desktop)

The application can also be executed using Docker images hosted on **GitHub Container Registry (GHCR)**.

### Prerequisites

* Docker Desktop installed and running
* Docker CLI access

---

### 1. Pull the Image from GHCR

```bash
docker pull ghcr.io/kaushikbasnet/secure-file-locker:latest
```

---

### 2. Run the Container

```bash
docker run -it --rm ghcr.io/kaushikbasnet/secure-file-locker:latest
```

>  For GUI-based execution, ensure your operating system supports GUI forwarding. Otherwise, use the local or PyPI installation.

---

##  CI/CD & Quality Assurance

This project uses **GitHub Actions** to implement continuous integration and deployment. Automated workflows perform dependency installation, testing, cryptographic validation, and security scanning on every push and pull request. Release workflows package verified builds and generate reproducible artifacts, ensuring consistent and secure distributions.

---

##  Testing

Run automated tests locally using:

```bash
pytest
```

---

## Badge

[![PyPI](https://img.shields.io/pypi/v/secure-file-locker.svg)](https://pypi.org/project/secure-file-locker/)
