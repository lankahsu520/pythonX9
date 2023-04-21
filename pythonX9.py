# -*- coding: utf-8 -*-
import os, sys, errno, getopt, signal, time, io
from time import sleep

import platform
# pip3 install numpy 
# import numpy as np # averageX

import fnmatch # file_find

import random

from pythonX9_def import *
from pythonX9_tag import *

import ctypes
__NR_gettid = 186  # gettid syscall number
libc = ctypes.CDLL('libc.so.6')

#******************************************************************************
# define
#******************************************************************************

def gettid():
 return libc.syscall(__NR_gettid)


#******************************************************************************
# UTIL_EX_DBG
#******************************************************************************
#** remote debug **
def remote_debug(server_ip="192.168.56.1", server_port=8864):
	sys.path.append("pydevd-pycharm.egg")
	import pydevd_pycharm

	pydevd_pycharm.settrace(server_ip, port=server_port, stdoutToServer=True, stderrToServer=True)

if ( USE_DBG_REMOTE == 1):
	remote_debug()

def dbg_more(*args):
	if not hasattr(dbg_more, "lvl"):
		dbg_more.lvl = DBG_LVL_DEFAULT  # it doesn't exist yet, so initialize it
	for arg in args:
		dbg_more.lvl = arg
	return dbg_more.lvl

def dbg_lvl_set(lvl= DBG_LVL_INFO):
	dbg_more(lvl)

def dbg_debug_helper(lvl):
	if lvl == 0:
		dbg_lvl_set(DBG_LVL_CRITICAL)
	elif lvl == 1:
		dbg_lvl_set(DBG_LVL_ERROR)
	elif lvl == 2:
		dbg_lvl_set(DBG_LVL_WARN)
	elif lvl == 3:
		dbg_lvl_set(DBG_LVL_INFO)
	elif lvl == 4:
		dbg_lvl_set(DBG_LVL_DEBUG)
	elif lvl == 5:
		dbg_lvl_set(DBG_LVL_TRACE)
	else:
		dbg_lvl_set(DBG_LVL_DEFAULT)

def DBG_XX_LN(f_back, need_lvl, color, *args):
	dbg_lvl = dbg_more()
	if ( len(args) == 2 ):
		obj = args[0]
		msg = args[1]
		#objname = "[{:04}/{:04}/{}]".format(os.getppid(), os.getpid(), obj.__class__.__name__)
		objname = "[{:04}/{:04}]".format( os.getpid(), gettid() )
		if hasattr(obj, "_dbg_more"):
			dbg_lvl = obj._dbg_more
	else:
		obj = None
		msg = args[0]
		objname = "[{:04}/{:04}]".format( os.getpid(), gettid() )

	filename = os.path.basename(f_back.f_code.co_filename)
	if ( dbg_lvl <= need_lvl ):
		print("{}{} {}|{}:{:04} - {}{}\r".format(color, objname, filename, f_back.f_code.co_name, f_back.f_lineno, (msg), COLOR_NONE))

def DBG_CR_LN(*args):
	try:
		raise Exception
	except:
		f_back = sys.exc_info()[2].tb_frame.f_back
	DBG_XX_LN(f_back, DBG_LVL_CRITICAL, COLOR_LIGHT_RED, *args)

def DBG_ER_LN(*args):
	try:
		raise Exception
	except:
		f_back = sys.exc_info()[2].tb_frame.f_back
	DBG_XX_LN(f_back, DBG_LVL_ERROR, COLOR_RED, *args)

def DBG_WN_LN(*args):
	try:
		raise Exception
	except:
		f_back = sys.exc_info()[2].tb_frame.f_back
	DBG_XX_LN(f_back, DBG_LVL_WARN, COLOR_PURPLE, *args)

def DBG_IF_LN(*args):
	try:
		raise Exception
	except:
		f_back = sys.exc_info()[2].tb_frame.f_back
	DBG_XX_LN(f_back, DBG_LVL_INFO, COLOR_YELLOW, *args)

def DBG_DB_LN(*args):
	try:
		raise Exception
	except:
		f_back = sys.exc_info()[2].tb_frame.f_back
	DBG_XX_LN(f_back, DBG_LVL_DEBUG, COLOR_WHITE, *args)

def DBG_TR_LN(*args):
	try:
		raise Exception
	except:
		f_back = sys.exc_info()[2].tb_frame.f_back
	DBG_XX_LN(f_back, DBG_LVL_TRACE, COLOR_DARY_GRAY, *args)

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

def getPYTHONbver():
	return "{0[0]}.{0[1]}.{0[2]}".format(sys.version_info)

def chkPYTHONge(major, minor, micro):
	return (sys.version_info >= (major, minor, micro))

def chkPYTHONle(major, minor, micro):
	return (sys.version_info <= (major, minor, micro))

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

def os_urandom(count):
	rand_num = random.randint(1e9, 1e10-1)
	rand_str = str(rand_num).zfill(count)
	return rand_str

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
		DBG_ER_LN(">>>{}".format( sdata ))
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

		self._last_time = time.process_time()

