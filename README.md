# 🔐 Secure File Sharing System

A web-based application for file encryption and decryption, designed with simplicity, transparency, and trust at its core. Built using **Flask** and **Fernet symmetric cryptography**, this tool helps users take control of their file security through an intuitive and ethically guided experience.

## 💡 Purpose
To create an accessible interface for secure file sharing that prioritizes:
- User autonomy and control
- Cryptographic clarity
- Ethical simplicity in design

## ⚙️ Technologies Used
- **Framework:** Flask (Python)
- **Encryption:** `cryptography.fernet` (AES-CBC + HMAC)
- **Frontend:** HTML & CSS (inline styles)
- **Storage:** Local file system (`uploads/`)
- **Key Management:** Persistent key saved in `secret.key`

## 🧩 Core Features
- Upload files to encrypt or decrypt with one click
- Persistent encryption key for repeatable decryption
- Minimalist UI: calm visuals, clear flow, no hidden logic
- Direct download after encryption/decryption

## 🗂 File Structure
secure-file-sharing/ ├── main.py                # Core Flask logic and Fernet integration ├── secret.key             # Persistent encryption key ├── uploads/               # Stores processed files └── templates/             # HTML layout files ├── index.html         # Home page with action buttons ├── preview.html       # Upload form for encrypt/decrypt └── success.htm

## 🔐 Encryption Flow
- One-time key generation using Fernet
- AES encryption with CBC mode, integrity via HMAC
- Key is stored in `secret.key` and reused for consistent results

## 🎨 Design Philosophy
- **Transparency:** No hidden data flows or complex logic
- **Empowerment:** Users decide what happens to their files
- **Simplicity:** Calm colors, intuitive paths, minimal clutter
## 👤 Author
Vaibhav Gulati

-Builder of tools where security meets empathy. Focused on ethical tech, user trust, and clear design.

## 🌱 Secure by design. Empowering by intent.

