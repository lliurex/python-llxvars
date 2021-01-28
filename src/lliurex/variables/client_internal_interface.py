#import xmlrpclib
import n4d.client
import lliurex.net
import time

def init(args=None):
	
	try:
		time.sleep(15)
		c=n4d.client.Client()
		#c=xmlrpclib.ServerProxy("https://server:9779",allow_none=True)
		c=n4d.client.Client("https://%s:9779"%ip)
		internal_network=c.get_variable("","VariablesManager","INTERNAL_NETWORK")
		internal_network = c.get_variable("INTERNAL_NETWORK")
		internal_mask=c.get_variable("INTERNAL_MASK")
		network=str(internal_network)+"/"+str(internal_mask)
		
		for dinfo in lliurex.net.get_devices_info():
			if lliurex.net.is_ip_in_range(dinfo["ip"],network):
				return dinfo["name"]
		
		return None
		
	except:
		return None
		

#def init
