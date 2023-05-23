import random
from activations import relu
from matrix import Matrix

# random.seed(42)
class Perceptron:
	def __init__(self, input_size: int, activation):
		self.weights = Matrix.rand(input_size, 1)
		self.bias = random.uniform(0, 5)
		self.activation = activation
		self.input_size = input_size


	def __repr__(self):
		return f"Perceptron: Weight = {self.weight}, Bias = {self.bias}, Activation = {self.activation.__name__}"

	def feed_forward(self, sample):
		return self.activation((self.weights * Matrix([sample]))[0, 0] + self.bias)


	def cost(self, x_data: Matrix, y_data: Matrix) -> float:
		
		if len(x_data) != len(y_data):
			print(f"X: {x_data} and y: {y_data} do not match")
			return

		res = 0	
		for i in range(len(x_data)):
			y_pred = self.feed_forward(x_data[i])

			cost = (y_pred - y_data[i, 0]) ** 2
			res += cost	

		return (res / len(x_data))


	def finite_diff(self, x_data: Matrix, y_data: Matrix, eps: float, lr: float) -> None:
		initial_cost = self.cost(x_data, y_data)
		dweights = Matrix.zero(self.input_size, 1)
		
		for i in range(self.input_size):

			self.weights[i, 0] += eps
			dweights[i, 0] = (self.cost(x_data, y_data) - initial_cost) / eps
			self.weights[i, 0] -= eps 
			

		
		self.bias += eps
		dbias = (self.cost(x_data, y_data) - initial_cost) / eps
		self.bias -= eps
		

		self.weights -= dweights * lr
		self.bias -= dbias * lr



