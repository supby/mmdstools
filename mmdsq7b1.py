import numpy as np


def calcIteration(r,M,b,eS, S):
	return np.array(np.dot(M * b, r) + np.dot(eS, (1 - b))/float(len(S)))[0]

if __name__ == '__main__':

	S = [1,2]
	eS = [1,1,0,0]
	lenS = len(S)

	M = np.mat([[0,1,0,0],[0.5,0,0,0],[0.5,0,0,1],[0,0,1,0]])
	b = 0.7	

	r0 = [0.25,0.25,0.25,0.25]

	for c in range(200):
		print r0
		r0 = calcIteration(r0, M, b, eS, S)

	# bM = np.dot(M, b)
	# mShape = np.shape(M)

	# A = np.zeros(shape=mShape)
	# for i in range(mShape[0]):
	# 	for j in range(mShape[1]):
	# 		A[i,j] = b*M[i,j] + ((1 - b)/float(lenS) if (i+1) in S else 0)

	

	# for c in range(20):
	# 	print r0
	# 	rNext = np.dot(A, r0)
	# 	r0 = rNext

	# 	# r0 = [int(ri*1000)/float(1000) for ri in r0]







