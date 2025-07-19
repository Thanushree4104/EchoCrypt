import socket
import datetime
from encryption import decrypt_message
from audio_codec import wav_to_audio_bytes, decode_bitstream

filename = input("Enter path to encrypted WAV file: ")
password = input("Enter password to decrypt: ")

print("[*] Decoding audio to bitstream...")

try:
    audio_data = wav_to_audio_bytes(filename)
    encrypted_text = decode_bitstream(audio_data)
    decrypted = decrypt_message(encrypted_text, password)
    print("[+] Decrypted message:", decrypted)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    receiver_ip = socket.gethostbyname(socket.gethostname())
    with open("transmission_log.txt", "a", encoding='utf-8') as log:
        log.write(f"[{timestamp}] Receiver IP: {receiver_ip} <-- Decrypted from: {filename}\n")

except Exception as e:
    print("[!] Decryption failed:", e)
