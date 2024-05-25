import time
import cv2
import pyautogui
import numpy as np
import utils

def take_screenshot():
    #Takes screenshot and returns it
    image = pyautogui.screenshot()
   
    # since the pyautogui takes as a 
    # PIL(pillow) and in RGB we need to 
    # convert it to numpy array and BGR 
    # so we can write it to the disk
    image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
    return image



def main():

    print("Starting Tetris CV.")
    time.sleep(1)
    print("Make sure you have an instance of tetris.com/play-tetris opened.")
    time.sleep(1)
    print("Starting detection in: ")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)

    #Main loop
    """ 
    while True:
        screenshot = take_screenshot()
        time.sleep(0.5) # Sleep for half a second
    """
    #Prepare window and set it to half of the screen
    tetris_window = utils.find_tetris_window()
    utils.bring_window_to_foreground(tetris_window)
    utils.cut_window()

    """
    screenshot = take_screenshot()
    cv2.imshow("Test window", screenshot) 
  
    # waits for user to press any key 
    # (this is necessary to avoid Python kernel form crashing) 
    cv2.waitKey(0) 
    
    # closing all open windows 
    cv2.destroyAllWindows() 
    """

main()