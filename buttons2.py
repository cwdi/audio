import pygame
import time
from time import sleep
import RPi.GPIO as GPIO
from random import choice
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.IN)

bad = ['wronganswer.wav', 'buzzwrong.wav']
good = ['youreright.wav','Cheering.wav']

def main():
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use



    def wrongPress(y):
        pygame.mixer.music.load(y)
        pygame.mixer.music.play()
        time.sleep(01)

    def rightPress(y):
        pygame.mixer.music.load(y)
        pygame.mixer.music.play()
        time.sleep(01)
        
    while True:
        try:
                if (GPIO.input(24) != 0):
                        print "24 pressed"                      #   leave the game loop.
                        randomBad = choice(bad)
                        wrongPress(randomBad)
                        print randomBad
                        sleep(2.51);
                if (GPIO.input(25) != 0):
                        print "24 pressed"                      #   leave the game loop.
                        randomGood = choice(good)
                        rightPress(randomGood % str)
                        print randomGood
                        sleep(2.51);
        except KeyboardInterrupt:
                exit()

  
