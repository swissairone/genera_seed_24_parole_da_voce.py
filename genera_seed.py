import sounddevice as sd
import numpy as np
from hashlib import sha256
from mnemonic import Mnemonic
from binascii import hexlify
from pbkdf2 import PBKDF2
import hmac
import hashlib
from colorama import Fore, Style

def generate_wallet():
    print(Fore.CYAN + "Inizia a parlare per generare il tuo seed..." + Style.RESET_ALL)

    # Registra l'audio per 10 secondi
    recording = sd.rec(int(10 * 44100), samplerate=44100, channels=1)
    sd.wait()

    # Converte l'audio in dati binari
    audio_data = recording.flatten().tobytes()

    # Usa SHA-256 per ottenere un hash dell'audio
    audio_hash = sha256(audio_data).digest()

    # Genera un seed mnemonico in italiano utilizzando l'hash dell'audio
    mnemonic = Mnemonic("italian")
    words = mnemonic.to_mnemonic(audio_hash)

    print(Fore.GREEN + "\nIl tuo seed mnemonico è: " + words + Style.RESET_ALL)

    # Converte il seed mnemonico in un seed binario
    seed = mnemonic.to_seed(words)

    # Genera la chiave privata
    private_key = hexlify(PBKDF2(words, seed, iterations=2048, macmodule=hmac, digestmodule=hashlib.sha512).read(64)).decode()

    print(Fore.GREEN + "\nLa tua chiave privata è: " + private_key + Style.RESET_ALL)

# Genera un nuovo wallet
generate_wallet()
