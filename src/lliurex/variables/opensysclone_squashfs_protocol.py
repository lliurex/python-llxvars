def init(args=None):
	try:
		opensysclone_squash_protocol = args['protocol']
	except:
		opensysclone_squash_protocol = 'tftp'
	return opensysclone_squash_protocol
