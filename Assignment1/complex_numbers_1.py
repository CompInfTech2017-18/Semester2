from __future__ import print_function
from sys import version


if int(version[0])>2:
	# raw_input deprecated in Python 3
	raw_input=input

class Complex:
	def __init__(self, x, y): # class constructor
		self.re = x # assign real part
		self.im = y # assign imag part

	def addt(self, other): # adds self to other
		return Complex(self.re + other.re, self.im + other.im)

	def subt(self, other): # subtract self-other
		return Complex(self.re - other.re, self.im- other.im)

	def mult(self, other): # multiplies self * other
		return Complex(self.re*other.re -self.im*other.im,
						self.re*other.im+self.im*other.re)

	def __repr__ (self): # convert z to string for print
		return '(%f, %f)' %(self.re, self.im)

print('Operation with two complex numbers \n')
z1 = Complex(2.0, 3.0)
print('z1 =', z1)
z2 = Complex(4.0, 6.0)
print("z2 =",z2)
z3 = Complex.addt(z1,z2)
print("z1 + z2= ",z3)
print('z1 - z2 =', Complex.subt(z1,z2))
print('z1 * z2 =', Complex.mult(z1,z2))
