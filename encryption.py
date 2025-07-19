from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.Padding import pad, unpad
import base64

def compute_checksum(text):
    return sum(ord(c) for c in text) % 256

def encrypt_message(message, password):
    key = SHA256.new(password.encode()).digest()
    iv = key[:16]
    checksum = compute_checksum(message)
    message_with_checksum = f"{message}|{checksum}"
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded = pad(message_with_checksum.encode(), AES.block_size)
    encrypted = cipher.encrypt(padded)
    return base64.b64encode(encrypted).decode()

def decrypt_message(encrypted_b64, password):
    try:
        key = SHA256.new(password.encode()).digest()
        iv = key[:16]
        encrypted = base64.b64decode(encrypted_b64)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted = unpad(cipher.decrypt(encrypted), AES.block_size).decode()
        message, checksum = decrypted.rsplit('|', 1)
        if compute_checksum(message) != int(checksum):
            raise ValueError("Checksum mismatch. Message corrupted.")
        return message
    except Exception as e:
        raise ValueError(f"Decryption failed: {e}")
