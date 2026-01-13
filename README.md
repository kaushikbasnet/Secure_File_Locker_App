#  Secure File Locker Application

The **Secure File Locker Application** is a Python-based security tool designed to protect sensitive files using **AES-256-GCM authenticated encryption**. It provides a user-friendly graphical interface for encrypting and decrypting files securely with strong password-based protection, ensuring confidentiality, integrity, and authenticity of stored data. The application follows secure cryptographic practices and is suitable for academic, personal, and lightweight professional use.

---

##  Features

* AES-256-GCM authenticated encryption
* Secure password-based file protection
* Automatic IV and authentication tag handling
* Password strength validation
* User-friendly GUI
* Cross-platform Python support
* Optional standalone executable build

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
│   └── secure_file_locker/           # PyInstaller build artifacts
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

---

##  Getting Started Locally

### 1️. Clone the Repository

```bash
git clone https://github.com/kaushikbasnet/Secure_File_Locker_App.git
cd Secure_File_Locker_App
```

---

### 2️. Create and Activate Virtual Environment (Recommended)

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

### 3️. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️. Run the Application

```bash
python -m secure_file_locker.gui
```

---

##  Install from PyPI

This project is published on **PyPI**.

🔗 [https://pypi.org/project/secure-file-locker/](https://pypi.org/project/secure-file-locker/)

```bash
pip install secure-file-locker
```

Run after installation:

```bash
secure-file-locker
```

---

##  Run Using Docker (GHCR + Docker Desktop)

The application can also be run using Docker via **GitHub Container Registry (GHCR)**.

### Prerequisites

* Docker Desktop installed and running
* Docker CLI access

---

### 1️. Pull the Image from GHCR

```bash
docker pull ghcr.io/kaushikbasnet/secure-file-locker:latest
```

---

### 2️. Run the Container

```bash
docker run -it --rm ghcr.io/kaushikbasnet/secure-file-locker:latest
```

>  For GUI-based containers, ensure your OS supports GUI forwarding or use the local/PyPI version.

---

##  CI/CD & Quality Assurance

The project uses **GitHub Actions** for continuous integration and deployment, automatically running tests, validating cryptographic correctness, enforcing pull request reviews, and generating release artifacts. All builds and releases are traceable and reproducible.

---

##  Testing

Run tests locally using:

```bash
pytest
```


##  Badges

[![PyPI](https://img.shields.io/pypi/v/secure-file-locker.svg)](https://pypi.org/project/secure-file-locker/)




