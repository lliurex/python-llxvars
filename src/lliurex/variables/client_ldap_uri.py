def init(args=None):

	try:
		client_ldap_uri = args['uri']
	except:
		client_ldap_uri = ""
	return client_ldap_uri
	
#def init
