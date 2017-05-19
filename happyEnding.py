import matplotlib.pyplot as plt
import random
import argparse
import itertools

def main():
	p = argparse.ArgumentParser()
	p.add_argument("numsides", type=int)
	p.add_argument("numpoints", type=int)
	args = p.parse_args()
	
	collinear = True
	while collinear:
		pts = []
		c = 0
		while c < args.numpoints:
			pts.append((random.uniform(0, 10), random.uniform(0, 10)))
			collinear = collinearityTest(pts)
			c += 1

	for i in pts:
		plt.plot(i[0], i[1], 'ro')
		print("({}, {})".format(i[0], i[1]))

	flag, poly = findConvex(pts, args.numsides)
	polyx = []
	polyy = []
	if flag:
		for n in poly:
			polyx.append(n[0])
			polyy.append(n[1])
		polyx.append(poly[0][0])
		polyy.append(poly[0][1])
		plt.plot(polyx, polyy)

	plt.ylabel('Some Numbers')
	plt.axis([0, 10, 0, 10])
	plt.show()

def genLineSegs(pts):
	lns = []
	length = len(pts)
	
	for i in range(0, length):
		lns.append((pts[i][0], pts[i][1], pts[(i + 1) % length][0], pts[(i + 1) % length][1]))
	return lns

def doEndPointsIntersect(ln1, ln2):
	if ln1[0] == ln2[0] and ln1[1] == ln2[1]:
		return True
	elif ln1[0] == ln2[2] and ln1[1] == ln2[3]:
		return True
	elif ln1[2] == ln2[0] and ln1[3] == ln2[1]:
		return True
	elif ln1[2] == ln2[2] and ln1[3] == ln2[3]:
		return True
	return False

def hasIntersection(ln1, ln2):
	if doEndPointsIntersect(ln1, ln2):
		return False
	i1 = [min(ln1[0], ln1[2]), max(ln1[0], ln1[2])]
	i2 = [min(ln2[0], ln2[2]), max(ln2[0], ln2[2])]
	ia = [max(i1[0], i2[0]), min(i1[1], i2[1])]
	if (max(ln1[0], ln1[2]) < min(ln2[0], ln2[2])):
		return False
	m1 = (ln1[3] - ln1[1]) * 1. / (ln1[2] - ln1[0]) * 1.
	m2 = (ln2[3] - ln2[1]) * 1. / (ln2[2] - ln2[0]) * 1.
	if m1 == m2:
		return False
	b1 = ln1[1] - m1 * ln1[0]
	b2 = ln2[1] - m2 * ln2[0]
	x1 = (b2 - b1) / (m1 - m2)
	if (x1 < max(i1[0], i2[0])) or (x1 > min(i1[1], i2[1])):
		return False
	return True

def isComplex(lns):
	for lines in itertools.permutations(lns, 2):
		if hasIntersection(lines[0], lines[1]):
			return True
	return False

def isConvex(pts):
	sides = len(pts)
	if sides < 4:
		return True
	sign = False
	c = 0
	while c < sides:
		dx1 = pts[(c + 2) % sides][0] - pts[(c + 1) % sides][0]
		dy1 = pts[(c + 2) % sides][1] - pts[(c + 1) % sides][1]
		dx2 = pts[c][0] - pts[(c + 1) % sides][0]
		dy2 = pts[c][1] - pts[(c + 1) % sides][1]
		zcrossproduct = dx1*dy2 - dy1*dx2

		if c == 0:
			sign = zcrossproduct >= 0
		elif sign != (zcrossproduct >= 0):
			return False
		c += 1
	return True

def findConvex(pts, n):
	for points in itertools.permutations(pts, n):
		if(isConvex(points) and not isComplex(genLineSegs(points))):
			print("Found Shape")
			return True, points
	return False, pts

def areCollinear(p0, p1, p2):
	s1 = (p1[1] - p0[1]) / (p1[0] - p0[0])
	s2 = (p2[1] - p1[1]) / (p2[0] - p1[0])
	return s1 == s2

def collinearityTest(pts):
	for points in itertools.combinations(pts, 3):
		if(areCollinear(points[0], points[1], points[2])):
			return True
	return False

def is_int(s):
	try:
		out = int(s)
		return True
	except ValueError:
		return False

if __name__ == "__main__":
	main()
