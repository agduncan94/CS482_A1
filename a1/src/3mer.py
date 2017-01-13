#!/usr/bin/env python

import sys

if (len(sys.argv) != 2):
	sys.exit();

fastaFile = sys.argv[1]
globalsequence = ''
sequence = ''
numOfKmers = 0
kmerDictionairy = {}
aminoAcids = [ 'A', 'C', 'T', 'G']

for a in aminoAcids:
	for b in aminoAcids:
		for c in aminoAcids:
			kmerDictionairy[a + b + c] = 0

def analyzeString():
	global numOfKmers
	global sequence
	if (len(sequence) > 0):
		# sequence has been stored, now get information
		kmerLength = 0
		kmerString = ''
		index = 0
		for c in sequence:
			if (len(sequence) - index < 3):
				break
			for x in range(0,3):
				if (index + x == len(sequence)):
					break
				aaOfInterest = sequence[index + x]
				if (aaOfInterest.upper()in aminoAcids):
					kmerLength += 1
					kmerString += aaOfInterest.upper()

					# if kmer is of length 3, add it to freq
					if (kmerLength == 3):
						kmerDictionairy[kmerString] = kmerDictionairy[kmerString] + 1
						kmerString = ''
						kmerLength = 0
						numOfKmers += 1
			index += 1
		sequence = ''

with open(fastaFile, 'r') as file:
	for line in file:
		if (line.startswith(">")):
			# new sequence
			analyzeString()
		elif (line.startswith(";")):
			# comment
			print "comment"
		elif (line.strip()):
			# non empty
			sequence += line.strip().rstrip("\r\n")

analyzeString()

for key, value in sorted(kmerDictionairy.iteritems()):
	#print key + " %.4f" % (float(value)/float(numOfKmers))
	print key + " " + str(value)