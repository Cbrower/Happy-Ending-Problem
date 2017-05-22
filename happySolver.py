#!/usr/bin/python3

from helper_func import *
import itertools
import random
import argparse
import time
import sys

ACCURACY = 10

def main():
	global ACCURACY
	p = argparse.ArgumentParser()
	p.add_argument("numsides", type=int)

	args = p.parse_args()

	numPoints = args.numsides
	flag = False
	while not flag:
		flag = testSides(args.numsides, numPoints)
		numPoints += 1
	print("G({}) = {}".format(args.numsides, numPoints - 1))

def testSides(numSides, numPoints):
	pts = []
	c = 0
	print("{}".format(numPoints))
	for i in range(0, numPoints):
		pts.append([])
		pts[i].append(0)
		pts[i].append(0)
	while updateAllPoints(pts):
		if not areAnyPointsSame(pts) and not collinearityTest(pts):
			flag, poly = findConvex(pts, numSides)
			if not flag:
				printPoints(pts)
				time.sleep(1)
				return False
		if c % 1000000 == 0:
			print()
			printPoints(pts)
			print()
		c += 1
	return True

def updatePoint(pt):
	global ACCURACY
	if pt[0] >= ACCURACY:
		if pt[1] >= ACCURACY:
			pt[0] = 0
			pt[1] = 0
			return False
		else:
			pt[0] = 0
			pt[1] += 1
	else:
		pt[0] += 1
	return True

def updateAllPoints(pts):
	for pt in pts:
		if updatePoint(pt):
			return True
	return False

if __name__ == "__main__":
	main()
