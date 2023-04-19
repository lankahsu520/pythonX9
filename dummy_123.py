#!/usr/bin/env python3

#import os, sys, errno, getopt, signal, time, io
#from time import sleep

from dummy_api import *

app_list = []
is_quit = 0
app_apps = {
}

def app_start():
	#dbg_lvl_set(DBG_LVL_DEBUG)
	DBG_IF_LN("(Python version: {}, chkPYTHONge(3,7,0): {}, chkPYTHONle(3,7,0): {})".format( getPYTHONbver(), chkPYTHONge(3,7,0), chkPYTHONle(3,7,0) ))

	IFACE = "enp0s3"
	(IFACE_MAC, IFACE_IPv4) = get_hwaddr( IFACE )
	DBG_IF_LN("(IFACE: {}, IFACE_MAC: {}, IFACE_IPv4: {})".format( IFACE, IFACE_MAC, IFACE_IPv4 ))

	dummy_mgr = dummy_ctx(dbg_more=DBG_LVL_TRACE)
	app_watch(dummy_mgr)
	dummy_mgr.start( app_apps )

def app_watch(app_ctx):
	global app_list

	app_list.append( app_ctx )

def app_release():
	global app_list

	DBG_DB_LN("{}".format(DBG_TXT_ENTER))
	for x in app_list:
		try:
			objname = DBG_NAME(x)
			if not x.release is None:
				DBG_DB_LN("call {}.release ...".format( objname ) )
				x.release() # No handlers could be found for logger "google.api_core.bidi"
		except Exception:
			pass
	DBG_DB_LN("{}".format(DBG_TXT_DONE))

def app_stop():
	global is_quit

	if ( is_quit == 0 ):
		is_quit = 1

		app_release()
		DBG_DB_LN("{}".format(DBG_TXT_DONE))

def app_exit():
	app_stop()

def show_usage(argv):
	print("Usage: {} <options...>".format(argv[0]) )
	print("  -h, --help")
	print("  -d, --debug level")
	print("    0: critical, 1: errror, 2: warning, 3: info, 4: debug, 5: trace")
	app_exit()
	sys.exit(0)

def parse_arg(argv):
	global app_apps

	try:
		opts,args = getopt.getopt(argv[1:], "hd:", ["help", "debug"])
	except getopt.GetoptError:
		show_usage(argv)

	#print (opts)
	#print (args)

	if (len(opts) > 0):
		for opt, arg in opts:
			if opt in ("-h", "--help"):
				show_usage(argv)
			elif opt in ("-d", "--debug"):
				dbg_debug_helper( int(arg) )
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
	DBG_WN_LN("{} (is_quit: {})".format(DBG_TXT_BYE_BYE, is_quit))

if __name__ == "__main__":
	main(sys.argv[0:])
