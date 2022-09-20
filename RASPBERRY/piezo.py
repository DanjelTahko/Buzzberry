# The frequencies in this code was based on the note frequencies found at:
# https://pages.mtu.edu/~suits/notefreqs.html
# Tuned at A4 = 440Hz.
 
 # imports:  
import RPi.GPIO as GPIO
from time import sleep
 
 # setup commands:
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
pin7 = GPIO.PWM(7, 100)
pin7.start(50)
 
 # looped commands: 
while True:
  GPIO.output(7, GPIO.HIGH)           # set high
  pin7.ChangeFrequency(16.35) # C0
  sleep(1)
  pin7.ChangeFrequency(261.63) # C4
  sleep(1)
  pin7.ChangeFrequency(293.66) # D4
  GPIO.output(7, GPIO.LOW)            # set low 
  sleep(1)