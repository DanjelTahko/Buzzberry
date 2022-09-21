# The frequencies in this code was based on the note frequencies found at:
# https://pages.mtu.edu/~suits/notefreqs.html
# Tuned at A4 = 440Hz.
   
import RPi.GPIO as GPIO
from time import sleep
 
_NOTE_F3 = 175
_NOTE_A3 = 220
_NOTE_C4 = 262

_NOTE_E5 = 659 
_NOTE_C5 = 523
_NOTE_G5 = 784
_NOTE_G4 = 392
_NOTE_E4 = 330
_NOTE_A4 = 440
_NOTE_B4 = 494


_NOTE_AS4 = 466 # Bb4


# mario = [E5, E5, E5, C5, E5, G5, G4, C5, G4, E4, A4, B4, Bb4, A4]

class Piezo:

    def __init__(self):   
        GPIO.setwarnings(False)        # prevent warnings
        GPIO.setmode(GPIO.BOARD)       # setup I/O
        GPIO.setup(7, GPIO.OUT)        # sets pin 7 to output
        self.pwm = GPIO.PWM(7, 100)    # variable for pin 7 with frequency

    def play_mario(self):
       
       self.pwm.start(50) # Start Mario
       
       self.pwm.ChangeFrequency(_NOTE_E5)
       sleep(0.10)
       self.pause()

       self.pwm.ChangeFrequency(_NOTE_E5)
       sleep(0.15)
       self.pause()
       
       self.pwm.ChangeFrequency(_NOTE_E5)
       sleep(0.15)
       self.pause() 

       self.pwm.ChangeFrequency(_NOTE_C5)
       sleep(0.10)
       self.pwm.ChangeFrequency(_NOTE_E5)
       sleep(0.20)

       # --------------------
       self.pwm.ChangeFrequency(_NOTE_G5)
       sleep(0.5)

       self.pwm.ChangeFrequency(_NOTE_G4)
       sleep(0.4)
       self.pause()
       
       # ---------------------
       self.pwm.ChangeFrequency(_NOTE_C5)
       sleep(0.33)
       self.pwm.ChangeFrequency(_NOTE_G4)
       sleep(0.33)
       self.pwm.ChangeFrequency(_NOTE_E4)
       sleep(0.33)
       # ---------------------
       self.pwm.ChangeFrequency(_NOTE_A4)
       sleep(0.20)
       self.pause()
       self.pwm.ChangeFrequency(_NOTE_B4)
       sleep(0.20)
       self.pause()
       self.pwm.ChangeFrequency(_NOTE_AS4)
       sleep(0.10)
       self.pause()
       self.pwm.ChangeFrequency(_NOTE_A4)
       sleep(0.20)
       
       self.pwm.stop()

    def play_starwars(self):
        
        self.pwm.start(50) # Start imperial march
        
        self.pwm.ChangeFrequency(_NOTE_A3)
        sleep(0.4)
        self.pause()
         
        self.pwm.ChangeFrequency(_NOTE_A3)
        sleep(0.4)
        self.pause()

        self.pwm.ChangeFrequency(_NOTE_A3)
        sleep(0.4)   
        self.pause()

        self.pwm.ChangeFrequency(_NOTE_F3)
        sleep(0.25)   

        self.pwm.ChangeFrequency(_NOTE_C4)
        sleep(0.25)
        # ------------
        self.pwm.ChangeFrequency(_NOTE_A3)
        sleep(0.5)

        self.pwm.ChangeFrequency(_NOTE_F3)
        sleep(0.25)   

        self.pwm.ChangeFrequency(_NOTE_C4)
        sleep(0.25)

        self.pwm.ChangeFrequency(_NOTE_A3)
        sleep(1)

        self.pwm.stop()


    def pause(self):
        self.pwm.stop()
        sleep(0.1)
        self.pwm.start(50)


    def play(self, message):

        if (message == 'starwars'):
            self.play_starwars()
        elif (message == 'mario'):
            self.play_mario()
        elif (message == 'icecream'):
            # self.play_icecream()

    

"""
def main():
    # Testing purpose 
    piezo = Piezo()
    while(True):
        cin = str(input(">"))
        if (cin == '1'):
            piezo.play_mario()
        elif (cin == '2'):
            piezo.play()
        elif (cin == 'q'):
            break
    
if __name__ == "__main__":
     main()
     
"""

