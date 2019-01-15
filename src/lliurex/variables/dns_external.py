def init(args=None):
	try:
		dns = args['DNS']
	except:
		dns = ['172.27.111.5','172.27.111.6']
	return dns
#def init

