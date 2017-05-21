#!/usr/bin/python3

from helper_func import *
import itertools
import random
import argparse
import sys

ACCURACY = 1000

def main():
	global ACCURACY
	p = argparse.ArgumentParser()
	p.add_argument("numsides", type=int)

	args = p.parse_args()

	numPoints = args.numsides
	flag = False
	while not flag:
		flag = testSides(args.numsides, numPoints)
	print("G({}) = {}".format(args.numsides, numPoints))

def testSides(numSides, numPoints):
	pts = []
	#iterate through every point possible somehow
		if collinearityTest(pts):
			continue
		flag, poly = findConvex(pts, numSides)
		if not flag:
			return False
	return True
