import numpy as np
from Plotter import Plotter

class OOPPlanet:
	def __init__(self, R, w, plotter): #initialize planet with basic parameters
		self.Radius = R #planet radius
		self.wplanet = w #planet angular velocity
		self.plotter = plotter #connection to some abstract plotter

	def getX(self, time):
		return self.Radius*np.cos(self.wplanet*time)

	def getY(self, time):
		return self.Radius*np.sin(self.wplanet*time)

	def position(self): #method creates planet orbit
		time=np.arange(0., 3.2, 0.02)
		xp = self.getX(time)
		yp = self.getY(time)
		plotter.plot(xp, yp, 'r') #after that we want to plot it, we use plotter's interface for this


class OOPMoon(OOPPlanet): #Moon inherits properties of Planet and adds some more
	def __init__(self, R, wp, r, wm, plotter):
		OOPPlanet.__init__(self, R, wp, plotter) #basic Planet is not initialized by default, we must do it by hand. 
		#At this point all attributes and methods from OOPPlanet now exist in OOPMoon
		self.radius = r #we add some more parameters
		self.wmoon = wm

	def position(self): #we override OOPPlanet's method by a new one
		time=np.arange(0., 3.2, 0.02)
		xp = self.getX(time)+self.radius*np.cos(self.wmoon*time)
		yp = self.getY(time)+self.radius*np.sin(self.wmoon*time)
		plotter.plot(xp, yp, 'b')

plotter = Plotter('Planet with moon', 'x', 'y')
# plotter.show()
moon = OOPMoon(4.0, 2.0, 1.0, 14.0, plotter)
moon.position()
planet = OOPPlanet(4.0, 2.0, plotter)
planet.position()

plotter.show()