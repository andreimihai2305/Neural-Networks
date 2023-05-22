import math

def sigmoid(nr):
	return round(1 / (1 + math.exp(-nr)), 8)


def relu(nr):
	return max(0.0, nr)



def no_activation(nr):
	return nr