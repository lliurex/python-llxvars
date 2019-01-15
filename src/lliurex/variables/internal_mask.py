import lliurex.net
def init(args=None):
	try:
		internal_mask = int(lliurex.net.get_net_size(args['internal_mask']))
	except:
		internal_mask = 24
	return internal_mask
