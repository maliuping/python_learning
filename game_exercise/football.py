#!/usr/bin/python
from random import choice


scores = [0, 0]
direction = ["left","middle","right"]

def kick():
	print("======= You kick =======")
	print("please choose direction! left, middle, right")
	you =  raw_input()
	print("You kick %s"%you)
	com = choice(direction)
	print("Com save %s"%com)
	if you != com:
		scores[0] += 1
		print("you win!")
	elif you == com:
		print("com saved!")

	print("======= You save =======")
	print("please choose direction! left, middle, right")
	you = raw_input()
	print("You save %s"%you)
	com = choice(direction)
	print("Com kick %s"%com)
	if you == com:
		print("you saved!")
	elif you != com:
		scores[1] += 1
		print("Com win!")

for round in range(0,5):
	print("======= Round %d ======="%(round+1))
	kick()
while scores[0] == scores[1]:
	print("======= Round %d ======="%(round+1))
	kick()

print("******* Result *******")
if scores[0] > scores[1]:
	print("You win!")
else:
	print("Com win!")

print("====== Score: %d(You)::%d(Com) ====== \n"%(scores[0],scores[1]))
