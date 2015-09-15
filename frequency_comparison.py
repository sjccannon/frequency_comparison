#objective: identify pathogenic variants in hgmd that have a MAF > 1 in exac
 
import re

#assign infiles and create an outfile 
#with open("hgmd") as infile1, open(exac.frequencies) as infile2, open("hgmd_disease", "w") as outfile:
#write the variants annotated as disease causing in hgmd to the outfile 
#			for line in infile1 and infile2:
#				line = line.rstrip()
#				if "Disease causing mutation" and in line:
#					outfile.write(line)

#using regular expressions to identify where more than one variant has been identified in a cohort
#^ means at the start, \d means digit for 0-9, + means just one match, , is a literal comma, .* means anythin an unlimited number of times.
#this therefore returns a match if it has a number comma number and then will greedily include everything else following the match   

p = re.compile('^\d+,\d.*')

#this looks for one number at the start of the string,the $ means tonly the number gets matched  
q = re.compile('^\d+$')

#creating a dictionary which can later be altere
my_dict = {}

#opening the exac file to be read the entry 11:11111111 was entered as a positive control to the test file
with open("exac.frequencies.test", "r") as file:
	#looping through each line in the exac file
	for line in file:
                line = line.rstrip()
		#print line
		#splitting lines into useable columns
		columns = line.split()
		#identifying parts in exac database that have more than one variant 
		if p.match(columns[1]):
			#creating a list of each character from the string concatenated with the population column as the final character, split columns[1] by comma
			#it's necessary to split the columns[2] variable so itself becomes a list 
			more_mut = columns[1].split(",") + columns[2].split()
			location = columns[0]
			MAF_list = []
			last = more_mut[-1]
			for mut in more_mut:
				#last = more_mut[-1]
				if mut != last:
					MAF = float(mut)/float(last)
					MAF_list.append(MAF)
					#assigning these matches to a dictionary with postion as a key and the concatenated list as the value
					my_dict[location] = MAF_list				
		elif q.match(columns[1]):
			one_mut = columns[1].split(",") + columns[2].split()
			location = columns[0]
			MAF_list = []
			last = one_mut[-1]
			for mut in one_mut:
				if mut != last:
					MAF = float(mut)/float(last)			
					MAF_list.append(MAF)
					my_dict[location] = MAF_list
		else:
			print "error" + columns[1]
print "dictionary complete"

#with open("my_dict", "w") as file:
#	file.write(my_dict)
#print  my_dict

#compare locations of disease causing mutations from hgmd_disease file with dictionary entries

#compare hgmd_disease to my_dict which containins locations as keys and a list of MAF(s) as the values
#iterate thrrough hgmd_disease lines using location

count = 0
count2 = 100000000

#open hgmd_disease file
with open("hgmd_disease_genes", "r") as infile, open("test.result2", "wa") as outfile:
	#iterate through the lines
	for line in infile:
		#split each line into columns 
		columns = line.split()
		#assign column [0] to variable k
		key = columns[0]
		#if column 0 (location) is in the dictionary keys
		if key in my_dict.keys():
			#assign the values of that key to variable v
			print key
			value = (my_dict[key])
			#for each value in the list relating to identified keys 
			count += 1
			print count 
			for each in value:
				#if each value is greater than 0.01
				if each > 0.01:
					print key
					print str(each) + "written"
					outfile.write(line + " " + str(each) + "\n")	 
#		else:
#			count2 += 1 
#			print str(key) + str(count2) 
outfile.close()
#output file to include exac colunms followed by hgmd_disease coulmns


#can use this to count the lines in the given file
#with open("hgmd_disease", "r") as f:  e_exac_MAF", "w") as outfile:
#	for i,l in enumerate(f):
#		pass
#	print i + 1	
