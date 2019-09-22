#This is a python script that will make pgn files
import time
import os

os.system('clear')

event = input("Event: ")
date = input("(yyyy.mm.dd) Date: " )
roundd = input("Round: ")
white = input("White: ")
black = input("Black: ")
result = input("(Ex: 1-0, 1/2 if draw) Result : ")
white_elo = (input("(\"enter\" for blank) White Elo: ") or "-")
black_elo = (input("(\"enter\" for blank) Black Elo: ") or "-")

os.system('clear') 
time.sleep(1)

list = [ event, date, roundd, black, result, white_elo, black_elo]

def user_input(event, date, roundd, white, black, result, white_elo, black_elo):
	print("(1) [Event ""\""+event+"\"]")
	print("(2) [Date ""\""+date+"]\"")
	print("(3) [Round ""\""+roundd+"\"]")
	print("(4) [White ""\""+white+"\"]")
	print("(5) [Black ""\""+black+"\"]")
	print("(6) [Result ""\""+result+"\"]")
	print("(7) [White Elo ""\""+white_elo+"\"]")
	print("(8) [Black Elo ""\""+black_elo+"\"]")
	return 






x = 1
while(x == 1):
	user_input(event, date, roundd, white, black, result, white_elo, black_elo)
	print ("\n")
	answer = (input("Is everything above correct? (yes/no): ") or "yes")
	if answer.casefold() in ['y', 'yes']:
		x +=1

	elif answer.casefold() in ['n', 'no']:
		print ('lemme fix that')

	else:
		print ('Please enter a valid answer')
		time.sleep (2)
		os.system('clear')

print ('out of loop')

	




