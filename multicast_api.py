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
from pythonX9 import *
from threadx_api import *

import select, socket
import struct

class multicast_ctx(pythonX9, threadx_ctx):

	def openx(self):
		self.sockfd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
		self.sockfd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		#sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 32)

	def closex(self):
		if not self.sockfd is None:
			self.sockfd.close()
			self.sockfd = None
			DBG_DB_LN(self, "{}".format(DBG_TXT_DONE) )

	def serverx(self):
		mreq = struct.pack("4sl", socket.inet_aton(self.addr), socket.INADDR_ANY)
		self.sockfd.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

		DBG_IF_LN(self, "bind ... ({}:{})".format(self.addr, self.port) )
		self.sockfd.bind((self.addr, self.port))

	def writex(self, buf):
		DBG_DB_LN(self, "send {}:{} - {}".format(self.addr, self.port, buf) )

		if ( self.is_quit == 0 ):
			try:
				self.sockfd.sendto(buf, (self.addr, self.port))
			except Exception:
				pass

	def readx(self):
		self.serverx()

		rlist = [self.sockfd]
		wlist, xlist  = [], []

		DBG_WN_LN(self, "{}".format( DBG_TXT_RUN_LOOP ) )
		while ( self.is_quit == 0 ):
			readable, writeable, exceptional = select.select(rlist, wlist, xlist, 1)

			for sock in readable:
				try:
					if self.sockfd is not None:
						buffer = self.sockfd.recv(self.max_size)
						#print len(buf)
						#print repr(buf)
						if not self.readcb is None:
							self.readcb(buffer)
						else:
							DBG_DB_LN(self, "buffer[{}] - {}".format( len(buffer), repr(buffer)) )
				except KeyboardInterrupt:
					self.is_quit = 1
				except (IOError, OSError) as exc:
					err = None
					if hasattr(exc, 'errno'):
							err = exc.errno
					elif exc.args:
							err = exc.args[0]
					if err == errno.EINTR:
							continue
					raise
				finally:
					pass
		self.closex()

	def threadx_handler(self):
		#DBG_IF_LN(self, "enter")
		self.threadx_set_inloop(1)
		self.readx()
		self.threadx_set_inloop(0)
		DBG_WN_LN(self, "{}".format(DBG_TXT_BYE_BYE))

	def release(self):
		if ( self.is_quit == 0 ):
			self.is_quit = 1
			if ( self.threadx_inloop() == 1 ):
				self.threadx_wakeup()
			self.threadx_join()
			self.closex()
			DBG_DB_LN(self, "{}".format(DBG_TXT_DONE))

	def ctx_init(self, url, port, readcb):
		DBG_DB_LN(self, "{}".format(DBG_TXT_ENTER))

		self.sockfd = None
		self.addr = url
		self.port = port
		self.readcb = readcb
		self.max_listen = 1
		self.max_size = 2048

		self.closex()
		self.openx()
		self.count = 0

	def __init__(self, url, port, readcb, **kwargs):
		if ( isPYTHON(PYTHON_V3) ):
			super().__init__(**kwargs)
		else:
			super(multicast_ctx, self).__init__(**kwargs)

		DBG_TR_LN(self, "{}".format(DBG_TXT_ENTER))
		self._kwargs = kwargs
		self.ctx_init(url, port, readcb)

	def parse_args(self, args):
		DBG_TR_LN(self, "{}".format(DBG_TXT_ENTER))
		self._args = args

	def start(self, args={}):
		DBG_TR_LN(self, "{}".format(DBG_TXT_START))
		self.parse_args(args)
		self.threadx_init()

#ip="239.255.255.250"
#port=3618
#multicast = multicast_ctx(ip, port, notify_cb)
#multicast.release()
