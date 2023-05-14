#Generatore di Seed e Chiave Privata Bitcoin

Questo modulo Python genera un seed mnemonico BIP39 e una chiave privata per un portafoglio Bitcoin utilizzando l'input audio da un microfono.

#Installazione

Prima di utilizzare questo modulo, dovrai installare alcune librerie Python. Puoi farlo utilizzando pip, il gestore dei pacchetti di Python. Apri un terminale e inserisci i seguenti comandi:

pip3 install sounddevice
pip3 install numpy
pip3 install mnemonic
pip3 install pbkdf2
pip3 install colorama

#Utilizzo

Per utilizzare questo modulo, devi eseguire il file genera_seed_24_parole_da_voce.py utilizzando Python 3. Puoi farlo con il seguente comando:

python3 genera_seed_24_parole_da_voce.py

Dopo aver eseguito il comando, dovrai parlare nel tuo microfono per 10 secondi. Il modulo genererà poi un seed mnemonico e una chiave privata basati sull'input audio.

#Nota di sicurezza

Ricorda che la generazione di chiavi private basata su input audio potrebbe non essere sufficientemente sicura per un ambiente di produzione. Utilizza questo modulo a tuo rischio e pericolo.
