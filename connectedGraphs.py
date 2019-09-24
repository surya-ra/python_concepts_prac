"""
1. Insert key value pair in a dictionary
2. Value in the form of list of lists
3. Search the values in a dictionary and find common elements using list
"""
from collections import defaultdict

class My_Dictionary(dict):
	def __init__(self):
		self = dict()

	def add(self, key, value):
		try:
			self[key].append(value)
		except KeyError:
			self[key] = [value]

def connectedGraphs():
	dict_obj = My_Dictionary()
	n = 6
	loop_run = int(n/2)
	thresh = 2
	arr_source = [1, 2, 3]
	arr_dest = [4, 5, 6]
	compiled_arr = arr_source + arr_dest
	res_bool = []
	ctr = 0
	temp = set()

	for elems in arr_source:
		temp_arr = findFactors(elems)
		dict_obj.add(ctr, temp_arr)
		ctr += 1
	ctr = 0
	for elems in arr_dest:
		temp_arr = findFactors(elems)
		dict_obj.add(ctr, temp_arr)
		ctr += 1

	for keys in dict_obj:
		temp.add(set(dict_obj[keys][0]) & set(dict_obj[keys][1]))
		print (temp)

		"""
		if temp > thresh:
			res_bool += 0
		else:
			res_bool += 1
		"""
	return res_bool





def findFactors(x):
	factor_store = []
	for i in range(1, x + 1):
		if x % i == 0:
			factor_store.append(i)
	return factor_store
 


print(connectedGraphs())
