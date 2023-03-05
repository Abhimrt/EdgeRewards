import pyautogui,time
time.sleep(2)

NumberOfSearch = int(pyautogui.prompt('Number of Search'));
NumberOfProfile = int(pyautogui.prompt('Number of Profile'));

# button position 
x,y = 1532,63
# close button position
x1,y1 = 26,21

pyautogui.keyDown('command')
pyautogui.press('space')
pyautogui.keyUp('command')
pyautogui.write("microsoft Edge")
pyautogui.press('enter') 
time.sleep(3)

# for searching
def search():
    pyautogui.keyDown('command')
    pyautogui.press('t')
    pyautogui.keyUp('command')
    pyautogui.write("fsda")
    pyautogui.press('enter') 
    for i in range(0,NumberOfSearch):
        time.sleep(.4)
        pyautogui.keyDown('command')
        pyautogui.press(str((i%2)+1))
        pyautogui.press("l")
        pyautogui.keyUp('command')
        pyautogui.write(str(i))
        pyautogui.press('enter') 

# for first profile
search()


# # for next profiles
for i in range(0,NumberOfProfile):
    time.sleep(.5)
    if i!=0:
        pyautogui.click(x1, y1)
        time.sleep(.5)
    pyautogui.click(x, y)
    time.sleep(.5)

    # for accessing the next profile
    for j in range(-1,i):
        pyautogui.press('tab') 
    time.sleep(.5)
    pyautogui.press('enter') 

    # for searching
    search()

for i in range(0,2):
    pyautogui.keyDown('command')
    pyautogui.press('Q')
    pyautogui.keyUp('command')

'''
    Data
    profile access = (x=1532, y=63)

'''