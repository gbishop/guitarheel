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
    
    def __init__(self, sound_box, button_map, name='KEYBOARD', id = -1):
        """ Constructor for Guitar
        
        sound_box -- the AdvGuitarSoundBox for this guitar
        button_map -- a mapping of numbers to the associated joystick 
        button
        name -- the name of the joystick. If this is a keyboard based
        guitar leave this parameter out
        id -- the id of the joystick for this guitar. If the guitar is 
                connected to a keyboard leave this value at its default
                id
        """
        self.sound_box = sound_box
        self.button_map = button_map
        self.name = name
        self.id = id
        if name is 'KEYBOARD':
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
    
    def handleEvent(self, evt, play=True):
        """ Takes in an event and handles it. A TWANGERDOWN or TWANGERUP
        down event will cause the guitar to play sound depending on it's
        current state. Other events will alter this guitar's state. The 
        method returns either None, or the button pressed.
        
        evt -- the evt to be handled 
        play -- True if the note should be played should the event call
                    for that.
        """
        if not self.isEventSource(evt):
            return None
        if self.name is 'KEYBOARD':
            if evt.key in self.button_map:
                button = self.button_map[evt.key]
            else:
                return None
        else:
            button = self.button_map[evt.button]
        if evt.type is self.down_event:
            if button is Constants.TWANGERDOWN or button is Constants.TWANGERUP:
                if play:
                    self.sound_box.play(self.states)
            else:
                if button in self.states:
                    self.states[button] = 1
        if evt.type is self.up_event:
            if button in self.states:
                self.states[button] = 0
                
        return button
        
    def isEventSource(self, evt):
        """Determines if this guitar is the source of the passed event
        
        evt -- the event in question
        """
        if evt.type is pygame.JOYBUTTONUP or evt.type is pygame.JOYBUTTONDOWN:
            return evt.joy is self.id
        elif evt.type is pygame.KEYDOWN or evt.type is pygame.KEYUP:
            return evt.key in self.button_map
        else:
            return False
            
    def getSoundBox(self):
        """returns the guitars sound box"""
        return self.sound_box
        
    def isPlay(self, evt,  button):
        """Returns true if the event and button combined represent
        a Play event. The button is usually aquired after the guitar
        handles an event to determine if the guitar just played.
        
        evt -- the event in question
        button -- the button string
        """
        return (evt.type is self.down_event and
                (button is Constants.TWANGERDOWN or
                button is Constants.TWANGERUP)
                )
    
    def getButtonStates(self):
        """returns the current button states of the guitar."""
        return self.states.values()
        
    def getNote(self):
        """Get the note string for the current state of the guitar. 
        The method asks the sound box to determine the note so the
        string returned depends on whether or not this guitar uses
        chords.
        """
        return self.sound_box.determine_note(self.states)
            
