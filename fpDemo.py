import pygame
import sys
from datautilities.DataConstants import Constants
from datautilities.DataProcessors import NoteDataReader
from sounds.ChannelManager import ChannelManager
from sounds.SoundBoxes import AdvGuitarSoundBox
from sounds.SoundBoxes import InstrumentNameSoundBox
from instruments.Guitar import Guitar
from games.Games import TwoPlayerFreePlay, Horse, SimonSays
import time
pygame.mixer.init(44100, -16, 8, 128)
pygame.init()

class MainGame(object):
    def __init__(self, width = 640, height = 480):
        self.size = (width, height)
        self.display = pygame.display.set_mode(self.size)
        
    def play(self):
        data = NoteDataReader.getData()
        channel_manager = ChannelManager(6)
        
        GSB_one = AdvGuitarSoundBox(
                    'electricguitar',
                    data['electricguitar'],
                    channel_manager
                    )
        GSB_two = AdvGuitarSoundBox(
                    'electricguitar',
                    data['electricguitar'],
                    channel_manager
                    )
                    
        joy = pygame.joystick.Joystick(0)
        joy.init()
        joy2 = pygame.joystick.Joystick(2)
        joy2.init()
        #guitar_one = Guitar(GSB_one, Constants.KEYBOARD_GUITAR_MAP)
        guitar_two = Guitar(GSB_two, Constants.TEST_GUITAR_MAP, joy.get_name(), 0)
        guitar_one = Guitar(GSB_one, Constants.TEST_GUITAR_MAP, joy.get_name(), 2)
        
        while True:
            running = True
            game = TwoPlayerFreePlay(channel_manager, guitar_one, guitar_two)
            #game = Horse(channel_manager, guitar_one, guitar_two, 1, self.display)
            #game = SimonSays(channel_manager, guitar_two, 1, self.display)
            while running:
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.QUIT:
                        sys.exit()
                    vals = game.update(event)
                    if vals[0] is game.end_status:
                        running = False
                        continue
                vals = game.update()
                if vals[0] is game.end_status:
                    running = False
                    continue        
                       
        
        
g = MainGame()
g.play()

