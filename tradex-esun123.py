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

from tradex_api import *

appX_list = []
is_quit = 0
is_release = 0
argsX = {
	"config_ini": '/work/esun/config.ini'
	,"verbose": True
}

def app_quit_get():
	return is_quit

def app_quit_set(mode):
	global is_quit
	is_quit=mode

def app_start():
	argsX_dump(argsX)

	tradex_mgr = tradex_ctx(dbg_lvl=DBG_LVL_INFO)
	tradex_mgr.start(argsX)

	#**************************************************
	# 交易下單
	#**************************************************
	# 委託紀錄
	#tradex_mgr.tradex_q_orders()

	# 委託歷史紀錄
	# 預設前 2日的歷史紀錄
	#tradex_mgr.tradex_q_orders_history()
	# 查詢 2026-09-09 ~ 2026-09-10 的歷史紀錄
	#tradex_mgr.tradex_q_orders_history("2026-09-09", "2026-09-10")

	# 成交明細
	#tradex_mgr.tradex_q_transactions(query_range="0d")

	# 成交明細（依指定日期）
	# 查詢 2026-09-09 ~ 2026-09-10 的成交紀錄
	#tradex_mgr.tradex_q_transactions_history("2026-09-09", "2026-09-10")

	# 交割款
	#tradex_mgr.tradex_q_settlements()

	# 交易訊息
	#tradex_mgr.tradex_o_response()

	# 整張買進 0050, 109 元 * 1張
	#tradex_mgr.tradex_o_buy("0050", 109, 1)
	# 整張買進 00919, 32.34 元 * 1張
	#tradex_mgr.tradex_o_buy("00919", 32.34, 1)
	# 零股買進 00919, 32.32 元 * 837股
	#tradex_mgr.tradex_o_buy_odd("00919", 32.32, 837)


	#**************************************************
	# 查詢
	#**************************************************
	# 交易額度及權限
	#tradex_mgr.tradex_q_tradelimit()

	# 銀行餘額
	tradex_mgr.tradex_q_balance()
	#print("(tradex_mgr.balance: {})\r".format( tradex_mgr.balance ))

	# 庫存明細
	#tradex_mgr.tradex_q_inventories()


	#**************************************************
	# 帳號
	#**************************************************
	# 重設密碼
	#tradex_mgr.tradex_password()

	# 憑證資訊
	#tradex_mgr.tradex_q_certinfo()

	# 金鑰資訊
	#tradex_mgr.tradex_q_apiKey()

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
