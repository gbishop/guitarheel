import pygame
from datautilities.DataConstants import Constants
from datautilities.DataProcessors import NoteDataReader
from sounds.SoundBoxes import AdvGuitarSoundBox
from sounds.SoundBoxes import InstrumentNameSoundBox
from instruments.Guitar import Guitar
import time

pygame.mixer.init(44100, -16, 4, 512)
pygame.init()

class Game(object):
    
    def __init__(self, width = 500, height=500):
        self.size = (width, height)
        display = pygame.display.set_mode(self.size)

    def play(self):
        data = NoteDataReader.getData()

        channel_count = 1
        insb = InstrumentNameSoundBox(data)

        picked_instrument = False 
        evt = pygame.event.Event(0)
        cur_instrument = 0
        instruments = data.keys()

        sound = pygame.mixer.Sound('notes/acoustic/acoustic1.ogg')
        channel = pygame.mixer.Channel(2)
        channel.play(sound)
        while not evt.type == pygame.QUIT and not picked_instrument:
            evt = pygame.event.wait()
            if evt.type == pygame.KEYDOWN:
                if evt.key == pygame.K_RETURN:
                    picked_instrument = True
                if evt.key == pygame.K_RIGHT:  
                    cur_instrument += 1
                    if len(instruments) == cur_instrument:
                        cur_instrument = 0
                    insb.say_name(instruments[cur_instrument])
                    
        insb.fadeout(1000)
                    
        if cur_instrument == -1:
            cur_instrument = 0
        instrument = instruments[cur_instrument]
        GSB = AdvGuitarSoundBox(instrument, data[instrument])
        GSB2 = AdvGuitarSoundBox(instrument, data[instrument])
        
        joy = pygame.joystick.Joystick(0)
        joy.init()
        guitars = {}
        guitars[joy.get_id()]= Guitar(GSB, Constants.TEST_GUITAR_MAP, joy.get_name())
        guitars['K'] = Guitar(GSB2, Constants.KEYBOARD_GUITAR_MAP)
        
        while not evt.type == pygame.QUIT:
            evt = pygame.event.wait()
            if evt.type == pygame.JOYBUTTONDOWN or evt.type == pygame.JOYBUTTONUP:
               guitars[evt.joy].handleEvent(evt)
            if evt.type == pygame.KEYDOWN or evt.type == pygame.KEYUP:
                guitars['K'].handleEvent(evt)
        
g = Game()
g.play()
