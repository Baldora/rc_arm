import serial

class DataReader:
    def __init__(self, port):
       
       self.serial = serial.Serial(port)

    def get_data(self):
        self.serial.reset_input_buffer()
        data = str(self.serial.readline())
        data = data.split("'")[1].replace("\\r\\n", "")
        x = data.split()[1]
        y = data.split()[3]
        data = {"x": x, "y": y}

        return data


