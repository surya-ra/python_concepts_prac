from collections import defaultdict

class FormDict:
	def creatDict(self, form_list):
		d = defaultdict(set)
		for k,v in form_list:
			d[k].add(v)
		return d

if __name__ == '__main__':
	List = [('blue',1),('blue',3),('green',3),('green',3),('red',2)]
	Callclass = FormDict()
	print(Callclass.creatDict(List))