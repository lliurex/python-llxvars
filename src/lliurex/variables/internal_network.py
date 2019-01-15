import lliurex.net
def init(args=None):
	try:
		ip = args['ip']
		netmask = args['netmask']
		internal_network = lliurex.net.get_network_ip(ip,netmask)
	except:
		internal_network = '10.2.1.0'
	return internal_network 
