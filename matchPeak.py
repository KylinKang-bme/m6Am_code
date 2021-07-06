import sys
import numpy
import queue as Q

# build a priority queue for annotated peaks
def hashOrder(file):

	RNA = {}

	f = open(file)

	while True:

		line = f.readline()

		if not line:
			break

		line = line.strip('\n').split("\t")

		key = line[0]

		# start and end postion
		pair = (int(line[1]), int(line[2]))
		# range and miRNA/gene name

		if key not in RNA:

			RNA[key] = Q.PriorityQueue()

		RNA[key].put((pair))


	for key in RNA.keys():

		record = []

		while not RNA[key].empty():

			record.append(RNA[key].get())

		RNA[key] = record

	return RNA


def matchPeak(file1, file2):

	# first
	exper = hashOrder(file1)
	# second
	refer = hashOrder(file2)
	com = set()

	f1 = open(file3, "w+")

	for indexs in exper.keys():

		if indexs in refer.keys():
			
			# first
			sample1 = exper[indexs]

			# second
			sample2 = refer[indexs]

			for one in sample1:

				for each in sample2:

				
					# if two peaks from two different samples overlap, they are considered as common peaks
					if not one[0] > each[1] and not each[0] > one[1]: 


						com.add( indexs + "\t" + str(one[0]) + "\t" + str(one[1]) + "\n")
						com.add( indexs  + "\t" + str(each[0]) + "\t" + str(each[1]) + "\n")

	for each in com:
		f1.write(each)


# peak from sample 1
file1 = sys.argv[1]
# peak from sample 2
file2 = sys.argv[2]
# output file for common peaks
file3 = sys.argv[3]

matchPeak(file1, file2, file3)
