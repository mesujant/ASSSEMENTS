from matplotlib import pyplot as plt
import math
from random import uniform
class RCDischargingCircuit:
	def __init__(self, q0 , plot_type, R , C):
		if plot_type == "current":
			self.expression = self.current_discharging
		else:
			self.expression = sel.voltage_discharging
		self.x_axis = [0]
		self.y_axis = [q0]
		self.R = R
		self.C = C

	def current_discharging(self , t , q):
		return (q*math.exp(-t/(self.R * self.C))) 
	
	def voltage_discharging(t , V):
		pass


	def RK_2(self):
		h = 1
		y = 12
		x_axis = [0]
		y_axis = [12]
		for t in range(1, 100, h):
			k1 = self.expression(t , y)
			k2 = self.expression(t+h, y+k1)
			y = y + (k1 + k2)/2
			self.x_axis.append(t)
			self.y_axis.append(y)

		

	def plot(self):
		fig, ax = plt.subplots()
		ax.plot(self.x_axis, self.y_axis)

		ax.set(xlabel='time (s)', ylabel='current ',
	       title='RC discharing Current characterstics')
		ax.grid()

		fig.savefig("RCdischarging.png")
		plt.show()



class MonteCarloSimulation:
	def __init__(self):
		pass

	def generate_value_of_pi(self):
		circle_points = 0
		total_points = 0
		while True:
			x = uniform(-1, 1)
			y = uniform(-1, 1)
			total_points += 1
			if x*x + y*y <= 1:
				circle_points += 1
			pi = 4*(circle_points/total_points)
			print(pi)


class LinearCongrurentialGenerator:
	def __init__(self ):
 		pass

	def linear_congurent_model(self, seed, a, c, m):
		while True:
			seed = (a*seed + c) % m
			yield seed


class FindDistributionMatrix:
	def __init__(self):
		pass

	def identity_matrix(self, matrix):
		if len(matrix) == 1:
			return [[1]]
		elif len(matrix) == 2:
			return [[1,0], [0,1]]
		elif len(matrix) == 3:
			return [[1,0,0], [0,1,0], [0,0,1]]
		elif len(matrix) == 4:
			return[[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]]
		else:
			raise "size of matrix need to be considered:"


	def find_distribution_matrix(self, t_matrix , n , d_matrix):
		result = self.identity_matrix(t_matrix)
		for i in range(n):
			result = self.matrix_multiplication(result , t_matrix)
		return(self.matrix_multiplication(d_matrix, result))

	def matrix_multiplication(self, matrix_1, matrix_2):
		col = len(matrix_2[0])
		row = len(matrix_1)
		if len(matrix_1[0]) != len(matrix_2):
			print("no multiplication possible")
			return
		result = [0 for i in range(row) for j in range(col)]
		result = [result[i:i+col] for i in range(0, len(result), col)]
		for i in range(row):
			for j in range(col):
				for k in range(row):
					result[i][j] += matrix_1[i][k]*matrix_2[k][j]
			
		return result


if __name__ == "__main__":
	rc = RCDischargingCircuit(12, "current", 100, 0.1)
	rc.RK_2()
	rc.plot()

	lcg = LinearCongrurentialGenerator()
	i = 0
	limit = 50
	for random_no in lcg.linear_congurent_model(27, 17, 43, 100):
		if i == limit:
			break
		print(random_no)
		i += 1

	dm = FindDistributionMatrix()
	t_matrix = [[0.3, 0.3, 0.4],[0.5, 0.2, 0.3], [0.5, 0.4, 0.1]]
	d_matrix = [[1, 0, 0]]
	n = 4
	print(dm.find_distribution_matrix(t_matrix, n, d_matrix))

	pi = MonteCarloSimulation()
	for i in range(50):
		pi.generate_value_of_pi()

