# gatoDone.py
import playsound

def gatoDone():
    soundEffectPath = "copyright-free-sound-effect-cat-scream.mp3"
    playsound.playsound(soundEffectPath)

def gatoLoop(x):
    for i in range(x):
        gatoDone()