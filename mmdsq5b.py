import numpy as np
import math


def calcDistance(p1, p2):
	return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
	
def calcClusterMeanPoint(points):
	length = len(points)
	return (float(sum([p[0] for p in points]))/length, float(sum([p[1] for p in points]))/length)

def assignPoints2Clusters(centriods, points):
	cluster2Points = {}
	for p in points:
		minD = -1
		closestC = None
		for c in centriods:
			curD = calcDistance(p, c)
			if minD == -1 or curD < minD:
				minD = curD
				closestC = c
		arr = cluster2Points.get(closestC, [])
		arr.append(p)
		cluster2Points[closestC] = arr

	return cluster2Points
	
if __name__ == '__main__':

	centriods = [(25,125), (44,105), (29,97), (35,63), (55,63), (42,57), (23,40), (64,37), (33,22), (55,20)]
	points = [(28,145),(65,140),(50,130),(38,115),(55,118),(50,90),(43,83),(63,88),(50,60),(50,30)]	

	# initial assign	
	cluster2Points = assignPoints2Clusters(centriods, points)
	print "0st assign (initial):"
	print cluster2Points

	# recalculate means for clusters	
	centriods = []
	for k,v in cluster2Points.items():
		meanPoint = calcClusterMeanPoint(v)
		centriods.append(meanPoint)

	# second assign	
	cluster2Points = assignPoints2Clusters(centriods, points)
	print "1st assign:"
	print cluster2Points	



	