#This is a python script that will make pgn files
import time
import os
import sys
from pathlib import Path


os.system('clear')

#tags_given = 8

# Define Save Path
directory = '~/Documents/Chess Games'
print ('Save Path: ' + directory)
print ("")

# User input for tags
event = input("Event: ")
date = input("Date (yyyy.mm.dd) : " )
roundd = (input("Round: ") or "1")
white = input("White: ")
black = input("Black: ")
result = input("Result (1-0, 0-1, 1/2 if draw): ")
white_elo = (input("WhiteElo: ") or "-")
black_elo = (input("BlackElo: ") or "-")

os.system('clear') 
time.sleep(1)

#Vlist = [event, date, roundd, white, black, result, white_elo, black_elo]
#list = [ "Event", "Date", "Round", "White", "Black", "Result", "White Elo", "Black Elo"]



def user_input(event, date, roundd, white, black, result, white_elo, black_elo, directory):
	print("(1) [Event ""\""+event+"\"]")
	print("(2) [Date ""\""+date+"]\"")
	print("(3) [Round ""\""+roundd+"\"]")
	print("(4) [White ""\""+white+"\"]")
	print("(5) [Black ""\""+black+"\"]")
	print("(6) [Result ""\""+result+"\"]")
	print("(7) [WhiteElo ""\""+white_elo+"\"]")
	print("(8) [BlackElo ""\""+black_elo+"\"]")
	print("(9) Save Path " + directory)
	return 



#tags = user_input(event, date, roundd, white, black, result, white_elo, black_elo)


x = 1
while(x == 1):
	user_input(event, date, roundd, white, black, result, white_elo, black_elo, directory)
	print ("")
	answer = (input("Is everything above correct? (yes/no): ") or "yes")
	if answer.casefold() in ['y', 'yes']:
		x +=1

	elif answer.casefold() in ['n', 'no']:
		x = 1
		while(x == 1):
			os.system('clear')
			user_input(event, date, roundd, white, black, result, white_elo, black_elo,directory)
			print('\n(0) to continue')
			selection = int(input('\nWhich tag would you like to fix?: ' ) or 0)
			"""
			if selection >=1 and selection <=8:
				print ('\n('+ str(selection) + ') ' + '[' + str(list[selection - 1]) + '] ' +  '\"' + Vlist[selection-1] + '\"')
				variable_change = input('\nPlease enter new value: ')
				Vlist[selection - 1] = variable_change 
				print (Vlist[selection - 1])
				time.sleep (2)
				"""
			if selection == 1:
				print ('\n('+ str(selection) + ') ' + '[' + str(list[selection - 1]) + '] ' +  '\"' + event + '\"')
				variable_change = input('\nPlease enter new value: ')
				event = variable_change
				print ("Event set to " '\"' + event + '\"')
				time.sleep(2)

			elif selection == 2:
				print ('\n('+ str(selection) + ') ' + '[' + str(list[selection - 1]) + '] ' +  '\"' + date + '\"')
				variable_change = input('\nPlease enter new value: ')
				date = variable_change
				print ("Date set to " '\"' + date + '\"')
				time.sleep(2)

			elif selection == 3:
				print ('\n('+ str(selection) + ') ' + '[' + str(list[selection - 1]) + '] ' +  '\"' + roundd + '\"')
				variable_change = input('\nPlease enter new value: ')
				roundd = variable_change
				print ("Round set to " '\"' + roundd + '\"')
				time.sleep(2)

			elif selection == 4:
				print ('\n('+ str(selection) + ') ' + '[' + str(list[selection - 1]) + '] ' +  '\"' + white + '\"')
				variable_change = input('\nPlease enter new value: ')
				white = variable_change
				print ("White set to " '\"' + white + '\"')
				time.sleep(2)

			elif selection == 5:
				print ('\n('+ str(selection) + ') ' + '[' + str(list[selection - 1]) + '] ' +  '\"' + black + '\"')
				variable_change = input('\nPlease enter new value: ')
				black = variable_change
				print ("Black set to " '\"' + black + '\"')
				time.sleep(2)

			elif selection == 6:
				print ('\n('+ str(selection) + ') ' + '[' + str(list[selection - 1]) + '] ' +  '\"' + result + '\"')
				variable_change = input('\nPlease enter new value: ')
				result = variable_change
				print ("Result set to " '\"' + result + '\"')
				time.sleep(2)

			elif selection == 7:
				print ('\n('+ str(selection) + ') ' + '[' + str(list[selection - 1]) + '] ' +  '\"' + white_elo + '\"')
				variable_change = input('\nPlease enter new value: ')
				white_elo = variable_change
				print ("WhiteElo set to " '\"' + white_elo + '\"')
				time.sleep(2)

			elif selection == 8:
				print ('\n('+ str(selection) + ') ' + '[' + str(list[selection - 1]) + '] ' +  '\"' + black_elo + '\"')
				variable_change = input('\nPlease enter new value: ')
				black_elo = variable_change
				print ("BlackElo set to " '\"' + black_elo + '\"')
				time.sleep(2)

			elif selection == 9:
				print ('Save Path: ' + directory)
				variable_change = input('\nPlease enter a new path: ')
				directory = variable_change
				print ("Save Path set to " + directory)
				time.sleep(2)

				

			elif selection == 0:
				x += 1



	else:
		print ('Please enter a valid answer')
		time.sleep (2)
		os.system('clear')


#a = [event, date, roundd, white, black, result, white_elo, black_elo]
#b = ['Event', 'Date', 'Round', 'White', 'Black', 'Result', 'White Elo', 'Black Elo']


time.sleep (1)
if os.path.isdir(os.path.expanduser(directory)) == True:
	print("")
	print(directory + " exists, making PGN file")
	time.sleep(2)
else:
	print("")
	print(directory + " does not exist, making directory")
	time.sleep(2)
	save_path = Path(os.path.expanduser(directory))
	save_path.mkdir(parents= True, exist_ok=True)



name_of_file = (white + ' v ' + black)
completeName = os.path.join (os.path.expanduser(directory), name_of_file + ".pgn")
print("")
print("Creating PGN file")
time.sleep(2)
f = open(completeName, "w+")
f.write('[Event '  + '\"' + event + '\"]')
f.write('\n[Date '  + '\"' + date + '\"]')
f.write('\n[Round '  + '\"' + roundd + '\"]')
f.write('\n[White '  + '\"' + white + '\"]')
f.write('\n[Black '  + '\"' + black + '\"]')
f.write('\n[Result '  + '\"' + result + '\"]')
f.write('\n[WhiteElo '  + '\"' + white_elo + '\"]')
f.write('\n[BlackElo '  + '\"' + black_elo + '\"]')
f.close()

print("")
print ('\"' + name_of_file + '\"' +  ' saved to ' + directory)


	




