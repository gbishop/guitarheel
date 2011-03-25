""" A modules containing Guitars to assist in dealing with guitar inputs

Authors: Logan Wilkerson
"""

import pygame
from datautilities.DataConstants import Constants
from sounds.SoundBoxes import AdvGuitarSoundBox

class Guitar(object):
    """ Assists in playing guitar sounds
    
    Authors: Logan Wilkerson
    """
    
    def __init__(self, sound_box, button_map, name='KEYBOARD'):
        """ Constructor for Guitar
        
        sound_box -- the AdvGuitarSoundBox for this guitar
        button_map -- a mapping of numbers to the associated joystick 
        button
        name -- the name of the joystick. If this is a keyboard based
        guitar leave this parameter out
        """
        self.sound_box = sound_box
        self.button_map = button_map
        self.name = name
        if name == 'KEYBOARD':
            self.down_event = pygame.KEYDOWN
            self.up_event = pygame.KEYUP
        else:
            self.down_event = pygame.JOYBUTTONDOWN
            self.up_event = pygame.JOYBUTTONUP
        
        self.states = {
            Constants.GREEN: 0,
            Constants.RED: 0,
            Constants.YELLOW: 0,
            Constants.BLUE: 0,
            Constants.ORANGE: 0,
            }
    
    def handleEvent(self, evt):
        """ Takes in an event and handles it. A TWANGERDOWN or TWANGERUP
        down event will cause the guitar to play sound depending on it's
        current state. Other events will alter this guitar's state. The 
        method returns either None, or the button pressed.
        
        evt -- the evt to be handled            
        """
        if self.name == 'KEYBOARD':
            if evt.key in self.button_map:
                button = self.button_map[evt.key]
            else:
                return None
        else:
            button = self.button_map[evt.button]
        if evt.type == self.down_event:
            if button == Constants.TWANGERDOWN or button == Constants.TWANGERUP:
                self.sound_box.play(self.states)
            else:
                if button in self.states:
                    self.states[button] = 1
        if evt.type == self.up_event:
            if button in self.states:
                self.states[button] = 0
                
        return button
