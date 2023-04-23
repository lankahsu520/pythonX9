#!/usr/bin/env python3

#import os, sys, errno, getopt, signal, time, io
#from time import sleep

from statex_api import *

app_list = []
is_quit = 0
app_apps = {
}

app_apps = {
}

def exec_cb_CloudConnected(data):
	DBG_IF_LN("(name: {})".format( data["name"] ))

def leave_cb_CloudConnected(data):
	DBG_WN_LN("(name: {})".format( data["name"] ))

StatexCloudConnected ={
"name":"CloudConnected", "priority":300, "init_cb": None, "exec_cb":exec_cb_CloudConnected, "leave_cb": leave_cb_CloudConnected
}

def exec_cb_NetworkOn(data):
	DBG_IF_LN("(name: {})".format( data["name"] ))

def leave_cb_NetworkOn(data):
	DBG_WN_LN("(name: {})".format( data["name"] ))

StatexNetworkOn ={
"name":"NetworkOn", "priority":600, "init_cb": None, "exec_cb":exec_cb_NetworkOn, "leave_cb": leave_cb_NetworkOn
}

def exec_cb_CableLinked(data):
	DBG_IF_LN("(name: {})".format( data["name"] ))

def leave_cb_CableLinked(data):
	DBG_WN_LN("(name: {})".format( data["name"] ))

StatexCableLinked ={
	"name": "CableLinked", "priority": 800, "init_cb": None, "exec_cb": exec_cb_CableLinked, "leave_cb": leave_cb_CableLinked
}

def exec_cb_Idle(data):
	DBG_IF_LN("(name: {})".format( data["name"] ))

def leave_cb_Idle(data):
	DBG_WN_LN("(name: {})".format( data["name"] ))

StatexIdle ={
	"name": "Idle", "priority": 999, "init_cb": None, "exec_cb": exec_cb_Idle, "leave_cb": leave_cb_Idle
}

def app_start():
	global is_quit
	statex_mgr = statex_ctx(dbg_more=DBG_LVL_DEBUG, name="HelloStateX", state_size=20, is_hold=0)

	app_watch(statex_mgr)
	statex_mgr.start( app_apps )
	statex_mgr.statex_gosleep()
	#statex_mgr.statex_push(name="Idle", priority=999, exec_cb=exec_cb_Idle, free_cb=free_cb_Idle)
	statex_mgr.statex_wakeup()

	# Idle->CableLinked->NetworkOn->CloudConnected
	statex_mgr.statex_push(StatexIdle)
	sleep(1)
	statex_mgr.statex_push(StatexCableLinked)
	sleep(1)
	statex_mgr.statex_push(StatexNetworkOn)
	sleep(1)
	statex_mgr.statex_push(StatexCloudConnected)
	sleep(1)

	# Idle->CableLinked->CloudConnected
	statex_mgr.statex_remove(StatexNetworkOn)
	sleep(1)

	# Idle->CableLinked
	statex_mgr.statex_pop()


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

	# dont block this function or print, signal_handler->app_stop
	if ( is_quit == 0 ):
		is_quit = 1

def app_exit():
	app_stop()
	app_release()
	DBG_DB_LN("{}".format(DBG_TXT_DONE))

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
		app_stop()
		return
	sys.exit(0)

def main(argv):
	global is_quit
	global app_apps

	signal.signal(signal.SIGINT, signal_handler)
	signal.signal(signal.SIGTERM, signal_handler)

	parse_arg(argv)

	app_start()

	app_exit()
	DBG_WN_LN("{} (is_quit: {})".format(DBG_TXT_BYE_BYE, is_quit))

if __name__ == "__main__":
	main(sys.argv[0:])
