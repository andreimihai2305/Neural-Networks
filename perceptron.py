import random
from activations import relu
from matrix import Matrix


class Perceptron:
	def __init__(self, activation=None):
		self.weight = random.uniform(0, 1)
		self.bias = random.uniform(0, 1)
		self.activation = activation

	def __repr__(self):
		if self.activation:
			return f"Perceptron: Weight = {self.weight}, Bias = {self.bias}, Activation = {self.activation.__name__}"

		else:
			return f"Perceptron: Weight = {self.weight}, Bias = {self.bias}"


	def cost(self, data: Matrix) -> float:
		res = 0
		for i in range(len(data)):
			activation = self.activation(self.weight * data[i, 0] + self.bias)
			cost = round((activation - data[i, 1]) ** 2, 8)
			res += cost	

		return (res / len(data))


	def finite_diff(self, data, eps, lr):
		initial_cost = self.cost(data)
		
		save_weight = self.weight
		save_bias = self.bias

		self.weight += eps
		dweight = self.cost(data) - initial_cost
		self.weight -= eps

		self.bias += eps
		dbias = self.cost(data) - initial_cost
		self.bias -= eps

		self.weight -= dweight * lr
		self.bias -= dbias * lr




if __name__ == "__main__":
	p = Perceptron(relu)
	double = Matrix([
	[1, 2],
	[2, 4],
	[3, 6],
	[4, 8],
	[5, 10],
	[6, 12]
])


	print(p.cost(double))
	for i in range(100):
		p.finite_diff(double, 1e-2, 1e-1)


	print(p.cost(double))
	
