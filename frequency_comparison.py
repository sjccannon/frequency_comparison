#objective: identify pathogenic variants in hgmd that have a MAF > 1 in exac
 
import re
import decimal

#assign infiles and create an outfile 
with open("hgmd") as infile1, open("result", "w") as outfile:
#write the variants annotated as disease causing in hgmd to the outfile 
			for line in infile1:
				if "Disease causing mutation" in line:
					outfile.write(line)

#using regular expressions to identify where more than one variant has been identified in a cohort
#^ means at the start, \d means digit for 0-9, + means just one match, , is a literal comma, .* means anythin an unlimited number of times.
#this therefore returns a match if it has a number comma number and then will greedily include everything else following the match   
p = re.compile('^\d+,\d.*')

#this looks for one number at the start of the string,the $ means tonly the number gets matched  
q = re.compile('^\d+$')

#creating a dictionary which can later be altere
my_dict = {'location': 'list_of_MAFs'}

#opening the exac file to be read
with open("test.freq", "r") as file:
	#looping through each line in the exac file
	for line in file:
		#splitting lines into useable columns
		columns = line.split()
		#identifying parts in exac database that have more than one variant 
		if p.match(columns[1]):
			#creating a list of each character from the string concatenated with the population column as the final character, split columns[1] by comma
			#it's necessary to split the columns[2] variable so itself becomes a list 
			more_mut = columns[1].split(",") + columns[2].split()			
			location = columns[0]
			#print location
			MAF_list = [] 
			for mut in more_mut:
				last = more_mut[-1]
				if mut != last:
					MAF = float(mut)/float(last)
					MAF_list.append(MAF)
					print MAF_list
					#assigning these matches to a dictionary with postion as a key and the concatenated list as the value
				#my_dict[columns[0]] = MAF
				#print my_dict		
				my_dict={location:MAF_list}	
				print my_dict 
		#identifying parts with only one varient
		#elif q.match(columns[1]):
		#	#assigning these matches to a dictionary with position as key and the concatenated lists as the value
		#	one_mut = columns[1].split() + columns[2].split() 	
		#	my_dict[columns[0]] = one_mut

#print my_dict 




			#num_in_list = len(more_mut)#everytime there is more than one for each of these things do that action
			#print num_in_list
			#removiing the comma from the identified strings
			#result = re.sub('[,]', '', more_mut)
			#print result
			#turning each digit into an integer
			#need an array within a hash table 
	#turn into array, put array in hash table with id (first column) as the key - the bit that
	#links the tables together
	#loop through the first file to do this to make the lookup database, in the array could have the third column as the final data element. can then remove this from the array 
	#before each loop assign it to a variable if putting the array in by reference will have to de reference it. 
	#
	#key = id, the value for this key needs to be an array of 
	#split by commas to form an array 
			#x = int(result)
			#y = x.split()
			#print y
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
