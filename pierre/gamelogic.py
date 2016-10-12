#!/usr/bin/env python2

import random, os

def compareSequences(list1, list2):
	for i in range(0, len(list1)-1):
		if list1[i] != list2[i]:
			return False
	return True

limit = 3
points = 0

while True:
	usersequence = []
	sequence = []
	while len(sequence) < limit:
		sequence.append(random.randint(0,3))

	print("\nReplay sequence :")
	print(sequence)
	#for i in sequence:
		#os.system("beep -f "+str(i*200+400)+" -l 400 -D 100")

	while True:
		print("Your sequence :")
		print(usersequence)	
		if len(usersequence) < limit:
			usersequence.append(int(input()))
		else:
			if compareSequences(sequence, usersequence):
				points = points + 1
				break
			else:
				print("End "+str(points)+" points.")
				quit()
				
	limit = limit+1

