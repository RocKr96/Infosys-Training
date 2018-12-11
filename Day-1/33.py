'''
Assignment 33: Lists – Hands - on - Practice

developer:Aman Zadafiya
date & time: 11/12/2018 12:35 PM
'''
currancy=[4,3,2,5,6,4,7,8]
for i in range(0,len(currancy)):
	for j in range(0,len(currancy)-1):
		if(currancy[j]<currancy[j+1]):
			currancy[j],currancy[j+1]=currancy[j+1],currancy[j]
print(currancy)