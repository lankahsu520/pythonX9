# -*- coding: utf-8 -*-

#import os, sys, errno, getopt, signal, time, io
#from time import sleep
from pythonX9 import *

from _thread import start_new_thread
#import platform
import subprocess # os_gpu_temperature
# sudo pip3 install psutil
# https://psutil.readthedocs.io/en/latest/
import psutil # cpu_usage

class sysinfo_ctx(pythonX9):
	def cpu_count(self):
		cpu_c = psutil.cpu_count()
		return cpu_c

	def cpu_num(self):
		if ( isOS(OS_WINDOWS) ):
			cpu_n = psutil.Process().cpu_percent(interval=1)
		else:
			cpu_n = psutil.Process().cpu_num()
		return cpu_n

	def cpu_freq(self):
		cpu_f = psutil.cpu_freq()
		return cpu_f

	def cpu_temperature(self):
		tempFile = open( "/sys/class/thermal/thermal_zone0/temp" )
		cpu_temp = tempFile.read()
		tempFile.close()
		return float(cpu_temp)/1000
		# Uncomment the next line if you want the temp in Fahrenheit
		# return float(1.8*cpu_temp)+32

	def os_gpu_temperature(self):
		gpu_temp = subprocess.getoutput( '/opt/vc/bin/vcgencmd measure_temp' ).replace( 'temp=', '' ).replace( '\'C', '' )
		return  float(gpu_temp)
	# Uncomment the next line if you want the temp in Fahrenheit
	# return float(1.8* gpu_temp)+32

	def disk_usage(self):
		disk_u = psutil.disk_usage("/").percent
		#disk_u = str(disk_u)+"%"
		return disk_u

	def cpu_usage(self):
		cpu_p = psutil.cpu_percent(interval=1, percpu=True)
		return cpu_p

	def cpu_loadavg(self):
		if hasattr(psutil, "getloadavg"):
			cpu_l = psutil.getloadavg()
		else:
			cpu_l = (0.0, 0.0, 0.0)
		return cpu_l

	def os_net_ipaddrs(self):
		#sudo pip3 install ifaddr
		import ifaddr
		adapters = ifaddr.get_adapters()
		for adapter in adapters:
			for ip in adapter.ips:
				DBG_DB_LN(self, "{} - {}/{}".format(adapter.nice_name, ip.ip, ip.network_prefix))

	def os_net_info(self):
		net_in = psutil.net_io_counters().bytes_recv/1024/1024
		net_in = round(net_in, 2)
		net_out = psutil.net_io_counters().bytes_sent/1024/1024
		net_out = round(net_out, 2)
		net = str(net_in)+" MB / "+str(net_out)+" MB"
		return net

	def os_net_speed(self):
		s1 = psutil.net_io_counters().bytes_recv
		time.sleep(1)
		s2 = psutil.net_io_counters().bytes_recv
		result = s2 - s1
		return str('%.2f'%(result / 1024)) + " KB/s"

	def secs2hours(self, sbattery):
		secsleft = sbattery.secsleft

		if ( sbattery.power_plugged ):
			return ("{:02d}:{:02d}:{:02d}").format(0, 0, 0)
		else:
			mm, ss = divmod(secsleft, 60)
			hh, mm = divmod(mm, 60)
			return ("{:02d}:{:02d}:{:02d}").format(hh, mm, ss)

	def sysinfo_show_watch(self):
		DBG_DB_LN(self, "--------------------------------------------------------------------------------")
		#DBG_DB_LN(self, "(cpu_temperature: {})".format(self.cpu_temperature()) )
		#DBG_DB_LN(self, "(os_gpu_temperature: {})".format(self.os_gpu_temperature()) )
		DBG_DB_LN(self, "(cpu_usage: {})".format(self.cpu_usage()) )
		DBG_DB_LN(self, "(cpu_loadavg: {})".format(self.cpu_loadavg()) )
		DBG_DB_LN(self, "(cpu_count: {})".format(self.cpu_count()) )
		DBG_DB_LN(self, "(cpu_num: {})".format(self.cpu_num()) )
		scpufreq = self.cpu_freq()
		DBG_DB_LN(self, "(cpu_freq: {}, min: {}, max: {})".format(scpufreq.current, scpufreq.min, scpufreq.max ) )
		#DBG_DB_LN(self, "(cpu_temperature: {})".format( psutil.sensors_temperatures() ) )
		if hasattr(psutil, "sensors_temperatures"):
			temps = psutil.sensors_temperatures()
			for name, entries in temps.items():
				for entry in entries:
					DBG_DB_LN(self, "({}: {} °C, high: {} °C, critical: {} °C)".format( entry.label or name, entry.current, entry.high, entry.critical ) )
		else:
			DBG_DB_LN(self, "(temperatures: None)" )
		DBG_DB_LN(self, "(disk_usage: {} %)".format(self.disk_usage()) )
		vmem = psutil.virtual_memory()
		DBG_DB_LN(self, "(mem_total: {} bytes, mem_usage: {} %)".format(vmem.total, vmem.percent) )
		if hasattr(psutil, "sensors_battery"):
			sbattery = psutil.sensors_battery()
			if hasattr(sbattery, "percent"):
				DBG_DB_LN(self, "(battery: {} %, secsleft: {}, AC: {})".format( sbattery.percent, self.secs2hours(sbattery), sbattery.power_plugged) )
			else:
				DBG_DB_LN(self, "(battery: None)" )
		else:
			DBG_DB_LN(self, "(battery: None)" )
		if hasattr(psutil, "sensors_fans"):
			fans = psutil.sensors_fans()
			DBG_DB_LN(self, "(fans: {})".format( fans ) )
		else:
			DBG_DB_LN(self, "(fans: None)" )

	def syinfo_show_uname(self):
		# 3.8 not support dist
		#DBG_IF_LN(self, "(os_dist: {})".format( platform.dist() ) )
		#DBG_IF_LN(self, "(linux_distribution: {})".format( platform.linux_distribution() ) )
		DBG_IF_LN(self, "(os_platform: {})".format( platform.platform() ) )
		DBG_IF_LN(self, "(os_system: {})".format( platform.system() ) )
		DBG_IF_LN(self, "(os_node: {})".format( platform.node() ) )
		DBG_IF_LN(self, "(os_release: {})".format( platform.release() ) )
		DBG_IF_LN(self, "(os_version: {})".format( platform.version() ) )
		DBG_IF_LN(self, "(os_machine: {})".format( platform.machine() ) )
		DBG_IF_LN(self, "(os_processor: {})".format( platform.processor() ) )
		uname_result = platform.uname()
		DBG_IF_LN(self, "(uname_result: {})".format( uname_result ) )
		#DBG_IF_LN(self, "(mac_ver: {})".format( platform.mac_ver() ) )

	def sysinfo_show(self):
		DBG_IF_LN(self, "(Python version: {})".format( sys.version.split('\n')[0] ) )
		self.syinfo_show_uname()
		#DBG_IF_LN(self, "(os_net_info: {})".format(self.os_net_info()) )
		#DBG_IF_LN(self, "(os_net_speed: {})".format(self.os_net_speed()) )

	def thread_handler(self):
		#DBG_IF_LN(self, "enter")
		self.os_net_ipaddrs()
		sleep(1)
		while ( self.is_quit ==0 ):
			self.sysinfo_show_watch()
			sleep(self.interval)

		DBG_IF_LN(self, "exit")

	def thread_init(self):
		start_new_thread(self.thread_handler, ())

	def keyboard_recv(self):
		DBG_IF_LN(self, "press q to quit the loop ...")

		k='\x00'
		while ( self.is_quit == 0 ):
			k = self.inkey()
			#DBG_IF_LN(self, "(k:{})".format(k))
			if k=='\x0d': # enter
				self.sysinfo_show()
			elif k=='\x71': # q
				self.release()
				break;
			DBG_IF_LN(self, "press q to quit the loop ...")

	def release(self):
		if ( self.is_quit == 0 ):
			self.is_quit = 1
			DBG_WN_LN(self, "{}".format(DBG_TXT_BYE_BYE))

	def sysinfo_init(self):
		DBG_DB_LN(self, "{}".format(DBG_TXT_INIT))
		self.interval = 30

	def __init__(self, **kwargs):
		if ( isPYTHON(PYTHON_V3) ):
			super().__init__(**kwargs)
		else:
			super(sysinfo_ctx, self).__init__(**kwargs)

		DBG_TR_LN(self, "{}".format(DBG_TXT_ENTER))
		self._kwargs = kwargs
		self.sysinfo_init()

	def parse_args(self, args):
		DBG_TR_LN(self, "{}".format(DBG_TXT_ENTER))
		self._args = args
		self.interval = args["interval"]
		self.keyboard = args["keyboard"]

	def start(self, args={"keyboard": 0, "interval": 10}):
		DBG_TR_LN(self, "{}".format(DBG_TXT_START))
		self.parse_args(args)
		if (self.keyboard==1):
			self.thread_init()
			self.keyboard_recv()

#sysinfo_mgr = sysinfo_ctx(dbg_more=DBG_LVL_TRACE)
#sysinfo_mgr.start(args={"keyboard": 1, "interval": 5})
##sysinfo_mgr.keyboard_recv()
#sysinfo_mgr.release()
