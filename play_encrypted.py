import socket
import datetime
from encryption import encrypt_message
from audio_codec import text_to_bitstream, bitstream_to_wav

message = input("Enter message to send: ")
password = input("Enter password: ")

encrypted_text = encrypt_message(message, password)
bitstream = text_to_bitstream(encrypted_text)

timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"encrypted_{timestamp}.wav"

bitstream_to_wav(bitstream, filename)

sender_ip = socket.gethostbyname(socket.gethostname())
with open("transmission_log.txt", "a", encoding='utf-8') as log:
    log.write(f"[{timestamp}] Sender IP: {sender_ip} --> Generated file: {filename}\n")

print(f"[+] Message encrypted and saved to {filename}")
