def init(args=None):
    try:
        srv_name = args['NAME']
    except: 
        srv_name = 'server'
    return srv_name
	
#def init
