def init(args=None):
	try:
		int_domain = args['DOMAIN']
	except:
		int_domain = 'aula'
	return int_domain
