#!/usr/bin/python

import commands
 
w='''
 press 1 for opening firefox 

 press 2 for executing a command 

 press 3 for opening a new terminal window 

'''

print w

x=input('enter a no.:')

if x == 1 : 
	commands.getoutput('firefox')
elif x == 2 :

	
        y=raw_input('enter a command:')
	print commands.getoutput(y)

elif x == 3:
	commands.getoutput('gnome-terminal')

else:
	print "wrong entry!!!"

	

	


	
