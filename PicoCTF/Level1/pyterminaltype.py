import pyautogui
print "This script activates a terminal window by automating the mouse movement and clicking.\n"
print "To choose which terminal will be activated the coordinates of the mouse click need to be recorded.\n"
print "To begin, please move your mouse to the middle of this window then press enter when ready...\n"
raw_input('Waiting...')
hx,hy=pyautogui.position()
print "(",hx,",",hy,") Captured.\n"
print "place the mouse curser in the middle of the window to be activated then press enter when ready\n"
raw_input('Waiting...')
wx,wy=pyautogui.position()
print "(",wx,",",wy,") Captured.\n"
print "enter the text which will be autotyped. To repeatedly autotype enter comma (,) after the text and then the number of repeats\n"
s=raw_input()
ls=s.split(',')
t=ls[0]
if len(ls)>1:
    r=int(ls[1])
    t=(ls[0])*r
pyautogui.click(wx,wy)
pyautogui.typewrite(t)
pyautogui.click(hx,hy)

