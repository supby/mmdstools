import numpy as np


def normalize(M):
	return M/float(M.max())

def computeStep(L,h):
	a = L.T*h
	a = normalize(a)
	h = L*a
	h = normalize(h)

	return h,a



if __name__ == '__main__':

	h = np.mat([1,1,1,1]).T
	L = np.mat([[0,1,1,0],[1,0,0,0],[0,0,0,1],[0,0,1,0]])

	h,a = computeStep(L,h)
	h,a = computeStep(L,h)

	print "Hobbies:"
	print h
	print "A:"
	print a


