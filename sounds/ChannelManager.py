"""A module containing classes to manage the reserving and handing out
of channels

Authors: Logan Wlkerson,
"""

import pygame

class ChannelManager(Object):
    """Manages the handing out of sound channels
    
    Authors: Logan Wilkerson,
    """
    
    def __init__(self):
        """The constructor for the sound manager"""
        self.x = 0
