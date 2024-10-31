# This script changes the color of a bi-color LED connected to GPIO pins 14 and 15, a pushbutton is connected to GPIO pin 16.
# Be sure to put a 150Ω resistor beetween the bi-color LED and the other GPIO pin, the pushbutton does not need a pulldown resistor

from machine import Pin #By loading only the class called "Pin", we don't have to use machine.Pin in our code, we just use Pin
import utime                #Loads microtime library which allows us to keep time

# Define GPIO pins
button_pin = 16  # Button connected to GPIO 16
led1_pin = 14     #Negative Connection for bi-color LED
led2_pin = 15      #Positive connection for bi-color LED

# Set up the button as an input without an external pull-down resistor
button = Pin(button_pin, Pin.IN, Pin.PULL_DOWN)

# Set up the LED as an output
led1 = Pin(led1_pin, Pin.OUT)
led2 = Pin(led2_pin, Pin.OUT)

while True: #Using "while" in this way allows the program to run in a loop, untill the loop is broken
    if button.value() == 1:     #If button's value is high...
        led1.on()               #Turn GPIO pin 14 high
        led2.off()              #Turn GPIO pin 15 low
        utime.sleep(0.01)       #Wait 0.01 seconds
    else:                   #If button's value is low...
        led1.off()            #Turn GPIO pin 14 low
        led2.on()             #Turn GPIO pin 15 high
        utime.sleep(0.01)     #Wait 0.01 seconds
    
    # Small delay to debounce
    utime.sleep(0.01)