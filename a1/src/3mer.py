#!/usr/bin/env python

import sys

if (len(sys.argv) != 2):
	sys.exit();

fastaFile = sys.argv[1]
globalsequence = ''
sequence = ''
numOfKmers = 0
kmerDictionary = {}
aminoAcids = [ 'A', 'C', 'T', 'G']

# Initialize kmerDictionary to
for a in aminoAcids:
	for b in aminoAcids:
		for c in aminoAcids:
			kmerDictionary[a + b + c] = 0

# Given a sequence, update the kmerDictionary
def analyzeString():
	global numOfKmers
	global sequence

	# create a new sequence without any extra characters
	filteredSequence = ''
	for aa in sequence:
		if (aa.upper()in aminoAcids):
			filteredSequence += aa

	# if the sequence is valid (>0 amino acids)
	if (len(filteredSequence) > 0):
		# sequence has been stored, now get information
		kmerLength = 0
		kmerString = ''
		index = 0
		for c in filteredSequence:
			# Exit if near the end of sequence with no more 3-mers
			if (len(filteredSequence) - index < 3):
				break

			# Create 3-mer and add to dictionary
			for x in range(0,3):
				if (index + x == len(filteredSequence)):
					break
				aaOfInterest = filteredSequence[index + x]
				kmerLength += 1
				kmerString += aaOfInterest.upper()

			# if kmer is of length 3, add it to freq
			if (kmerLength == 3):
				kmerDictionary[kmerString] = kmerDictionary[kmerString] + 1
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

# Analyze final sequence in file
analyzeString()

for key, value in sorted(kmerDictionary.iteritems()):
	#print key + " %.4f" % (float(value)/float(numOfKmers))
	print key + " " + str(value)