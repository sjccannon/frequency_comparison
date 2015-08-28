#objective: identify pathogenic variants in hgmd that have a MAF > 1 in exac
 
import re


#assign infiles and create an outfile 
with open("hgmd") as infile1, open("result", "w") as outfile:
#write the variants annotated as disease in hgmd to the outfile 
			for line in infile1:
				if "Disease causing mutation" in line:
					outfile.write(line)

#using regular expressions to identify where more than one variant has been identified 
p = re.compile('\d*,\d')

with open("exac.frequencies", "r") as file:
	for line in file:
		column = line.split()
		str(column[1])
		if p.match(column[1]):
			print column[1] 


#with open("result", "rw") as infile1, open("exac.frequencies", "r") as infile2:
#	for line in infile2:
#		column = line.split()
#		MAF = column[1]/column[2]
#			if column[2] == 
#	for line in infile1:
#		column = line.split()	
#
#if location in exac == location in HGMD
	
		
