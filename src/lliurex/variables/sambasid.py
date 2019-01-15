import subprocess

def init(args=None):
	try:
		pprocess = subprocess.Popen(['net','getlocalsid'],stdout=subprocess.PIPE)
		sid = pprocess.communicate()[0].split(":")[1]
		sid = sid[1:len(sid)-1]	
	except:
		sid = ""
	return sid
	
#def init
