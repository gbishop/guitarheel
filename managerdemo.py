import pygame
from datautilities.DataConstants import Constants
from datautilities.DataProcessors import NoteDataReader
from sounds.ChannelManager import ChannelManager
from sounds.SoundBoxes import AdvGuitarSoundBox
from sounds.SoundBoxes import InstrumentNameSoundBox
from instruments.Guitar import Guitar
import time

pygame.mixer.init(44100, -16, 8, 512)
pygame.init()

class Game(object):
    def __init__(self, width = 500, height = 500):
        self.size = (width, height)
        display = pygame.display.set_mode(self.size)
        
    def play(self):
        cm = ChannelManager(7)
        a = ' '
        c = cm.reserveChannel(a)
        cm.printinfo()

g = Game()
g.play()
