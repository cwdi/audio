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
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop

        if ev.type == pygame.KEYDOWN:
          key = ev.dict["key"]
          if ( GPIO.input(24) != 0 ):     # b key press             
              print "24 pressed"                      #   leave the game loop.
              randomBad = choice(bad)
              wrongPress(randomBad)
              print randomBad
              sleep(2.51);
          elif key == 97:   #a key press
              print "24 pressed"                      #   leave the game loop.
              randomGood = choice(good)
              rightPress(randomGood % str)
              print randomGood
              sleep(2.51);
          elif key == 27:                  # On Escape key ...
            break  
          

        # Update your game objects and data structures here...


    pygame.quit()     # Once we leave the loop, close the window.

main()
