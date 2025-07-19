import wave
import struct
import numpy as np

def text_to_bitstream(text):
    return ''.join(format(ord(c), '08b') for c in text)

def bitstream_to_text(bitstream):
    chars = [bitstream[i:i+8] for i in range(0, len(bitstream), 8)]
    try:
        return ''.join(chr(int(b, 2)) for b in chars)
    except ValueError:
        raise ValueError("Failed to decode bitstream: Non-binary character detected.")

def encode_bitstream(bitstream, sample_rate=44100, freq0=1000, freq1=2000, duration=0.05):
    samples = []
    for bit in bitstream:
        freq = freq1 if bit == '1' else freq0
        t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
        waveform = 0.5 * np.sin(2 * np.pi * freq * t)
        samples.extend(waveform)
    return np.array(samples, dtype=np.float32)

def bitstream_to_wav(bitstream, filename, sample_rate=44100):
    audio = encode_bitstream(bitstream, sample_rate)
    scaled = np.int16(audio * 32767)

    with wave.open(filename, 'w') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(scaled.tobytes())

def wav_to_audio_bytes(filename):
    with wave.open(filename, 'rb') as wf:
        frames = wf.readframes(wf.getnframes())
        audio = np.frombuffer(frames, dtype=np.int16)
        return audio.astype(np.float32) / 32767.0

def decode_bitstream(audio, sample_rate=44100, freq0=1000, freq1=2000, duration=0.05):
    samples_per_bit = int(sample_rate * duration)
    bits = ''
    for i in range(0, len(audio), samples_per_bit):
        chunk = audio[i:i+samples_per_bit]
        if len(chunk) < samples_per_bit:
            continue
        fft = np.fft.fft(chunk)
        freqs = np.fft.fftfreq(len(chunk), d=1/sample_rate)
        peak_freq = abs(freqs[np.argmax(np.abs(fft))])
        bits += '1' if abs(peak_freq - freq1) < abs(peak_freq - freq0) else '0'

    try:
        return bitstream_to_text(bits)
    except Exception as e:
        raise ValueError("Failed to decode bitstream: " + str(e))
