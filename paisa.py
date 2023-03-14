import pyautogui,time
pyautogui.PAUSE = 1
time.sleep(2)

    # NumberOfSearch = in   t(pyautogui.prompt('Number of Search'))

# india         
NumberOfSearchMob,NumberOfSearchPC = "30","40"

# usa
# NumberOfSearchMob,NumberOfSearchPC = "40","60"

NumberOfProfile = 17;

# button position 
x,y = 1532,63
# close button position
x1,y1 = 26,21

# for searching
def search():
    pyautogui.keyDown('command')
    pyautogui.press('t')
    pyautogui.keyUp('command')
    pyautogui.write("fsda")
    pyautogui.press('enter') 
    for i in range(0,NumberOfSearch):
        pyautogui.keyDown('command')
        pyautogui.press(str((i%2)+1))
        pyautogui.press("l")
        pyautogui.keyUp('command')
        pyautogui.write(str(i))
        pyautogui.press('enter') 
# search()


def extension():
    pyautogui.click(1567,52) #menu
    pyautogui.click(1424,394) #extension
    pyautogui.typewrite("")
    pyautogui.press('enter')     
    pyautogui.typewrite("")           
    pyautogui.press('tab')
    pyautogui.typewrite(NumberOfSearchPC)
    pyautogui.press('tab')
    pyautogui.typewrite(NumberOfSearchMob)
    for i in range(0,5):
        pyautogui.press('tab')
    pyautogui.press('enter')
extension()


# # for  profiles
for i in range(0,NumberOfProfile):
    # if i!=0:
    #     pyautogui.click(x1, y1)
    pyautogui.click(x, y)

    # for accessing the next profile
    for j in range(-1,i):
        pyautogui.press('tab') 
    pyautogui.press('enter') 
    # for searching
    # search()
    extension()





'''
    Data
    profile access = (x=1532, y=63)

'''