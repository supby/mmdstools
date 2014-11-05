import numpy as np
import math


def calcDistance(p1, p2):
	return math.sqrt(sum((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2))
	
def calcClusterMeanPoint(points):
	length = len(points)
	return (sum([p[0] for p in points])/length, sum([p[1] for p in points])/length)
	
if __name__ = '__main__':
	