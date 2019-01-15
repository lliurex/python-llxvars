def init(args=None):
	try:
		epoptes_srv = args['epoptes_srv']
	except:
		epoptes_srv = 'server'
	return epoptes_srv
