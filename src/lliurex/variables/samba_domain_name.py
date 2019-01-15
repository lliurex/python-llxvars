def init(args=None):
	try:
		samba_domain_name = args['SAMBA_DOMAIN_NAME']
	except:
		samba_domain_name = 'lliurex'
	return samba_domain_name
	
#def init
