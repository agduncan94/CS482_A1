#!/usr/bin/env python

import sys

if (len(sys.argv) != 2):
	sys.exit();

fastaFile = sys.argv[1]
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

	# if the sequence is valid (>0 amino acids)
	if (len(sequence) > 0):
		# sequence has been stored, now get information
		kmerString = ''
		index = 0

		for c in sequence:
			# Exit if near the end of sequence with no more 3-mers
			if (len(sequence) - index < 3):
				break

			# Create 3-mer string
			for offset in range(0,3):
				# is this necessary?
				# if (index + offset == len(sequence)):
				# 	break
				aaOfInterest = sequence[index + offset]
				kmerString += aaOfInterest.upper()

			# check that kmer doesn't have non-ACTG in it
			toAdd = True
			for char in kmerString:
				if (not char.upper() in aminoAcids):
					toAdd = False

			# only add if 3mer is composed of A, C, T, or G
			if (toAdd) :
				kmerDictionary[kmerString] = kmerDictionary[kmerString] + 1
				numOfKmers += 1
			kmerString = ''
			index += 1
		sequence = ''

# open file
with open(fastaFile, 'r') as file:
	for line in file:
		if (line.startswith(">")):
			# new sequence
			analyzeString()
		elif (line.startswith(";")):
			# comment
			# need to find a better way to deal
			# perhaps just put in the elif below if line.strip()
			print "comment"
		elif (line.strip()):
			# non empty
			sequence += line.strip().rstrip("\r\n")

# Analyze final sequence in file
analyzeString()

for key, value in sorted(kmerDictionary.iteritems()):
	print key + " %.4f" % (float(value)/float(numOfKmers))
	#print key + " " + str(value)