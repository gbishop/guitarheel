class Guitar(object):
    import pygame

    pygame.mixer.pre_init(44100, -16, 1, 512)

    pygame.init()   

    def isGuitarEvent(self, event):
        if pygame.JOYBUTTONDOWN == event.type or pygame.JOYBUTTONUP == event.type:
            return isFretButton(event.button)
        elif KEYUP == event.type or KEYDOWN == event.type:
            return isFretButton(event.key)
        else:
            return false
    
    def setSound(self, button):
        self.snd = PowerChord[self.buttonMap[button]]
        self.currentButton = button
        
    def clearSound(self):
        self.fadeSound()
        self.snd = None
        self.currentButton = self.green
        
    def clearStopSound(self):
        self.stopSound()
        self.snd = None
        self.currentButton = self.green
        
    def stopSound(self):
        if self.chan:
            self.chan.stop()
            
    def fadeSound(self):
        if self.chan:
            self.chan.fadeout(500)
            
    def isFretButton(self, button):
        return button in self.buttonMap
        
    def compareToCurrent(self, button):
        return self.buttonMap[button] - self.buttonMap[self.currentButton]
    def __init__(self, ControlList, Chords):
        self.green = controlList[0]
        self.red = controlList[1]
        self.yellow = controlList[2]
        self.blue = controlList[3]
        self.orange = controlList[4]
        self.clear = controlList[5]
        self.rock = controlList[6]
        self.twangerDown = controlList[7]
        self.twangerUp = controlList[8]
        self.select = controlList[9]
        self.start = controlList[10]
        self.currentButton = self.clear
        
        self.buttonMap = { self.clear:0, self.green:1, self.red:2, self.yellow:3,  self.blue:4, self.orange:5 }
        self.buttonDownMap = {self.clear:True, self.green:False, self.red:False, self.yellow:False, self.blue:False, self.orange:False}