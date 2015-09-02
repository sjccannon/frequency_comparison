#objective: identify pathogenic variants in hgmd that have a MAF > 1 in exac
 
import re


#assign infiles and create an outfile 
with open("hgmd") as infile1, open("result", "w") as outfile:
#write the variants annotated as disease in hgmd to the outfile 
			for line in infile1:
				if "Disease causing mutation" in line:
					outfile.write(line)

#using regular expressions to identify where more than one variant has been identified in a cohort
p = re.compile('\d*,\d') #make sure match all numbers not just 1-9 

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
			print more_mut
			num_in_list = len(more_mut)#everytime there is more than one for each of these things do that action
			print num_in_list
			#removiing the comma from the identified strings
			result = re.sub('[,]', '', more_mut)
			print result
			#turning each digit into an integer
			#need an array within a hash table 
	#turn into array, put array in hash table with id (first column) as the key - the bit that
	#links the tables together
	#loop through the first file to do this to make the lookup database, in the array could have the third column as the final data element. can then remove this from the array 
	#before each loop assign it to a variable if putting the array in by reference will have to de reference it. 
	#
	#key = id, the value for this key needs to be an array of 
	#split by commas to form an array 
			x = int(result)
			y = x.split()
			print y
			#for digit in str(result):
			#	x = int(digit)
			#	list_of_integers = list(x)
					
 

#with open("result", "rw") as infile1, open("exac.frequencies", "r") as infile2:
#	for line in infile2:
#		column = line.split()
#		MAF = column[1]/column[2]
#			if column[2] == 
#	for line in infile1:
#		column = line.split()	
#
#if location in exac == location in HGM
