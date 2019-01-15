def init(args=None):
    try:
        disk = args['DEVICE']
    except: 
        disk = '/dev/vdb'
    return disk
	
#def init
