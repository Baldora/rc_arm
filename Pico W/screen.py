from machine import Pin, SoftI2C
import ssd1306
from time import sleep_ms

class Screen:
    def __init__(self, scl_pin:int, sda_pin:int, display_width:int, display_height:int):
        '''
        initalize the screen, needs scl & sda pin also need the display width and height
        '''
        
        self.i2c = SoftI2C(scl=Pin(scl_pin), sda=Pin(sda_pin))

        self.display_width = display_width
        self.display_height = display_height
        self.display = ssd1306.SSD1306_I2C(self.display_width, self.display_height, self.i2c)

    def update_screen(self, display_text:list[str]):

        counter = 0

        for line in display_text:
            display_line = counter * 10
            self.display.text(line , 0, display_line)

            counter += 1

        self.display.show()
        self.display.fill(0)
        sleep_ms(100)