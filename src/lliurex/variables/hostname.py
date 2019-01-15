def init(args=None):
	try:
		hostname = args['hostname']
	except:
		hostname = 'pandora'
	return hostname


