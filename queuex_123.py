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

from queuex_api import *

appX_list = []
is_quit = 0
is_release = 0
argsX = {
}

def exec_cb(data):
	DBG_IF_LN("(data: {})".format( data ))

def queue_test(is_stack=0):
	#dbg_lvl_set(DBG_LVL_DEBUG)
	queuex_mgr = queuex_ctx(dbg_lvl=DBG_LVL_DEBUG, name="HelloQueueX", queue_size=20, exec_cb=exec_cb, free_cb=None, is_stack=is_stack)
	app_watch(queuex_mgr)

	queuex_mgr.start( argsX )

	queuex_mgr.queuex_gosleep()
	DBG_IF_LN("Push an integer every 10/1000 seconds. (is_stack: {})".format( is_stack ))
	idx=1
	while (app_quit_get() == 0 ):
		sleep(10/1000)
		item=idx
		DBG_DB_LN("call queuex_push ... (item: {})".format( item ) )
		queuex_mgr.queuex_push(idx)
		idx+=1
		if ( idx == 6):
			queuex_mgr.queuex_wakeup()
		if ((idx%11==0)):
			break

def queue_test_dict():
	#dbg_lvl_set(DBG_LVL_DEBUG)
	queuex_mgr = queuex_ctx(dbg_lvl=DBG_LVL_DEBUG, name="HelloQueueX", queue_size=20, exec_cb=exec_cb, free_cb=None, is_stack=0, is_sort=1, dict_key="key")
	app_watch(queuex_mgr)

	queuex_mgr.start( argsX )

	queuex_mgr.queuex_gosleep()

	idx=1
	while (app_quit_get() == 0 ):
		sleep(10/1000)
		item={"key":os_urandom(),"idx":idx}
		DBG_DB_LN("call queuex_push ... (item: {})".format( item ) )
		queuex_mgr.queuex_push(item)
		idx+=1
		if ( idx == 8):
			queuex_mgr.queuex_wakeup()
		if ((idx%11==0)):
			break

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

	queue_test(is_stack=0)
	queue_test(is_stack=1)
	queue_test_dict()

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
