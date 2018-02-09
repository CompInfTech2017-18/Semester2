import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

Radius = 4.0 # Planet Orbit radius
wplanet = 2.0 # planet angular velocity
radius = 1.0 # moon Orbit radius around planet
wmoon = 14.0 # moon angular velocity

x = []
y = []
time=np.arange(0., 3.2, 0.02)
x = Radius*np.cos(wplanet*time)+radius*np.cos(wmoon*time)
y = Radius*np.sin(wplanet*time)+radius*np.sin(wmoon*time)
ax.plot(x,y)

plt.show()