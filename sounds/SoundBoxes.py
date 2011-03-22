"""
This module contains the different "sound boxes" that assit in determining
which sounds to play and actually playing them.

Authors: Logan Wilkerson,
"""
import pygame
from datautilities.DataConstants import Constants
import time

class GuitarSoundBox(object):
    """
    GuitarSoundBox
    The sound box for the guitar controller. It is set up to play notes after
    being passed the lowest fret
    Author: Logan Wilkerson
    """
    
    NO_NOTE = 0
    GREEN_NOTE = 1
    RED_NOTE = 2
    YELLOW_NOTE = 3
    BLUE_NOTE = 4
    ORANGE_NOTE = 5
    
    def __init__(self, sound_list, channel_id):
        self.sound_map = {
            GuitarSoundBox.NO_NOTE: pygame.mixer.Sound(sound_list[0]),
            GuitarSoundBox.GREEN_NOTE: pygame.mixer.Sound(sound_list[1]),
            GuitarSoundBox.RED_NOTE: pygame.mixer.Sound(sound_list[2]),
            GuitarSoundBox.YELLOW_NOTE: pygame.mixer.Sound(sound_list[3]),
            GuitarSoundBox.BLUE_NOTE: pygame.mixer.Sound(sound_list[4]),
            GuitarSoundBox.ORANGE_NOTE: pygame.mixer.Sound(sound_list[5]),
            }
        self.channel = pygame.mixer.find_channel()

    """
    play
    Plays a sound given the note.
    """
    def play(self, note):
        self.channel.play(self.sound_map[note])

class AdvGuitarSoundBox(object):
    """ A more advanced guitar sound box 
    
    Authors: Logan Wilkerson
    """
    
    button_map = {
    0: Constants.OPEN,
    1: Constants.GREEN,
    2: Constants.RED,
    3: Constants.YELLOW,
    4: Constants.BLUE,
    5: Constants.ORANGE,
    }
    
    def __init__(self, file_name, sound_list):
        """ Constructor for AdvGuitarSoundBox
        
        file_name -- the file name for the instrument this "guitar" relates too
        sound_list -- maps the individual key states to sound files
        """        
        self.sound_map = {}
        dir = 'notes/' + file_name + '/'
        for key in sound_list:
            self.sound_map[key] = pygame.mixer.Sound(dir + sound_list[key])
        self.channel = pygame.mixer.find_channel()
        
    def determine_note(self, states):
        count = 0
        last_button_down = Constants.OPEN
        state_string = ''
        if states[Constants.GREEN] == 1:
            last_button_down = Constants.GREEN
            state_string += Constants.GREEN
        if states[Constants.RED] == 1:
            last_button_down = Constants.RED
            state_string += Constants.RED
        if states[Constants.YELLOW] == 1:
            last_button_down = Constants.YELLOW
            state_string += Constants.YELLOW
        if states[Constants.BLUE] == 1:
            last_button_down = Constants.BLUE
            state_string += Constants.BLUE
        if states[Constants.ORANGE] == 1:
            last_button_down = Constants.ORANGE
            state_string += Constants.ORANGE
            
        if state_string in self.sound_map:
            return state_string
        else:
            return last_button_down
            
    def play(self, states):
        """ Plays the sound associated with guitar state
        
        states -- The current state of the guitar. This is a dictionary with the keys being the
            Constants for each key (Constants.GREEN, etc) and the values being a 1 if the key
            is down and a 0 otherwise.
        """
        self.channel.play(self.sound_map[self.determine_note(states)])
        
    def fadeout(self, fade_time=500):
        self.channel.fadeout(fade_time)
        
class InstrumentNameSoundBox(object):
    """ Reads in all the instrument names and their SPOKEN_NAME and plays the spoken names
    
    Authors: Logan Wilkerson
    """
    
    def __init__(self, instrument_list):
        """  Constructor for InstrumentNameSoundBox
        
        instrument_list -- the data dictionary retrived from reading the note data file
            using the DataProcessors.NoteDataReader class        
        """
        self.sound_map = {}
        for key in instrument_list.keys():
            dir = 'notes/' + key + '/'
            self.sound_map[key] = pygame.mixer.Sound(dir + instrument_list[key][Constants.SPOKEN_NAME])
        self.channel = pygame.mixer.find_channel()
        
    def say_name(self, instrument_name):
        """ Plays the sound file associated with the instrument's name
        
        instrument_name -- name of the instrument        
        """
        self.channel.play(self.sound_map[instrument_name])
    
    def fadeout(self, fade_time=1000):
        """ Fades out the currently playing sound for this object
        
        fade_time -- The time to fade in milliseconds. Defaults to 1000 ms
        """
        self.channel.fadeout(fade_time)

    def __str__(self):
        return repr(self.sound_map) + ' ' + repr(self.channel)