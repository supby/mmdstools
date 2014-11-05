import numpy as np
import math


def calcLength(v):
	return math.sqrt(sum([vi**2 for vi in v]))
	
def calcCos(v1,v2):
	return np.dot(v1,v2)/(calcLength(v1)*calcLength(v2))
	
def applyAlpha(v, alpha):
	va = [vi for vi in v]
	va[-1] *= alpha
	return va

a = [1,0,1,0,1,2]
b = [1,1,0,0,1,6]
c = [0,1,0,1,0,2]

alphaVec = [0,0.5,1,2]



for alpha in alphaVec:
	
	aa = applyAlpha(a, alpha)
	ba = applyAlpha(b, alpha)
	ca = applyAlpha(c, alpha)	
	
	cosAB = calcCos(aa,ba)
	cosAC = calcCos(aa,ca)
	cosBC = calcCos(ba,ca)
	
	print 'Alpha: %s' % alpha
	print '1 - cosAB: %s' % (1 - cosAB)
	print '1 - cosAC: %s' % (1 - cosAC)
	print '1 - cosBC: %s' % (1 - cosBC)
	print "----------------------------------"
	