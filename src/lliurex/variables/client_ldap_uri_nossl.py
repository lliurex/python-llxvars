def init(args=None):
	try:
		client_ldap_uri_nossl = args['uri']
	except:
		client_ldap_uri_nossl = ""
	return client_ldap_uri_nossl
	
#def init
