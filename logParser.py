import matplotlib.pyplot as plt

def parseLogFile(filename):    
    """Parses a log file and returns a dictionary of name to log data 
    which itself is a dictionary containing timestamps, data and the header
    """
    # Timestamp,isHeader(1 or 0),name,logginglevel,val1,val2,val3,...
    nameData = {}
    with open(filename) as f:
        # For every line in the file, determine if it is a header and handle appropriately
        for line in f:
            split = line.split(',')

            # Ignore commented lines or lines that are too small like empty lines
            if split[0][0] == '#' or len(split) < 4:
                continue
            
            # If Log Level isn't I then print out the line instead of graphing it
            if split[3] != 'I':
                print(line)
                continue

            # Remove trailing newline
            split[-1] = split[-1].rstrip('\n') 
            name = split[2]

            if split[1] == '1': # Handle header line
                nameData[name] = {}
                nameData[name]['header'] = split[4:]
                nameData[name]['data'] = {}
                for valName in split[4:]:
                    nameData[name]['data'][valName] = []
                nameData[name]['timestamps'] = []
            else: # Handle data line
                nameData[name]['timestamps'].append(float(split[0]))
                for valName, val in zip(nameData[name]['header'], split[4:]):
                    nameData[name]['data'][valName].append(float(val))
    return nameData