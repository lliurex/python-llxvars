def init(args=None):
    try:
        export_dirs = args['DIRS']
    except: 
        export_dirs = '/net/mirror /net/server-sync'
    return export_dirs
	
#def init
