import matplotlib.pyplot as plt

class Plotter: 
	'''Plotter fives some instruments for plotting. It has interfaces 'plot' and 'show'. Outside objects stay unaware of internal structure of Plotter'''
	def __init__(self, title, xlabel, ylabel): #initialize a canvas to plot on
		self.fig = plt.figure()
		self.ax = self.fig.add_subplot(111)
		self.ax.set_title(title) #we make some preparations
		self.ax.set_xlabel(xlabel)
		self.ax.set_ylabel(ylabel)

	def plot(self, x, y, color): #Plotter interface, to plot we use this method
		return self.ax.plot(x, y, color)

	def show(self):
		plt.show()
