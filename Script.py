from pynput.keyboard import Key, Controller
import time
import pydirectinput
import random
options = ['a','w','s','d']
while True:
	choice = random.choice(options)
	pydirectinput.keyDown('2')
	time.sleep(random.randrange(3))
	pydirectinput.keyUp('2')
	pydirectinput.click()
	for i in range(random.randrange(5)):   
		pydirectinput.keyDown(choice)
		time.sleep(random.randrange(3))
		pydirectinput.keyUp(choice)

		pydirectinput.keyDown('2')
		time.sleep(random.randrange(3))
		pydirectinput.keyUp('2')
		pydirectinput.click()

		time.sleep(random.randrange(10))
