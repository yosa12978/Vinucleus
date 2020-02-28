import numpy as np
from kernel.neuron import Neuron  
import os
import time

clear = lambda: os.system("cls")
clear()

field = ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," ", " ", "|\n",]
def draw():
	print("~"*50)
	for i in field:
		print(i, end = "")
	print("~"*50)

def main():
	draw()
	time.sleep(0.1)
	bias = 4

	w1 = 2 * np.random.random((2,)) - 1
	w2 = 2 * np.random.random((2,)) - 1

	n1 = Neuron(w1, bias)
	n2 = Neuron(w2, bias)

	x = np.array([1, 0])
	if n1.feedforward(x) > n2.feedforward(x):
		for i in range(len(field)-1):
			if field[i] == "*":
				if i-1 == 0:
					break
				else:
					field[i] = " "
					field[i-1] = "*"
					break
	elif n1.feedforward(x) < n2.feedforward(x):
		for i in range(len(field)-1):
			if field[i] == "*":
				if i+1 == 49:
					break
				else:
					field[i] = " "
					field[i+1] = "*"
					break
	clear()

if __name__ == "__main__":
	while True:
		try:
			main()
		except:
			print("I am tired (((")