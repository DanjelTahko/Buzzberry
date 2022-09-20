# The frequencies in this code was based on the note frequencies found at:
# https://pages.mtu.edu/~suits/notefreqs.html
# Tuned at A4 = 440Hz.
   
import RPi.GPIO as GPIO
from time import sleep
 
_NOTE_F3 = 175
_NOTE_A3 = 220
_NOTE_C4 = 262

class Piezo:

    def __init__(self):   
        GPIO.setwarnings(False)        # prevent warnings
        GPIO.setmode(GPIO.BOARD)       # setup I/O
        GPIO.setup(7, GPIO.OUT)        # sets pin 7 to output
        self.pwn = GPIO.PWM(7, 100)    # variable for pin 7 with frequency

    def play(self):
        
        self.pwn.start(50) # Start imperial march
        
        self.pwn.ChangeFrequency(_NOTE_A3)
        sleep(0.4)
        self.pause()
         
        self.pwn.ChangeFrequency(_NOTE_A3)
        sleep(0.4)
        self.pause()

        self.pwn.ChangeFrequency(_NOTE_A3)
        sleep(0.4)   
        self.pause()

        self.pwn.ChangeFrequency(_NOTE_F3)
        sleep(0.25)   

        self.pwn.ChangeFrequency(_NOTE_C4)
        sleep(0.25)
        # ------------
        self.pwn.ChangeFrequency(_NOTE_A3)
        sleep(0.5)

        self.pwn.ChangeFrequency(_NOTE_F3)
        sleep(0.25)   

        self.pwn.ChangeFrequency(_NOTE_C4)
        sleep(0.25)

        self.pwn.ChangeFrequency(_NOTE_A3)
        sleep(1)

        self.pwn.stop()


    def pause(self):
        self.pwn.stop()
        sleep(0.1)
        self.pwn.start(50)

    


def main():
    # Testing purpose 
    piezo = Piezo()
    while(True):
        cin = str(input(">"))
        if (cin == '1'):
            piezo.play()
        elif (cin == 'q'):
            break
    
if __name__ == "__main__":
     main()
