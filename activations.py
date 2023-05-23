import math

def sigmoid(nr):
	return 1 / (1 + math.exp(-nr))


def relu(nr):
	return max(0.0, nr)


def tanh(nr):
	return (math.exp(2*nr) - 1) / (math.exp(2*nr) + 1)

def no_activation(nr):
	return nr

