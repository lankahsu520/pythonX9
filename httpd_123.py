#!/usr/bin/python3

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
http_port = 8087
http_bind = "0.0.0.0"

class HTTPServer_ctx(http.server.SimpleHTTPRequestHandler):
	def dump_header(self):
		DBG_IF_LN("** path **")
		DBG_IF_LN("{}".format(self.path))
		DBG_IF_LN("** headers **")
		DBG_IF_LN("{}".format(self.headers))

		#path = self.translate_path(self.path)
		self.filename = "/tmp/{}-{}".format( self.__class__.__name__, os_urandom(10) )
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

def app_stop():
	global is_quit

	if ( is_quit == 0 ):
		is_quit = 1

def app_exit():
	app_stop()

def show_usage(argv):
	print("Usage: {} <options...>".format(argv[0]) )
	print("  -h, --help")
	print("  port")
	app_exit()
	sys.exit(0)

def parse_arg(argv):
	global http_port

	try:
		opts,args = getopt.getopt(argv[1:], "h", ["help"])
	except getopt.GetoptError:
		show_usage(argv)

	#print (opts)
	#print (args)

	if (len(opts) > 0):
		for opt, arg in opts:
			if opt in ("-h", "--help"):
				show_usage(argv)
			else:
				print ("(opt: {})".format(opt))
	elif (len(args) > 0):
		http_port = int(args[0])
	else:
		show_usage(argv)

def signal_handler(sig, frame):
	if sig in (signal.SIGINT, signal.SIGTERM):
		app_exit()
		return
	sys.exit(0)

def main(argv):
	global http_port

	parse_arg(argv)

	http.server.test(HandlerClass=HTTPServer_ctx, port=http_port, bind=http_bind)

	app_exit()
	DBG_WN_LN("{} (is_quit: {})".format(DBG_TXT_BYE_BYE, is_quit))

if __name__ == "__main__":
	main(sys.argv[0:])
