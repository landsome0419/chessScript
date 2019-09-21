#This is a python script that will make pgn files
import time
import os

event = raw_input("Event: ")
date = raw_input("(yyyy.mm.dd) Date: " )
roundd = raw_input("Round: ")
white = raw_input("White: ")
black = raw_input("Black: ")
result = raw_input("(Ex: 1-0, 1/2 if draw) Result : ")
white_elo = raw_input("(\"-\" for blank) White Elo: ")
black_elo = raw_input("(\"-\" for blank) Black Elo: ")

os.system('clear') 
time.sleep(1)

print("[Event ""\""+event+"\"]")
time.sleep(.3)
print("[Date ""\""+date+"]\"")
time.sleep(.3)
print("[Round ""\""+roundd+"\"]")
time.sleep(.3)
print("[White ""\""+white+"\"]")
time.sleep(.3)
print("[Black ""\""+black+"\"]")
time.sleep(.3)
print("[Result ""\""+result+"\"]")
time.sleep(.3)
print("[White Elo ""\""+white_elo+"\"]")
time.sleep(.3)
print("[Black Elo ""\""+black_elo+"\"]")
