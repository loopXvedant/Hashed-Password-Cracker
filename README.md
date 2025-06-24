# 🔓 Hashed Password Cracker

A simple Python script to crack hashed passwords using a dictionary attack.

---

## ⚙️ Features

- 🔑 Supports SHA-256, SHA-1, MD5
- 📂 Accepts any custom wordlist
- ⚙️ Command-line interface for flexible usage
- 🧪 Sample wordlist included
- 🔒 Ethical use only — intended for CTFs, labs, and educational environments

---

## 🧠 How It Works

The script compares the target hash with the hashes of every word in a dictionary file. If a match is found — the original password is revealed.

### 📦 Installation

```bash
git clone https://github.com/loopXvedant/Hashed-Password-Cracker.git
cd Hashed-Password-Cracker

### 🔧 Run the script:

```bash
python3 cracker.py -H <hashed_password> -w wordlists/sample.txt -a sha256
