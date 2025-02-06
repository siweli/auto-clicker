import pyautogui
import keyboard


toggle_button = 'insert'

last_state = False
while True:
    # CHECKS IF THE KEY LAST PRESSED WAS THE TOGGLE KEY
    # IF SO THEN TOGGLE THE SCRIPT TO ENABLED
    key_down = keyboard.is_pressed(toggle_button)
    if key_down != last_state:
        last_state = key_down
        if last_state:
            print(pyautogui.position())
