#objective: identify pathogenic variants in hgmd that have a MAF > 1 in exac
 
import re

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
my_dict = {}

#opening the exac file to be read
with open("test.freq", "r") as file:
	#looping through each line in the exac file
	for line in file:
		#splitting lines into useable columns
		columns = line.split()
		#identifying parts in exac database that have more than one variant 
		if p.match(columns[1]):
			print columns[1]
			#creating a list of each character from the string concatenated with the population column as the final character, split columns[1] by comma
			#it's necessary to split the columns[2] variable so itself becomes a list 
			more_mut = columns[1].split(",") + columns[2].split()			
			print more_mut
			location = columns[0]
			MAF_list = [] 
			for mut in more_mut:
				last = more_mut[-1]
				if mut != last:
					MAF = float(mut)/float(last)
					MAF_list.append(MAF)
					print MAF_list 
					#assigning these matches to a dictionary with postion as a key and the concatenated list as the value
				my_dict[location] = MAF_list					
		elif q.match(columns[1]):
			print columns[1]
			one_mut = columns[1].split(",") + columns[2].split()
			print one_mut
			location = columns[0]
			MAF_list = []
			for mut in one_mut:
				last = one_mut[-1]
				if mut != last:
					MAF = float(mut)/float(last)			
					MAF_list.append(MAF)
					print MAF_list
					my_dict[location] = MAF_list

		else:
			 print "error" + columns[1]

print my_dict 
