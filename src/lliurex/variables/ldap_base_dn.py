def init(args=None):
	try:
		base_dn = args['LDAP_BASE_DN']
	except:
		base_dn = 'dc=ma5,dc=lliurex,dc=net'
	return base_dn
	
#def init
