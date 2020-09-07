import pyautogui # install pyautogui for using keyboard and mouse on auto
from PIL import Image, ImageGrab #pip install pillow (ImageGrab used to take screenshot)
import time

def hit(key):
    pyautogui.keyDown(key)

def takeScreenshot():
    '''This function will help us to take the screenshot whenever we need it'''
    image = ImageGrab.grab().convert('L') #image in grayscale
    return image

def checkColour(data):
    for i in range(50, 80):
        for j in range(285, 325):
            if data[i, j] < 150:    #black screen                                                                                                                                                                                                                                               
                ind = 0
                return ind
            elif data[i, j] > 200:  ##white screen
                ind = 1
                return ind

def isCollide(data):
    ''' function to jump the dragon before the collision '''
    pin = 1
    ind = checkColour(data)

    if ind == pin:
        k = 0
    else:
        k = 40
        pin = ind

    for i in range(665, 830+k):
        for j in range(285, 325):
            if ind == 1:
                if data[i, j] < 150:
                    hit('up')
                    return
            elif ind == 0:
                if data[i, j] > 150:
                    hit('up')
                    return


if __name__ == "__main__":
    print('Hey... Dino game about to start in 2 seconds')
    # just open the browser screen with dino game on it, program will play the game by it's own
    time.sleep(2)
    hit('up')
    while True:
        image = takeScreenshot()
        data = image.load()
        isCollide(data)