import math

def calcDistance(p1, p2):
	return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

if __name__ == '__main__':
	selected = [(0,0),(10,10)]
	notSelected = [(1,6), (3,7), (4,3), (7,7), (8,2), (9,5)]


	length = len(notSelected) + len(selected)
	while len(notSelected) > 0:		
		maxD = -1
		maxP = None
		for p in notSelected:
			curD = min([calcDistance(p, sp) for sp in selected])
			if curD > maxD:
				maxD = curD
				maxP = p
		selected.append(maxP)
		notSelected.remove(maxP)

	print selected



