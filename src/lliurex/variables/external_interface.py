def init(args=None):
	try:
		external_interface = args['external_interface']
	except:
		external_interface = 'eth1'
	return external_interface