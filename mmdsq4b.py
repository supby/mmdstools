import numpy as np
import math

v0 = [2/7,3/7,6/7]

m1 = [[2/7,0.312],[3/7,0.156],[6/7,-0.937]]
m2 = [[2/7,0.429],[3/7,0.857],[6/7,0.286]]
m3 = [[2/7,0.702],[3/7,-0.702],[6/7,0.117]]
m4 = [[2/7,2.250],[3/7,-0.500],[6/7,-0.750]]

print "det(m1) = %s" % np.linalg.det(np.dot(m1, np.transpose(m1)))
print "det(m2) = %s" % np.linalg.det(np.dot(m2, np.transpose(m2)))
print "det(m3) = %s" % np.linalg.det(np.dot(m3, np.transpose(m3)))
print "det(m4) = %s" % np.linalg.det(np.dot(m4, np.transpose(m4)))


pm = 	[[1,1],
		 [2,2],
		 [3,4]]

w, v = np.linalg.eigh(np.dot(pm, np.transpose(pm)))

print v


