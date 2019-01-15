def init(args=None):
	try:
		enable_nss_ldap = args['ENABLE_NSS_LDAP']
	except:
		enable_nss_ldap = ""
	
	return enable_nss_ldap
	
#def init
