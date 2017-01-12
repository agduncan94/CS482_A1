#!/usr/bin/env python

import sys

if (len(sys.argv) != 2):
	sys.exit();

fastaFile = sys.argv[1]
sequence = ''
sequenceCount = 0
sequenceLength = 0
numOfKmers = 0

with open(fastaFile, 'r') as file:
	for line in file:
		if (line.startswith(">")):
			# new sequence
			if (len(sequence) > 0):
				# sequence has been stored, now get information
				for (c in sequence):
					

			print "New Sequence " + str(sequenceCount)
			sequenceCount += 1
			sequence = ''
		elif (line.startswith(";")):
			# comment
			print "comment"
		elif (line.strip()):
			# non empty
			sequence += line.strip().rstrip("\r\n")

