#!/usr/bin/python3
from helper_func import *
import matplotlib.pyplot as plt
import random
import argparse
import sys

def main():
	p = argparse.ArgumentParser()
	p.add_argument("numsides", type=int)
	p.add_argument("numpoints", type=int)
	p.add_argument("numiterations", type=int)

	args = p.parse_args()

	if args.numsides > args.numpoints:
		print("The number of sides is greater than the number of points!")
		sys.exit(1)

	counter = 0
	for i in range(0, args.numiterations):
		collinear = True
		while collinear:
			pts = []
			c = 0
			while c < args.numpoints:
				pts.append((random.uniform(0, 10), random.uniform(0, 10)))
				collinear = collinearityTest(pts)
				c += 1
		flag, poly = findConvex(pts, args.numsides)
		polyx = []
		polyy = []
		if flag:
			counter += 1
	print("Number of iterations: {}".format(args.numiterations))
	print("Number of polygons found: {}".format(counter))

if __name__ == "__main__":
	main()

