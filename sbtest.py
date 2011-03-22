from sounds.SoundBoxes import InstrumentNameSoundBox
import pygame
from sounds.SoundBoxes import GuitarSoundBox
pygame.mixer.init(44100, -16, 2, 512)
pygame.init()

a = {}
insb = InstrumentNameSoundBox(a)
	
