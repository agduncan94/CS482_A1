#!/usr/bin/env python

import sys

if (len(sys.argv) != 2):
	sys.exit();

fastaFile = sys.argv[1]
sequence = ''
sequenceLength = 0
numOfKmers = 0
kmerDictionairy = {}


with open(fastaFile, 'r') as file:
	for line in file:
		if (line.startswith(">")):
			# new sequence
			if (len(sequence) > 0):
				# sequence has been stored, now get information
				kmerLength = 0
				kmerString = ''
				print sequence
				for c in sequence:
					if (c.upper() == 'A' or c.upper() == 'C' or c.upper() == 'T' or c.upper() == 'G'):
						kmerLength += 1
						kmerString += c.upper()

						# if kmer is of length 3, add it to freq
						if (kmerLength == 3):
							if (not kmerString in kmerDictionairy):
								kmerDictionairy[kmerString] = 1
							else:
								kmerDictionairy[kmerString] = kmerDictionairy[kmerString] + 1
							kmerString = ''
							kmerLength = 0
							numOfKmers += 1



			sequence = ''
		elif (line.startswith(";")):
			# comment
			print "comment"
		elif (line.strip()):
			# non empty
			sequence += line.strip().rstrip("\r\n")

for key, value in kmerDictionairy.iteritems():
	#print key + " %.4f" % (float(value)/float(numOfKmers))
	print key + " " + str(value)