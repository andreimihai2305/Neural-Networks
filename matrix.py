import random
from sys import exit

class Matrix:

	def __init__(self, mat=[[]], dec=4):
		self._mat = self.set(mat)
		self.rows = len(mat)
		self.cols = len(mat[0]) if isinstance(mat[0], list) else 1
		self.dec = dec
		

	def __repr__(self):
		return f"Matrix({self.rows}, {self.cols});"



	def __len__ (self):
		return len(self._mat)

	def __getitem__(self, key):
		try:
			if isinstance(key, tuple):
				row, col = key
				if row >= self.rows or col >= self.cols:
					raise IndexError()

				return self._mat[row][col]

			else:
				row = key
				if row >= self.rows:
					raise IndexError()

				return self._mat[row]

		except IndexError:
			print(f"IndexError: Index out of range, Matrix size: ({self.rows}, {self.cols}) ")
			exit(1)

	def __setitem__(self, key, value):
		row, col = key
		
		try:
			if row >= self.rows or col >= self.cols:
				raise IndexError()

			self._mat[row][col] = value

		except IndexError:
			print(f"IndexError: Index out of range, Matrix size: ({self.rows}, {self.cols}) ")
			exit(1)


	def __add__(self, other):
		rows, cols = self.rows, self.cols
		try:
			if not isinstance(other, Matrix):
				raise TypeError

			if rows == other.rows and cols == other.cols:
				dec = self.dec if self.dec > other.dec else other.dec
				res = Matrix([[0 for j in range(cols)] for i in range(rows)])

				for i in range(rows):
					for j in range(cols):
						res[i, j] = round(self[i, j] + other[i, j], self.dec)

				return res 

			else: 
				raise TypeError

		except Exception as e:
			print(f"TypeError: {str(other)} can not be added to Matrix ({self.rows}, {self.cols})")
			print(e)
			exit(1)

	def __sub__(self, other):
		rows, cols = self.rows, self.cols
		try:
			if not isinstance(other, Matrix):
				raise TypeError

			if rows == other.rows and cols == other.cols:
				dec = self.dec if self.dec > other.dec else other.dec
				res = Matrix([[0 for j in range(cols)] for i in range(rows)])

				for i in range(rows):
					for j in range(cols):
						res[i, j] = round(self[i, j] - other[i, j], self.dec)

				return res 

			else: 
				raise TypeError

		except Exception as e:
			print(f"TypeError: {str(other)} can not be added to Matrix ({self.rows}, {self.cols})")
			print(e)
			exit(1)


	def __eq__(self, other):
		if not isinstance(other, Matrix):
			return False
		if self.cols != other.cols or self.rows != other.rows:
			return False

		for i in range(self.rows):
			for j in range(self.cols):
				if self[i,j] != other[i,j]:
					return False
		 
		return True


	def __mul__(self, other):
		try:
			# Scalar Multiplication
			if isinstance(other, int):
				dec = self.dec
				prod = Matrix([[0 for j in range(self.cols)] for i in range(self.rows)])
	
				for i in range(self.rows):
					for j in range(self.cols):
						prod[i,j] = self[i,j] * other
	
				return prod

			# Matrix Multiplication
			elif isinstance(other, Matrix):
				dec = self.dec if self.dec > other.dec else other.dec
				prod = self.zero(self.rows, other.cols)
				
				if (self.cols == other.rows):
					for i in range(self.rows):
						for j in range(other.cols):
							row_sum = 0
							for k in range(self.cols):
								row_sum += self[i,k] * other[k,j]

							prod[i,j] = row_sum
	
					return prod
					
				else:
					raise TypeError

			else:
				raise TypeError

		except TypeError as e:
			print(f"TypeError: {str(other)} can not be multiplied with Matrix ({self.rows}, {self.cols})")
			print(e)
			exit(1)

	def set(self, mat: list[list]):
		if not isinstance(mat, list):
			print(f"Invalid Matrix: {str(mat)}")
			exit(1)

		for i in range(len(mat)):
			if not isinstance(mat[i], list):
				print(f"Invalid Matrix: {str(mat)}")
				exit(1)


			if len(mat[i]) != len(mat[0]):
				print(f"Invalid Matrix: {str(mat)}")
				exit(1)
			

			for j in range(len(mat[i])):
				if not isinstance(mat[i][j], int) and not isinstance(mat[i][j], float):
					print(f"Invalid Matrix: {str(mat)}")
					exit(1)

		return mat


	@staticmethod
	def sub_mat(mat: tuple, rows: tuple, cols: tuple):
		try:
			if not isinstance(mat, Matrix):
				raise TypeError()

			if rows[1] > mat.rows:
				raise IndexError()

			if cols[1] > mat.cols:
				raise IndexError()

			return Matrix([[mat[i,j] for j in range(cols[0], cols[1])] for i in range(rows[0], rows[1])])


		except TypeError as e:
			print(f"TypeError: Cannot take submatrix of type {type(mat)}")
			print(e)

		except IndexError as e:
			print(f"IndexError: Cannot take Submatrix({rows}, {cols}) from Matrix({mat.rows}, {mat.cols})")
			print(e)


	# Default Matrix		
	@classmethod
	def zero(cls, rows: int, cols: int) -> list[list]:
		return cls([[0 for j in range(cols)] for i in range(rows)])


	# Random Matrix
	@classmethod	
	def rand(cls, rows, cols,low=0, high=1, dec=4):
		return cls([[round(random.uniform(low, high), dec) for j in range(cols)] for i in range(rows)], dec)

	
	def print_mat(self) -> None:
		print(f"Matrix({self.rows}, {self.cols})")
		print('[ ')
		for i in range(self.rows):
			for j in range(self.cols):
				print(f"{(self._mat[i][j]):10f},", end=' ')
			print()
		print('];')


		



if __name__ == "__main__":
	double = Matrix([
	[1, 2],
	[2, 4],
	[3, 6],
	[4, 8],
	[5, 10],
	[6, 12]
])
	mat2 = Matrix.sub_mat(double, (0, len(double)), (1, 2))
	print(mat2)
	mat2.print_mat()


	


