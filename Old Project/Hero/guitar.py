#~ Guitar
#~ author: Logan Wilkerson
#~ Description: This class simulates a guitar controller class,
#~ the keys are bound individually, and the class handles the sound
#~ as well.

import pygame
pygame.mixer.pre_init(22050, -16, 1, 64)
pygame.init()

class Guitar(object):
    def __init__(self, id):
        #All buttons start at -1
        #Class will not handle events unless this is changed
        self.guitarID = id
        self.flag = -1
        self.green = self.flag
        self.red = self.flag
        self.yellow = self.flag
        self.blue = self.flag
        self.orange = self.flag
        self.noButton = -1
        self.twangerDown = self.flag
        self.twangerUp = self.flag
        
        self.soundList = []
        
        #Button info is added to maps as it is set
        self.buttonMap = {self.noButton:0}
        self.buttonDownMap = {self.noButton:True}
        
        #Lowest button current held down
        self.currentButton = self.noButton
        self.soundUp = None
        self.soundDown = None
        self.sound = None
        self.channel = pygame.mixer.Channel(id)
        pygame.mixer.set_reserved(id)
        
        #Max notes at 12, really just implemented for ease of logic
        self.maxSounds = 12
        
    #Accessor
    def getID(self):
        return self.guitarID
        
        
    def handleButton(self,event):
      if event.type == pygame.JOYBUTTONDOWN:
        if event.button == self.twangerDown:
          self.stopSound()
          self.play(self.soundDown)
          return
        elif event.button == self.twangerUp:
          self.stopSound()
          self.play(self.soundUp)
          return
          
        if self.isFretButton(event.button):
          self.buttonDownMap[event.button] = True
          if self.compareToCurrent(event.button) >= 0:
            self.clearSound()
            self.currentButton = event.button
            self.setUpperSound(self.currentButton)
            self.setLowerSound(self.currentButton)
          
      elif event.type == pygame.JOYBUTTONUP:
        if self.isFretButton(event.button):
          self.buttonDownMap[event.button] = False
          if self.compareToCurrent(event.button) == 0:
            self.clearSound()
            for i in [self.orange, self.blue, self.yellow, self.red, self.green, self.noButton]:
              if self.buttonDownMap[i] == True:
                self.currentButton = i
                self.setUpperSound(self.currentButton)
                self.setLowerSound(self.currentButton)
                return
      else:
        return
        
    
    #Are the buttons set?
    def buttonsSet(self):
        self.isSet = self.green != self.flag and self.red != self.flag and self.yellow != self.flag and self.blue != self.flag and self.orange != self.flag and self.twangerDown != self.flag and self.twangerUp != self.flag
        self.isSet = self.isSet and len(self.soundList) == self.maxSounds
        return self.isSet
    
    
    def playUp(self):
      if not self.channel:
        self.channel = pygame.mixer.find_channel(False)
      self.channel.play(self.soundUp)
      
    def playDown(self):
      if not self.channel:
        self.channel = pygame.mixer.find_channel(False)
      self.channel.play(self.soundDown)
      
    def play(self, sound):
      if not self.channel:
        self.channel = pygame.mixer.find_channel(False)
      self.channel.play(sound)
     
    
    def setSoundList(self, lst):
        for snd in lst:
            self.soundList.append(snd)
        self.setUpperSound(self.currentButton)
        self.setLowerSound(self.currentButton)
        
    def setGreen(self, key):
        if(self.green == self.flag):
            self.green = key
            self.buttonMap.update({self.green:1})
            self.buttonDownMap.update({self.green:False})
    
    def setRed(self, key):
        if(self.red == self.flag):
            self.red = key
            self.buttonMap.update({self.red:2})
            self.buttonDownMap.update({self.red:False})
        
    def setYellow(self, key):
        if(self.yellow == self.flag):
            self.yellow = key
            self.buttonMap.update({self.yellow:3})
            self.buttonDownMap.update({self.yellow:False})
        
    def setBlue(self, key):
        if(self.blue == self.flag):
            self.blue = key
            self.buttonMap.update({self.blue:4})
            self.buttonDownMap.update({self.blue:False})
        
    def setOrange(self, key):
        if(self.orange == self.flag):
            self.orange = key
            self.buttonMap.update({self.orange:5})
            self.buttonDownMap.update({self.orange:False})
        
    def setTwangerDown(self, key):
        if(self.twangerDown == self.flag):
            self.twangerDown = key
        
    def setTwangerUp(self,key):
        if(self.twangerUp == self.flag):
            self.twangerUp = key
     
    def setLowerSound(self, button):
      if(not self.soundDown == self.soundList[self.buttonMap[button]+6]):
        self.soundDown = self.soundList[self.buttonMap[button] + 6]
        
    def setUpperSound(self,button):
      if(not self.soundUp == self.soundList[self.buttonMap[button]]):
        self.soundUp = self.soundList[self.buttonMap[button]]
        
    def clearSound(self):
        self.fadeSound()
        self.currentButton = self.noButton
        
    def clearStopSound(self):
        self.stopSound()
        self.currentButton = self.clear
        
    def stopSound(self):
        if self.channel:
            self.channel.stop()
            
    def stopSoundDown(self):
      if self.soundDown:
        self.soundDown.stop()
        
    def stopSoundUp(self):
      if self.soundUp:
        self.soundUp.stop()
            
    def fadeSound(self):
        if self.channel:
            self.channel.fadeout(500)
            
    def isFretButton(self, button):
        return button in self.buttonMap.keys()
        
    def compareToCurrent(self,button):
        return self.buttonMap[button] - self.buttonMap[self.currentButton]