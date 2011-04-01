"""A module containing classes to manage the reserving and handing out
of channels

Authors: Logan Wlkerson,
"""

import pygame


class ChannelManager(object):
    """Manages the handing out of sound channels
    
    Authors: Logan Wilkerson,
    """
    
    def __init__(self, num_channels):
        """The constructor for the sound manager
        
        num_channels -- number of channels to be reserved by the sound manager
        """
        pygame.mixer.set_reserved(num_channels)
        self.unused_channel_list = []
        for id in range(0, num_channels):
            self.unused_channel_list.append(pygame.mixer.Channel(id))
        
        self.used_channel_map = {}
        
    def reserveChannel(self, reserver):
        """Reserves a channel for a reserver
        
        reserver -- the reserver
        """
        channel = self.unused_channel_list.pop(0)
        self.used_channel_map[reserver] = channel
        return channel
        
    def releaseChannel(self, reserver):
        """Releases the channel belonging to the reserver
        
        reserver -- the original reserver
        """
        channel = self.used_channel_map[reserver]
        del self.used_channel_map[reserver]
        self.unused_channel_list.append(channel)
        
    def printinfo(self):
        """Prints some info about the manager. Mainly for debugging"""
        print self.unused_channel_list
        print self.used_channel_map
