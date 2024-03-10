import random, pyautogui, time 
while True :
	x=random.randint(1,1489)
	y=random.randint(1,1876)
	pyautogui.moveTo(x,y,2)
	time.sleep(2)