#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 ***************************************************************************
 * Copyright (C) 2023, Lanka Hsu, <lankahsu@gmail.com>, et al.
 *
 * This software is licensed as described in the file COPYING, which
 * you should have received as part of this distribution.
 *
 * You may opt to use, copy, modify, merge, publish, distribute and/or sell
 * copies of the Software, and permit persons to whom the Software is
 * furnished to do so, under the terms of the COPYING file.
 *
 * This software is distributed on an "AS IS" basis, WITHOUT WARRANTY OF ANY
 * KIND, either express or implied.
 *
 ***************************************************************************
"""

#import os, sys, errno, getopt, signal, time, io
#from time import sleep

from multicast_api import *

appX_list = []
is_quit = 0
is_release = 0
argsX = {
}

ip="239.255.255.250"
port=3618

def notify_cb(buffer):
	DBG_IF_LN("buffer[{}] - {}".format( len(buffer), repr(buffer)) )

def argsX_set(name, val):
	global argsX
	argsX[name]=val

def argsX_get(name):
	return argsX[name]

def argsX_dump():
	#dbg_lvl_set(DBG_LVL_TRACE)
	DBG_IF_LN("{}".format( argsX ) )

def app_quit_get():
	return is_quit

def app_quit_set(mode):
	global is_quit
	is_quit=mode

def app_start():
	argsX_dump()

	multicast_mgr = multicast_ctx(dbg_lvl=DBG_LVL_TRACE, url="239.255.255.250", port=3618, readcb=notify_cb)
	app_watch(multicast_mgr)

	multicast_mgr.start( argsX )

	DBG_IF_LN("Send a packet every 2 seconds {}:{}.".format(multicast_mgr.addr, multicast_mgr.port) )

	idx=1
	while (app_quit_get() == 0 ):
		sleep(2)
		hello="{}".format(idx)
		multicast_mgr.writex(hello.encode())
		idx+=1

def app_watch(app_ctx):
	global appX_list

	appX_list.append( app_ctx )

def app_release():
	global appX_list
	global is_release

	if ( is_release == 0 ):
		is_release = 1
		DBG_DB_LN("{}".format(DBG_TXT_ENTER))
		for x in appX_list:
			try:
				objname = DBG_NAME(x)
				if not x.release is None:
					DBG_DB_LN("call {}.release ...".format( objname ) )
					x.release() # No handlers could be found for logger "google.api_core.bidi"
			except Exception:
				pass
		DBG_DB_LN("{}".format(DBG_TXT_DONE))

def app_stop():
	# dont block this function or print, signal_handler->app_stop
	if ( app_quit_get() == 0 ):
		app_quit_set(1)

		app_release()

def app_exit():
	app_stop()
	DBG_DB_LN("{}".format(DBG_TXT_DONE))

def show_usage(argv):
	print("Usage: {} <options...>".format(argv[0]) )
	print("  -h, --help")
	print("  -d, --debug level")
	print("    0: critical, 1: errror, 2: warning, 3: info, 4: debug, 5: trace")
	app_exit()
	sys.exit(0)

def parse_arg(argv):
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
	signal.signal(signal.SIGINT, signal_handler)
	signal.signal(signal.SIGTERM, signal_handler)

	parse_arg(argv)

	app_start()

	app_exit()
	DBG_WN_LN("{} (app_quit_get: {})".format(DBG_TXT_BYE_BYE, app_quit_get()) )

if __name__ == "__main__":
	main(sys.argv[0:])
