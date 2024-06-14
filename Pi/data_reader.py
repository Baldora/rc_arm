import serial

class DataReader:
    '''
    handles reading data from pico W coming over the serial port
    '''
    def __init__(self, port):
       '''
       on setup sets the port it will be listening to
       '''
       self.serial = serial.Serial(port)

    def get_data(self):
        '''
        gets the data from the pico W and converts it to a dictonary with 'x' and 'y'
        '''

        #reset the buffer to remove old data that was waiting
        self.serial.reset_input_buffer()
        #read next line sent
        data = str(self.serial.readline())
        #Remove extra parts from the string
        data = data.split("'")[1].replace("\\r\\n", "")
        #remove the x and y data and put it in a dictonary
        x = data.split()[1]
        y = data.split()[3]
        data = {"x": x, "y": y}

        #return the data
        return data


