def init(args=None):
	try:
		srv_ip = args['ip']
	except:
		srv_ip = '10.3.0.254'
	return srv_ip