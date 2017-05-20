#!/usr/bin/python3

from helper_func import *
import matplotlib.pyplot as plt
import random
import argparse
import itertools
import sys

def main():
	p = argparse.ArgumentParser()
	p.add_argument("numsides", type=int)
	p.add_argument("numpoints", type=int)
	args = p.parse_args()

	if args.numsides > args.numpoints:
		print("The number of sides is greater than the number of points!")
		sys.exit(1)
	
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

if __name__ == "__main__":
	main()
