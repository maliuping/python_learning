#!/usr/bin/python
#-*- coding: utf-8 -*-
from random import randint

def Is_equal(answer,num):
	if answer < num:
		print("too small!")
		return False
	elif answer > num:
		print("too big!")
		return False
	else:
		print("bingo!")
		return True
##########################################

ret = False
name = raw_input("请输入玩家名字:") #输入玩家名字
f = open("cmd.txt")
lines = f.readlines()
f.close()

scores = {} #初始化一个空字典
for line in lines:
	s = line.split()
	#print(s)
	scores[s[0]] = s[1:]

score = scores.get(name)
if score is None:
	score = [0, 0, 0] #如果该账号无成绩，则初始化成0

game_times = int(score[0])
min_times = int(score[1])
total_times = int(score[2])
avg_times = 0
if game_times == 0 or game_times<0:
	avg_times = 0
else:
	avg_times = float(total_times)/game_times
print("%s,你已经玩了%d次游戏，最快%d轮猜出，平均每%.2f轮猜出"%(name,game_times,min_times,avg_times))

times = 0
num =  randint(0,100)
print("you guess what do i think?")
while ret == False:
	times += 1
	myNum = input()
	ret = Is_equal(myNum,num)

if game_times==0 or times<min_times:
	min_times = times

game_times += 1
total_times += times

scores[name] = [str(game_times),str(min_times),str(total_times)]
#print(scores)
#print(scores[name])

result = " "
for per in scores:
	per_line = per + " " + " ".join(scores[per]) + "\n" 
	result += per_line
#print(result)
f = open("cmd.txt","w")
f.write(result)
f.close()
