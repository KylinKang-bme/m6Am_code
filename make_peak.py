# adjust the format of MACS2 output files (summit file)
# also need to keep the chr number and name the same with the reference vcf file (use bash)
import sys

f = sys.argv[1]
wr = sys.argv[2]

with open(f) as file:
	data = file.readlines()


w = open(wr,'w+')

for each in data:
	each = each.strip("\n").split("\t")
	summit = int(each[1])

	w.write(each[0] + "\t" + str(summit-100) + "\t" + str(summit+100) 
		+ "\t" + each[3] + "\t" + each[4] +"\n")


w.close() 

