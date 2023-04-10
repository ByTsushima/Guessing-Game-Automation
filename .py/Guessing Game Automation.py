import keyboard
import pyautogui
import time

print("PROJECT: TSUSHIMA")

MAX_NUMBER = 1000000
MID_NUMBER = 500000
MIN_NUMBER = 0
TIMER = 1
CONFIDENCE = 0.8

atm_input = pyautogui.locateOnScreen('AtmInput.png', grayscale=True, confidence=CONFIDENCE)

def on_right_arrow_press(event, mid_number):
    
    if event.name == 'right':    
        keyboard.write(str(int(mid_number)))

def on_up_arrow_press(event, max_number, min_number, mid_number):
    
    if event.name == 'down':    
        max_number = mid_number
        mid_number = (max_number + min_number) // 2
        
        keyboard.write(str(int(mid_number)))
        
        return max_number, min_number, mid_number

    return max_number, min_number, mid_number

def on_down_arrow_press(event, max_number, min_number, mid_number):
    
    if event.name == 'up':
        min_number = mid_number
        mid_number = (min_number + max_number) // 2
        
        keyboard.write(str(int(mid_number)))
        
        return max_number, min_number, mid_number
    
    return max_number, min_number, mid_number

def on_left_arrow_press(event):
    
    if event.name == 'left':
        mid_number = MID_NUMBER

        keyboard.write(str(int(mid_number)))

        return mid_number
    
    return None

while True:
    
    if pyautogui.locateOnScreen('AtmDialog.png', grayscale=True, confidence=CONFIDENCE):
        
        pyautogui.click(atm_input)
        
        time.sleep(TIMER)
        
        if pyautogui.locateOnScreen('Low.png', grayscale=True, confidence=CONFIDENCE):
            
            pyautogui.press('CTRL + A')
            pyautogui.press('Delete')
            
            MAX_NUMBER, MIN_NUMBER, MID_NUMBER = on_up_arrow_press(None, MAX_NUMBER, MIN_NUMBER, MID_NUMBER)
            
            time.sleep(TIMER)
            
            pyautogui.press('Enter')
        
        if pyautogui.locateOnScreen('High.png', grayscale=True, confidence=CONFIDENCE):
            
            pyautogui.press('CTRL + A')
            pyautogui.press('Delete')
            
            MAX_NUMBER, MIN_NUMBER, MID_NUMBER = on_down_arrow_press(None, MAX_NUMBER, MIN_NUMBER, MID_NUMBER)
                
            time.sleep(TIMER)
            
            pyautogui.press('Enter')
            
    events = keyboard.record(until='esc')
    
    for event in events:
        
        mid_number = on_left_arrow_press(event)
        
        if mid_number is not None:
            MAX_NUMBER = 1000000
            MIN_NUMBER = 0
            MID_NUMBER = mid_number
        
        MAX_NUMBER, MIN_NUMBER, MID_NUMBER = on_up_arrow_press(event, MAX_NUMBER, MIN_NUMBER, MID_NUMBER)
        MAX_NUMBER, MIN_NUMBER, MID_NUMBER = on_down_arrow_press(event, MAX_NUMBER, MIN_NUMBER, MID_NUMBER)
