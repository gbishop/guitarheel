""" Module contains the abstract game class

Authors: Logan Wilkerson,
"""


class AbstractGame(object):
    """This is the Abstract Game class. All minigames *must* 
    inherit this class in order to function properly
    
    A game class must implement the following methods:
    update
    
    Authors: Logan Wilkerson,
    """
    running_status = 'RUNNING'
    end_status = 'END'
    def update(self, evt=None):
        """The update method for a game. The update method may take in
        an event. The game loop should also call the update method at
        least once per loop with no event. The game can use this chance
        to update any none event based events, or to update after a
        collection of events. 
        
        This method should return a list with the following 
        information:
        
        return[0]: the game status. It should be either 'RUNNING' if the
            game is still running, or 'END' if it is no longer running
        return[1]: the game name to be run after this one. Most often 
            this is just a menu type set up.
        return[2:]: Any extra parameters that might be needed by the
            next game        
        
        evt -- a user event
        """
        raise NotImplementedError("This method has not been implemented")
