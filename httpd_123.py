#!/usr/bin/python3
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

#  curl -F "data=@endianness.jpg" http://192.168.56.104:8087

# python -m httpd 8089
# httpd.py 8089
import os, sys, errno, getopt, signal, time, io
from time import sleep

from pythonX9 import *
#import SimpleHTTPServer
import http.server
#import BaseHTTPServer

app_list = []
is_quit = 0
app_apps = {
	"http_port": 8087,
	"http_bind": "0.0.0.0"
}

class HTTPServer_ctx(http.server.SimpleHTTPRequestHandler):
	def dump_header(self):
		DBG_IF_LN("** path **")
		DBG_IF_LN("{}".format(self.path))
		DBG_IF_LN("** headers **")
		DBG_IF_LN("{}".format(self.headers))

		#path = self.translate_path(self.path)
		self.filename = "/tmp/{}-{}".format( self.__class__.__name__, os_urandom_str(10) )
		DBG_IF_LN("** Body {} **".format( self.filename))

	def do_PUT(self):
		DBG_IF_LN("{}".format(DBG_TXT_ENTER))
		self.dump_header()

		if "Content-Length".lower() in map(str.lower, self.headers.keys()):
			length = int(self.headers["Content-Length"])

			with open(self.filename, "wb") as dst:
				buff = self.rfile.read(length)
				#print(buff)
				dst.write( buff )

		self.send_response(200)
		self.end_headers() # curl: (52) Empty reply from server

	def do_GET(self):
		DBG_IF_LN("{}".format(DBG_TXT_ENTER))
		self.dump_header()

		if "Content-Length".lower() in map(str.lower, self.headers.keys()):
			length = int(self.headers["Content-Length"])

			with open(self.filename, "wb") as dst:
				buff = self.rfile.read(length)
				#print(buff)
				dst.write( buff )

		self.send_response(200)
		self.end_headers() # curl: (52) Empty reply from server

	def do_POST(self):
		DBG_IF_LN("{}".format(DBG_TXT_ENTER))
		self.dump_header()

		if "Content-Length".lower() in map(str.lower, self.headers.keys()):
			length = int(self.headers["Content-Length"])

			with open(self.filename, "wb") as dst:
				buff = self.rfile.read(length)
				#print(buff)
				dst.write( buff )

		self.send_response(200)
		self.end_headers() # curl: (52) Empty reply from server

def app_start():
	global app_apps

	http.server.test(HandlerClass=HTTPServer_ctx, port=app_apps["http_port"], bind=app_apps["http_bind"])

def app_watch(app_ctx):
	global app_list

	app_list.append( app_ctx )

def app_release():
	global app_apps
	global app_list

	DBG_DB_LN("{}".format(DBG_TXT_ENTER))
	#try:
	#app_apps["httpd"].server_close()
	#except Exception:
	#	pass

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
	print("  -p, --port port number")
	app_exit()
	sys.exit(0)

def parse_arg(argv):
	global app_apps

	try:
		opts,args = getopt.getopt(argv[1:], "hd:p:", ["help", "debug", "port"])
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
			elif opt in ("-p", "--port"):
				app_apps["http_port"] = int(arg)
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

	#signal.signal(signal.SIGINT, signal_handler)
	#signal.signal(signal.SIGTERM, signal_handler)

	parse_arg(argv)

	app_start()

	app_exit()
	DBG_WN_LN("{} (is_quit: {})".format(DBG_TXT_BYE_BYE, is_quit))

if __name__ == "__main__":
	main(sys.argv[0:])
