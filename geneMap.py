import sys
import numpy
import queue as Q

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

def omg(file):

	# gene = set()

	RNA = {}

	f = open(file)

	while True:

		line = f.readline()

		if not line:
			break

		line = line.strip('\n').split("\t")

		# if line[2] == 'gene':

		key = line[0]

		# print(line[8])


		# pid = line[8].split(";")[4].split(" ")[2]
		# pid = pid[1: len(pid)-1]

		# gene.add(pid)

		# name = line[8].split(";")[1].split(" ")[2]
		# name = name[1:len(name)-1]

		# start and end postion
		pair1 = (int(line[3]), int(line[4]))
		pair2 = (line[2], line[11])

		pair = (pair2, pair1)
		# range and miRNA/gene name

		if key not in RNA:

			RNA[key] = Q.PriorityQueue()

		RNA[key].put((pair))

	# print(len(gene))

	# f = open("gene_id.txt","w+")

	# for each in gene:
	# 	f.write(each + "\n")

	# f.close()


	for key in RNA.keys():

		record = []

		while not RNA[key].empty():

			record.append(RNA[key].get())

		RNA[key] = record

	return RNA


def matchPeak(file1, file2):

	# bed
	exper = hashOrder(file1)
	
	# ref
	refer = omg(file2)

	rec = set()

	f1 = open(f3, "w+")

	for indexs in exper.keys():

		if indexs in refer.keys():
			
			# peak
			sample1 = exper[indexs]

			# ref
			sample2 = refer[indexs]

			# peak
			for one in sample1:

				# ref
				for each in sample2:

					point = one[0] + 100

					if point >= each[1][0] and point <= each[1][1]:

						rec.add(indexs + "\t" + str(one[0]) + "\t" + str(one[1]) + "\t"  + str(each[1][0]) + "\t" + str(each[1][1]) + "\t" + each[0][0] + "\t"  + each[0][1] + "\n")
	for each in rec:
		f1.write(each)

file1 = sys.argv[1]
file2 = sys.argv[2]
f3 = sys.argv[3]

matchPeak(file1, file2, f3)