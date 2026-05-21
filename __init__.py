# gatoDone.py
import playsound
from pathlib import Path
import atexit

SOUND_FILE = Path(__file__).with_name("copyright-free-sound-effect-cat-scream.mp3")

def gatoDone():
    playsound.playsound(str(SOUND_FILE))

def gatoLoop(x):
    for _ in range(x):
        gatoDone()

def play_when_done():
    atexit.register(gatoDone)
