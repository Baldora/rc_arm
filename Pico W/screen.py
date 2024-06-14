from machine import Pin, SoftI2C
from libary import ssd1306
from time import sleep_ms

class Screen:
    '''
    screen object handles updates to the oled screen and holds screen info (data pins and size)
    '''
    def __init__(self, scl_pin:int, sda_pin:int, display_width:int, display_height:int):
        '''
        initalize the screen, needs scl & sda pin also need the display width and height
        '''
        
        #setup data pins
        self.i2c = SoftI2C(scl=Pin(scl_pin), sda=Pin(sda_pin))
        #save screen size info
        self.display_width = display_width
        self.display_height = display_height
        #setup the display object
        self.display = ssd1306.SSD1306_I2C(self.display_width, self.display_height, self.i2c)

    def update_screen(self, display_text:list[str]):
        '''
        updates the screen with new text.

        takes in a list of lines then displays them one line per element
        '''
        #set counter to 0 (tracks what line is being written)
        counter = 0

        #for each element write a new line on the display
        for line in display_text:
            display_line = counter * 10
            self.display.text(line , 0, display_line)

            counter += 1

        #update the display with the new text
        self.display.show()
        self.display.fill(0)
        sleep_ms(100)