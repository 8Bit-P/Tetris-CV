import win32gui
import time
import pygetwindow as gw
import pyautogui

def list_window_names():
        active_windows = []
        def winEnumHandler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                active_windows.append(win32gui.GetWindowText(hwnd))
        win32gui.EnumWindows(winEnumHandler, None)
        
        return active_windows

# Busca los nombres de ventana que contengan Tetris
def find_tetris_window():
    tetris_windows = []

    for windowName in list_window_names():
        if "Play Tetris" in windowName:
            tetris_windows.append(windowName)

    arr_len = len(tetris_windows)

    if( arr_len == 1): 
        return tetris_windows[0]
    elif(arr_len == 0):
        raise Exception("No se ha registrado ninguna partida en Tetris.com")
    elif(arr_len > 1):
        raise Exception("Hay mas de una partida jugandose a la vez")
    
def bring_window_to_foreground(window_name):
    window = gw.getWindowsWithTitle(window_name)

    if window:
        # Bring the window to the foreground
        window[0].activate()
        # If the window is minimized, maximize it
        if window[0].isMinimized:
            window[0].maximize()
    else:
        print(f'Window with title "{window_name}" not found.')

    # Optional: Wait a few seconds to see the window in the foreground
    time.sleep(5)

    # Example of typing something in the activated window
    pyautogui.write('Hello, this window has been activated by Python!', interval=0.1)

#Set window to occupy only half the screen
def setup_windows():
    pyautogui.hotkey('winleft', 'left')