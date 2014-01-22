import pygame
import time
from time import sleep
import RPi.GPIO as GPIO
from random import choice
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.IN)

bad = ['wronganswer.wav', 'buzzwrong.wav', 'nottrue.wav', 'noway.wav']
good = ['youreright.wav','Cheering.wav', 'congratulations.wav', 'whyyes.wav']


pygame.init()      # Prepare the pygame module for use



def wrongPress(y):
    print y
    pygame.mixer.music.load(y)
    pygame.mixer.music.play()
    time.sleep(01)

def rightPress(y):
    print y
    pygame.mixer.music.load(y)
    pygame.mixer.music.play()
    time.sleep(01)
        
while True:
    try:
            if (GPIO.input(24) != 0):
                    print "24 pressed"                      #   leave the game loop.
                    randomBad = choice(bad)
                    wrongPress(randomBad)
                    #print randomBad
                    sleep(2.51);
            if (GPIO.input(25) != 0):
                    print "25 pressed"                      #   leave the game loop.
                    randomGood = choice(good)
                    rightPress(randomGood)
                    #print randomGood
                    sleep(2.51);
    except KeyboardInterrupt:
                exit()

  
