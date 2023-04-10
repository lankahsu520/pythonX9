# -*- coding: utf-8 -*-

import os, sys, errno, getopt, signal, time, io
from time import sleep
import logging

import platform
# pip3 install numpy 
# import numpy as np # averageX

import fnmatch # file_find

#******************************************************************************
# define
#******************************************************************************
USE_DBG_REMOTE = 0

OS_LINUX = "linux, linux2"
OS_OSX = "darwin"
OS_WINDOWS = "win32"

PYTHON_V2 = 2
PYTHON_V3 = 3

TAG_ACTION = "action"

TAG_CACHE_DB = "cache_db"
TAG_ID = "id"
TAG_CHANNEL_ID = "cid"
TAG_CHANNEL_TXT = "cid_txt"
#TAG_CONTEXT = "context"
TAG_CRAWLER = "crawler"

TAG_DBG_LOGGING ="dbg_logging"
TAG_DBG_MORE = "dbg_more"
TAG_DBG_PATH = "dbg_path"

TAG_DEPTH_LVL = "depth_lvl"
TAG_DEPTH_MAX = "depth_max"

TAG_FILE_ID = "file_id"
TAG_FUNC_CB = "func_cb"

TAG_HANDLE = "handle"

TAG_GROUP_ID = "tid"
TAG_GROUP_TXT = "tid_txt"

TAG_HTTP_REFERER = "Referer"
TAG_HTTP_USER_AGENT = "User-Agent"

TAG_QUERY_STRING = "query_string"

TAG_LAST_TIME = "last_time"

TAG_MODE_ID = "mode_id"

TAG_NO_CACHE = "no_cache"

TAG_OUT_FILE = "out_file"

TAG_REFERER = "referer"
TAG_ROOT_URL = "root_url"

TAG_SEARCH_STRING = "search_string"
TAG_SITE_ARY = "site_ary"

TAG_TIMEOUT ="timeout"
TAG_TITLE = "title"
TAG_TITLE_ARY = "title_ary"
TAG_TITLE_TXT = "title_txt"

TAG_USRDATA = "usrdata"

TAG_URL = "url"
TAG_URL_TXTS = "utxts"
TAG_URL_AND_TXT = "url_and_txt"

#******************************************************************************
# UTIL_EX_DBG
#******************************************************************************
logging.TRACE = logging.DEBUG-5
logging.addLevelName(logging.TRACE, 'TRACE')  
logging.trace = lambda x: logging.log(logging.TRACE, x)

COLOR_NONE = "\033[0m"
COLOR_RED = "\033[0;32;31m"
COLOR_LIGHT_RED = "\033[1;31m"
COLOR_GREEN = "\033[0;32;32m"
COLOR_LIGHT_GREEN = "\033[1;32m"
COLOR_BLUE = "\033[0;32;34m"
COLOR_LIGHT_BLUE = "\033[1;34m"
COLOR_DARY_GRAY = "\033[1;30m"
COLOR_CYAN = "\033[0;36m"
COLOR_LIGHT_CYAN = "\033[1;36m"
COLOR_PURPLE = "\033[0;35m"
COLOR_LIGHT_PURPLE = "\033[1;35m"
COLOR_BROWN = "\033[0;33m"
COLOR_YELLOW = "\033[1;33m"
COLOR_LIGHT_GRAY = "\033[0;37m"
COLOR_WHITE = "\033[1;37m"

DBG_LVL_CRITICAL = logging.CRITICAL # 50
DBG_LVL_ERROR = logging.ERROR # 40
DBG_LVL_WARN = logging.WARNING # 30
DBG_LVL_INFO = logging.INFO # 20
DBG_LVL_DEBUG = logging.DEBUG # 10
DBG_LVL_TRACE = logging.TRACE
#DBG_LVL_MAX = 5

DBG_LVL_DEFAULT=DBG_LVL_INFO
#DBG_LVL_DEFAULT=DBG_LVL_TRACE

#** remote debug **
def remote_debug(server_ip="192.168.56.1", server_port=8864):
	sys.path.append("pydevd-pycharm.egg")
	import pydevd_pycharm

	pydevd_pycharm.settrace(server_ip, port=server_port, stdoutToServer=True, stderrToServer=True)

if ( USE_DBG_REMOTE == 1):
	remote_debug()

def DBG_LEVEL_SET(self):
	objname = self.__class__.__name__
	if (self._dbg_logging==1):
		#logging.basicConfig(level=dbg_more, format='%(message)s', filename = dbg_path)
		#logger = logging.getLogger(objname)
		self.dbg_func = logging
		#if hasattr(self, "dbg_func"):
		self.dbg_func.basicConfig(level=self._dbg_more, format='%(message)s', filename = self._dbg_path)

def DBG_CR_LN(self, msg=""):
	try:
		raise Exception
	except:
		f = sys.exc_info()[2].tb_frame.f_back
	objname = self.__class__.__name__
	if hasattr(self, "dbg_func"):
		self.dbg_func.critical("{}[{}|{}:{:04}] - {}{}".format(COLOR_LIGHT_RED, objname, f.f_code.co_name, f.f_lineno, (msg), COLOR_NONE))
	else:
		if ( self._dbg_more <= DBG_LVL_CRITICAL ):
			print("{}[{}|{}:{:04}] - {}{}\r".format(COLOR_LIGHT_RED, objname, f.f_code.co_name, f.f_lineno, (msg), COLOR_NONE))

def DBG_ER_LN(self, msg=""):
	try:
		raise Exception
	except:
		f = sys.exc_info()[2].tb_frame.f_back
	objname = self.__class__.__name__
	if hasattr(self, "dbg_func"):
		self.dbg_func.error("{}[{}|{}:{:04}] - {}{}".format(COLOR_RED, objname, f.f_code.co_name, f.f_lineno, (msg), COLOR_NONE))
	else:
		if ( self._dbg_more <= DBG_LVL_ERROR ):
			print("{}[{}|{}:{:04}] - {}{}\r".format(COLOR_RED, objname, f.f_code.co_name, f.f_lineno, (msg), COLOR_NONE))

def DBG_WN_LN(self, msg=""):
	try:
		raise Exception
	except:
		f = sys.exc_info()[2].tb_frame.f_back
	objname = self.__class__.__name__
	if hasattr(self, "dbg_func"):
		self.dbg_func.warning("{}[{}|{}:{:04}] - {}{}".format(COLOR_PURPLE, objname, f.f_code.co_name, f.f_lineno, (msg), COLOR_NONE))
	else:
		if ( self._dbg_more <= DBG_LVL_WARN ):
			print("{}[{}|{}:{:04}] - {}{}\r".format(COLOR_PURPLE, objname, f.f_code.co_name, f.f_lineno, (msg), COLOR_NONE))

def DBG_IF_LN(self, msg=""):
	try:
		raise Exception
	except:
		f = sys.exc_info()[2].tb_frame.f_back
	objname = self.__class__.__name__
	if hasattr(self, "dbg_func"):
		self.dbg_func.info("{}[{}|{}:{:04}] - {}{}".format(COLOR_YELLOW, objname, f.f_code.co_name, f.f_lineno, (msg), COLOR_NONE))
	else:
		if ( self._dbg_more <= DBG_LVL_INFO ):
			print("{}[{}|{}:{:04}] - {}{}\r".format(COLOR_YELLOW, objname, f.f_code.co_name, f.f_lineno, (msg), COLOR_NONE))

def DBG_DB_LN(self, msg=""):
	try:
		raise Exception
	except:
		f = sys.exc_info()[2].tb_frame.f_back
	objname = self.__class__.__name__
	if hasattr(self, "dbg_func"):
		self.dbg_func.debug("{}[{}|{}:{:04}] - {}{}".format(COLOR_WHITE, objname, f.f_code.co_name, f.f_lineno, (msg), COLOR_NONE) )
	else:
		if ( self._dbg_more <= DBG_LVL_DEBUG ):
			print("{}[{}|{}:{:04}] - {}{}\r".format(COLOR_WHITE, objname, f.f_code.co_name, f.f_lineno, (msg), COLOR_NONE) )

def DBG_TR_LN(self, msg=""):
	try:
		raise Exception
	except:
		f = sys.exc_info()[2].tb_frame.f_back
	objname = self.__class__.__name__
	objname = self.__class__.__name__
	if hasattr(self, "dbg_func"):
		self.dbg_func.trace("{}[{}|{}:{:04}] - {}{}".format(COLOR_LIGHT_GRAY, objname, f.f_code.co_name, f.f_lineno, (msg), COLOR_NONE) )
	else:
		if ( self._dbg_more <= DBG_LVL_TRACE ):
			self.dbg_func("{}[{}|{}:{:04}] - {}{}\r".format(COLOR_LIGHT_GRAY, objname, f.f_code.co_name, f.f_lineno, (msg), COLOR_NONE))

def DBG_NAME(self):
	return self.__class__.__name__

def debug_attr(obj):
	for attr in dir(obj):
		try:
			print("obj.{} = {}".format(attr, getattr(obj, attr)))
		except AttributeError:
			print("obj.{} = ?".format(attr))

def dump2hex(obj):
	#valp = [ ord(c) for c in obj]
	valp=bytes(obj)
	val_str = ' '.join( format(x, '02x') for x in valp)
	print(val_str)

#******************************************************************************
# UTIL_EX_BASIC
#******************************************************************************
def isOS(X):
	return (sys.platform in X)

def isPYTHON(X):
	return (sys.version_info[0] == X)

def averageX(X):
	#return np.mean(X)
	return sum(X) / len(X)

def ittle2byte(size, val):
	#data = val.to_bytes(size, byteorder="little")
	#return data
	data = bytes(1)
	if ( size == 1 ):
		return struct.pack('B', val)
	elif ( size == 2 ):
		return struct.pack('<H', val )
	elif ( size == 4 ):
		return struct.pack('<I', val)
	return data

def byte2little(size, data):
	num = 0
	if ( size == 1 ):
		return data[0]
	elif ( size == 2 ):
		num = struct.unpack('>H', struct.pack('2B', data[0], data[1]) )
		return num[0]
	elif ( size == 4 ):
		num = struct.unpack('>I', struct.pack('4B', data[0], data[1], data[2], data[3]) )
		return num[0]
	return num

def u8Str(txt):
	return txt.encode('utf-8')

def uStr(txt):
	return u"{}".format(txt)

def file_find(directory, pattern):
	for root, dirs, files in os.walk(directory):
		for basename in files:
			if fnmatch.fnmatch(basename, pattern):
				filename = os.path.join(root, basename)
				yield filename

#******************************************************************************
# UTIL_EX_NETWORK
#******************************************************************************
def get_ifaces():
	import netifaces as ni
	return ni.interfaces()

def get_ipaddr():
	if ( isOS(OS_WINDOWS) ):
		iface = ""
		ipaddr = ""
	else:
		#Use ip route list
		import subprocess
		arg='ip route list'
		p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
		data = p.communicate()
		sdata = data[0].decode().split()
		ipaddr = sdata[ sdata.index('src')+1 ]
		iface = sdata[ sdata.index('dev')+1 ]
	return (iface, ipaddr)

def get_ipaddr_ping():
	'''
	Source:
	http://commandline.org.uk/python/how-to-find-out-ip-address-in-python/
	'''
	import socket
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(('google.com', 0))
	ipaddr= s.getsockname()[0]
	return ipaddr

def get_hwaddr(netdev='eth0'):
	# Use ip addr show
	import subprocess
	arg='ip addr show ' + netdev 
	p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
	data = p.communicate()
	sdata = data[0].decode().split('\n')
	macaddr = sdata[1].strip().split(' ')[1]
	ipaddr = sdata[2].strip().split(' ')[1].split('/')[0]
	return (macaddr, ipaddr)

#STATIC_IP="127.0.0.1"
##STATIC_IP = "127.0.0.1"
#STATIC_IFACE = "eth0"
#STATIC_PORT = "9981"
#(STATIC_IFACE, STATIC_IP) = get_ipaddr()

#******************************************************************************
# pythonX9
#******************************************************************************
class pythonX9(object):
	def inkey(self):
		if ( isOS(OS_WINDOWS) ):
			import keyboard
			return keyboard.read_key()
		else:
			import tty, termios # keyboard

			fd = sys.stdin.fileno()
			old_settings = termios.tcgetattr(fd)
			try:
				tty.setraw(sys.stdin.fileno())
				ch = sys.stdin.read(1)
			finally:
				termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
			return ch

	def release(self):
		self.is_quit = 1

	def __init__(self, dbg_more=DBG_LVL_DEFAULT, dbg_logging=0, dbg_path="", func_cb=None, usrdata=None):
		self.is_quit = 0
		self._dbg_more = dbg_more
		self._dbg_logging = dbg_logging
		self._dbg_path = dbg_path
		self._func_cb = func_cb
		self._usrdata = usrdata
		DBG_LEVEL_SET(self)
	
		self._last_time = time.process_time()

