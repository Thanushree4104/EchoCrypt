EchoCrypt 🔐🔊
# 🔐 EchoCrypt – Encrypted Chat Over Sound

Securely send encrypted messages via sound (`.wav` files).  
Uses AES encryption and converts messages to audible waveforms.

---

## 🚀 Features
- AES-256 encryption with password
- Converts encrypted message into a `.wav` sound file
- Receiver decodes & decrypts the message using the same password
- Integrity check with checksum
- Logs sender and receiver IP + timestamp

---

## 🧰 Requirements

- Python 3.7+
- Dependencies:
  ```bash
  pip install -r requirements.txt

## 📦 Project Structure
audio_codec.py        # Audio encoding/decoding logic
encryption.py         # AES encryption/decryption logic
play_encrypted.py     # Turn message into encrypted .wav
decrypt_from_wav.py   # Decode and decrypt message from .wav
requirements.txt      # Dependencies list
transmission_log.txt  # Logs of transmissions
encrypted_*.wav       # Example audio files
README.md             # This guide


## 🛡️ Notes
Offers best-effort privacy via AES and checksum; not for military-grade security.

Uses human-audible frequencies for simplicity and reliability.
