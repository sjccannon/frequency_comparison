#objective: identify pathogenic variants in hgmd that have a MAF > 1 in exac
 
import re


#assign infiles and create an outfile 
with open("hgmd") as infile1, open("result", "w") as outfile:
#write the variants annotated as disease in hgmd to the outfile 
			for line in infile1:
				if "Disease causing mutation" in line:
					outfile.write(line)

#using regular expressions to identify where more than one variant has been identified in a cohort
p = re.compile('\d*,\d')

#opening the exac file
with open("exac.frequencies", "r") as file:
	#looping through each line in the exac file
	for line in file:
		#splitting lines into useable columns
		columns = line.split()
		#identifying parts that have more than one varient 
		if p.match(columns[1]):
			#assigning a row to the variable more_mut if it meets the regular expression
			more_mut = columns[1]
			#removiing the comma from the identified strings
			result = re.sub('[,]', '', more_mut)
			#turning each digit into an integer
			x = int(result)
			print x
			#for digit in str(result):
			#	x = int(digit)
			#	list_of_integers = list(x)
			#num_in_list = len(list_of_strings))		
 

#with open("result", "rw") as infile1, open("exac.frequencies", "r") as infile2:
#	for line in infile2:
#		column = line.split()
#		MAF = column[1]/column[2]
#			if column[2] == 
#	for line in infile1:
#		column = line.split()	
#
#if location in exac == location in HGM
