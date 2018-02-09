import numpy as np
import matplotlib.pyplot as plt

class Plotter:
	def __init__(self):
		self.fig = plt.figure()
		self.ax = self.fig.add_subplot(111)

class OOPPlanet:
	def __init__(self, R, w, plotter):
		self.Radius = R
		self.wplanet = w
		self.plotter = plotter

	def getX(self, time):
		return self.Radius*np.cos(self.wplanet*time)

	def getY(self, time):
		return self.Radius*np.sin(self.wplanet*time)

	def position(self):
		time=np.arange(0., 3.2, 0.02)
		xp = self.getX(time)
		yp = self.getY(time)
		plotter.ax.plot(xp, yp, 'r')


class OOPMoon(OOPPlanet):
	def __init__(self, R, wp, r, wm, plotter):
		OOPPlanet.__init__(self, R, wp, plotter)
		self.radius = r
		self.wmoon = wm

	def position(self):
		time=np.arange(0., 3.2, 0.02)
		xp = self.getX(time)+self.radius*np.cos(self.wmoon*time)
		yp = self.getY(time)+self.radius*np.sin(self.wmoon*time)
		plotter.ax.plot(xp, yp, 'b')

plotter = Plotter()
moon = OOPMoon(4.0, 2.0, 1.0, 14.0, plotter)
moon.position()
planet = OOPPlanet(4.0, 2.0, plotter)
planet.position()

plt.show()