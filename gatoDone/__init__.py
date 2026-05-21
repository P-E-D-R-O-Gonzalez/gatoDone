# gatoDone.py
import playsound
from pathlib import Path
import atexit

SOUND_FILE = Path(__file__).with_name("copyright-free-sound-effect-cat-scream.mp3")

def play():
    playsound.playsound(str(SOUND_FILE))
    
def gatoDone():
    atexit.register(play)

def gatoLoop(x):
    for _ in range(x):
        play()

