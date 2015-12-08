from datetime import datetime, time
from time import sleep

def act(x):
	print("wirth")
	return x+10

def wait_start(runTime):
	startTime = time(*(map(int, runTime.split(':'))))
	while startTime != datetime.today().time(): # you can add here any additional variable to break loop if necessary
		sleep(1)# you can change 1 sec interval to any other
	return 0
wait_start('02:35')
print("Maaaaaaaaaaaaaaaaal")
