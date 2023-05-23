import random
from matrix import Matrix


class Perceptron:
	def __init__(self, input_size: int, activation):
		self.weights = Matrix.rand(input_size, 1, 0, 5)
		self.bias = random.uniform(0, 10)
		self.activation = activation
		self.input_size = input_size


	def __repr__(self):
		return f"Perceptron: Weight = {self.weights._mat}, Bias = {self.bias}, Activation = {self.activation.__name__}"

	def feed_forward(self, sample):
		return self.activation((Matrix([sample]) * self.weights)[0, 0] + self.bias)


	def cost(self, x_data: Matrix, y_data: Matrix) -> float:
		
		if len(x_data) != len(y_data):
			print(f"X: {x_data} and y: {y_data} do not match")
			return

		res = 0	
		for i in range(len(x_data)):
			y_pred = self.feed_forward(x_data[i])

			cost = (y_pred - y_data[i, 0]) ** 4
			res += cost	

		return (res / len(x_data))


	def finite_diff(self, x_data: Matrix, y_data: Matrix, eps: float, lr: float) -> None:
		initial_cost = self.cost(x_data, y_data)
		dweights = Matrix.zero(self.input_size, 1)
		
		for i in range(self.input_size):
			saved_w = self.weights[i, 0] 
			self.weights[i, 0] += eps
			dweights[i, 0] = (self.cost(x_data, y_data) - initial_cost) / eps
			self.weights[i, 0] = saved_w


		saved_bias = self.bias
		self.bias += eps
		dbias = (self.cost(x_data, y_data) - initial_cost) / eps
		self.bias = saved_bias
		

		self.weights -= (dweights * lr)
		self.bias -= (dbias * lr)



