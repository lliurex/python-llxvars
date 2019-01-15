def init(args=None):
	try:
		internal_interface = args['internal_interface']
	except:
		internal_interface = 'eth0'
	return internal_interface
