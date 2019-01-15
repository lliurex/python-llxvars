def init(args=None):
	'''initialize example variable'''

	try:
		a=args["a"]
		b=args["b"]
	except:
		a=1
		b=2

	
	return support_function(a,b)
	
#def init


def support_function(a,b):
	
	return a+b
	
#def support_function