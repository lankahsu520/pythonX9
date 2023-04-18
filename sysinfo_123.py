#!/usr/bin/env python3

#import os, sys, errno, getopt, signal, time, io
#from time import sleep

from sysinfo_api import *

app_list = []
is_quit = 0
app_apps = {
	"keyboard": 1,
	"interval": 5
}

def app_start():
	#dbg_lvl_set(DBG_LVL_TRACE)
	sysinfo_mgr = sysinfo_ctx(dbg_more=DBG_LVL_TRACE)
	app_watch(sysinfo_mgr)
	sysinfo_mgr.start(args={"keyboard": 1, "interval": 5})
	#sysinfo_mgr.keyboard_recv()
	sysinfo_mgr.release()

def app_watch(app_ctx):
	global app_list

	app_list.append( app_ctx )

def app_release():
	global app_list

	DBG_WN_LN("enter")
	for x in app_list:
		try:
			objname = DBG_NAME(x)
			if not x.release is None:
				DBG_IF_LN("call {}.release ...".format( objname ) )
				x.release() # No handlers could be found for logger "google.api_core.bidi"
		except Exception:
			pass

def app_stop():
	global is_quit

	if ( is_quit == 0 ):
		is_quit = 1

		app_release()

def app_exit():
	app_stop()

def show_usage(argv):
	print("Usage: {} <options...>".format(argv[0]) )
	print("  -h, --help")
	print("  -k, --key")
	print("  -d, --debug level")
	print("    0: critical, 1: errror, 2: warning, 3: info, 4: debug, 5: trace")
	app_exit()
	sys.exit(0)

def parse_arg(argv):
	global app_apps

	try:
		opts,args = getopt.getopt(argv[1:], "hkd:", ["help", "key", "debug"])
	except getopt.GetoptError:
		show_usage(argv)

	#print (opts)
	#print (args)

	if (len(opts) > 0):
		for opt, arg in opts:
			#DBG_IF_LN("opt:{}, arg:{}".format(opt, arg))
			if opt in ("-h", "--help"):
				show_usage(argv)
			elif opt in ("-k", "--key"):
				app_apps["keyboard"] = 1
			elif opt in ("-d", "--debug"):
				#app_apps["debug"] = int(arg)
				dbg_debug_helper( int(arg) )
				#DBG_IF_LN("arg:{}".format(arg))
			else:
				print ("(opt: {})".format(opt))
	else:
		show_usage(argv)

def signal_handler(sig, frame):
	if sig in (signal.SIGINT, signal.SIGTERM):
		app_exit()
		return
	sys.exit(0)

def main(argv):
	global app_apps

	signal.signal(signal.SIGINT, signal_handler)
	signal.signal(signal.SIGTERM, signal_handler)

	parse_arg(argv)

	app_start()

	app_exit()
	DBG_IF_LN("bye bye !!! (is_quit: {})".format(is_quit))

if __name__ == "__main__":
	main(sys.argv[0:])
