import pygame
import sys
pygame.mixer.pre_init(44100,-16,1,512)
pygame.init()

sounds = [pygame.mixer.Sound('%s' % str) for str in ['speed_kills.ogg','walk_this_way.ogg','bassloopone.ogg','akiwawa.ogg','analog.ogg','nosound.ogg']]

class DrumLoop(object):
  def __init__(self):
    self.channel = None
    self.sound = None
    self.currentSound = 0
    self.maxSound = len(sounds)
    
  def playDrum(self):
    self.sound = self.pickSound()
    
    self.channel.play(self.sound, -1)
      
  def pickSound(self):
      self.previousSound = -1
      while True:
        if(not self.currentSound == self.previousSound):
            if(self.currentSound == self.maxSound):
                self.currentSound = 0
            elif(self.currentSound == -1):
              self.currentSound = self.maxSound - 1
            self.previousSound = self.currentSound
              
            self.sound = sounds[self.currentSound]
            self.play()
        self.event = pygame.event.wait()
        if self.event.type == pygame.QUIT:
            sys.exit(0)
        if self.event.type == pygame.KEYDOWN and self.event.key == pygame.K_UP:
            self.currentSound += 1
        elif self.event.type == pygame.KEYDOWN and self.event.key == pygame.K_DOWN:
            self.currentSound -= 1
        elif self.event.type == pygame.KEYDOWN and self.event.key == pygame.K_RETURN:
            self.channel.stop()
            return sounds[self.currentSound]
            
        if self.event.type == pygame.JOYBUTTONDOWN and self.event.button == 14:
              self.currentSound += 1
        elif self.event.type == pygame.JOYBUTTONDOWN and self.event.button == 12:
              self.currentSound -= 1
        elif self.event.type == pygame.JOYBUTTONDOWN and self.event.button == 5:
            self.channel.stop()
            return sounds[self.currentSound]
            
  def play(self):
    if not self.channel:
          self.channel = pygame.mixer.Channel(7)
          pygame.mixer.set_reserved(7)
    self.channel.play(sounds[self.currentSound])
    