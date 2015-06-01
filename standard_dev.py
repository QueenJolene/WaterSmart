import math

def standard_deviation(number_list):
	average = sum(number_list) / float(len(number_list))
	stdev = 0
	for value in number_list:
		stdev += (average - value)**2 / float(len(number_list))
		
 	return round(math.sqrt(stdev),4)


print standard_deviation([1,2,3,4,5])