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

#https://streamlink.github.io/api.html
from streamlink import Streamlink, StreamError, PluginError, NoPluginError
import urllib.parse as urlparse
from urllib.parse import unquote as urlunquote

class streamlink_ctx(pythonX9):
	def streams_urlparse(self):
		self.urlparse = urlparse.urlparse( urlunquote(self.stream_url) )
		DBG_IF_LN(self, "(stream_url: {})".format(self.stream_url) )
		DBG_IF_LN(self, "(urlparse: {})".format(self.urlparse))

	def streams_fetch(self):
		self.session = Streamlink()
		self.session.set_option("stream-timeout", 15);
		try:
			self.streams = self.session.streams(self.stream_url)
		except PluginError as err:
			DBG_ER_LN(self, "streamlink.streams error !!! ({})".format(err) )
			self.streams = None

	def streams_choice(self, quality="best"):
		if self.streams:
			#print("{}".format(streams) )
			if quality in self.streams.keys():
				self.quality = quality
			else:
				self.quality = list(self.streams.keys())[0]

			DBG_IF_LN(self, "(quality: {} / {})".format(self.quality, self.streams.keys()) )
			self.stream = self.streams[self.quality]
		else:
			self.stream = None

	def streams_streaming(self):
		try:
			self.length = 0
			self.saveto_fd = open(self.filename, "wb")
			tmpbuff = self.stream_fd.read(self.chunksize)
			while (tmpbuff) and (self.is_quit==0):
				self.length += len(tmpbuff);
				#self.wfile.write(bytes("{}".format(data), "utf-8"))
				self.saveto_fd.write(tmpbuff)
				#print("#", end="", flush=True)
				print(f'\r{self.filename}: {self.length:,} bytes', end='', flush=True)
				tmpbuff = self.stream_fd.read(self.chunksize)
			print("\n")
			DBG_IF_LN(self, "Download complete !!!")
		except IOError as err:
			pass

		self.saveto_fd.close()
		self.stream_fd.close()

	def streams_savetofile(self, filename):
		if self.stream:
			try:
				self.filename = filename
				DBG_IF_LN(self, "(filename: {}, chunksize:{})".format(self.filename, self.chunksize) )

				self.stream_fd = self.stream.open()
				self.streams_streaming()
			except StreamError as err:
				DBG_ER_LN(self, "stream.open error !!! ({})".format(err) )

	def release(self):
		if ( self.is_quit == 0 ):
			self.is_quit = 1
			DBG_DB_LN(self, "{}".format(DBG_TXT_DONE))

	def ctx_init(self, url):
		DBG_DB_LN(self, "{}".format(DBG_TXT_ENTER))

		self.stream_url = url
		self.chunksize = 1024
		self.length = 0

	def __init__(self, url, **kwargs):
		if ( isPYTHON(PYTHON_V3) ):
			super().__init__(**kwargs)
		else:
			super(streamlink_ctx, self).__init__(**kwargs)

		DBG_TR_LN(self, "{}".format(DBG_TXT_ENTER))
		self._kwargs = kwargs
		self.ctx_init(url)

	def parse_args(self, args):
		DBG_TR_LN(self, "{}".format(DBG_TXT_ENTER))
		self._args = args

	def start(self, args={}):
		DBG_TR_LN(self, "{}".format(DBG_TXT_START))
		self.parse_args(args)

		self.streams_urlparse()
		self.streams_fetch()

#streamlink_mgr = streamlink_ctx()
#streamlink_mgr.release()
