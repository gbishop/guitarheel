import os, sys
from datautilities.DataConstants import Constants



"""
NoteDataReader
This class contains all static methods that will read the notedata.dat file and parse
it into a easy to use data structure. It returns a dictionary where the keys are the 
instrument ids (also their file name) and the values are another set of dictionaries 
with key states and the file for each key state. The values also contain a file connected
to the key 'SPOKEN_NAME' which is a file containing the instruments spoken name.

"""
class NoteDataReader(object):
    my_data_file_string = os.path.join('data', 'notedata.dat')

    @staticmethod
    def getData():
        data_file = open(NoteDataReader.my_data_file_string);
        data = {}
        for line in data_file:
            striped_line = line.strip()
            if not NoteDataReader.isIgnoredLine(striped_line):
                split_line = striped_line.split(' ')
                if not len(split_line) == 2:
                    raise ConfigFileSyntaxException('Syntax Error on instrument header: ' + striped_line)
                else:
                    data[split_line[0]] = NoteDataReader.getInstrument(split_line[1], data_file)
        return data
    
    @staticmethod
    def getInstrument(voice_file, data_file):
        data = {Constants.SPOKEN_NAME: voice_file}
        for line in data_file:
            striped_line = line.strip();
            if not NoteDataReader.isIgnoredLine(striped_line):
                if striped_line == '-':
                    break
                split_line = striped_line.split(' ')
                if not len(split_line) == 2:
                    raise ConfigFileSyntaxException('Syntax Error in note data: ' + striped_line)
                else:
                    data[split_line[0]] = split_line[1]
        return data
            
    @staticmethod
    def isIgnoredLine(line):
        return len(line) == 0 or line[0] == '#'
        
class ConfigFileSyntaxException(Exception):
    def __init__(self, value):
        self.value = value
        
    def __str__(self):
        return repr(self.value)
        
if __name__ == "__main__":
    data = NoteDataReader.getData()
    print data
   
