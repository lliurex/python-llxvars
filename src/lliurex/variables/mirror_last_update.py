import datetime

def init(args=None):

	try:
		now = datetime.datetime.now()
		return str(now)
	except:
		return str("None")

#def init
