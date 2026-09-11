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

from configparser import ConfigParser
from esun_trade.sdk import SDK
from esun_trade.order import OrderObject
from esun_trade.constant import (APCode, Trade, PriceFlag, BSFlag, Action)

from datetime import date, timedelta

#import os, sys, errno, getopt, signal, time, io
#from time import sleep
from pythonX9 import *
from threadx_api import *

class tradex_ctx(pythonX9, threadx_ctx):

	#**************************************************
	# 交易下單
	#**************************************************
	# 委託紀錄
	def tradex_q_orders(self):
		self.orders = self.trade_sdk.get_order_results()
		if ( self.verbose == True ):
			JSON_FORMAT( self.orders )
		return self.orders

	# 委託歷史紀錄
	def tradex_q_orders_history(self, start_date_str=None, end_date_str=None):
		if end_date_str is None:
			end_date = date.today() - timedelta(days=1)
			end_date_str = end_date.strftime("%Y-%m-%d")

		if start_date_str is None:
			start_date = date.today() - timedelta(days=2)
			start_date_str = start_date.strftime("%Y-%m-%d")

		DBG_IF_LN("( {} ~ {} )".format(start_date_str, end_date_str))

		self.orders_history = self.trade_sdk.get_order_results_by_date(start_date_str, end_date_str)
		if ( self.verbose == True ):
			JSON_FORMAT( self.orders_history )
		return self.orders_history

	# 成交明細
	def tradex_q_transactions(self, query_range="0d"):
		self.transactions = self.trade_sdk.get_transactions(query_range)
		if ( self.verbose == True ):
			JSON_FORMAT( self.transactions )
		return self.transactions

	# 成交明細（依指定日期）
	def tradex_q_transactions_history(self, start_date_str=None, end_date_str=None):
		if end_date_str is None:
			end_date = date.today() - timedelta(days=1)
			end_date_str = end_date.strftime("%Y-%m-%d")

		if start_date_str is None:
			start_date = date.today() - timedelta(days=2)
			start_date_str = start_date.strftime("%Y-%m-%d")

		DBG_IF_LN("( {} ~ {} )".format(start_date_str, end_date_str))

		self.transactions_history = self.trade_sdk.get_transactions_by_date(start_date_str, end_date_str)
		if ( self.verbose == True ):
			JSON_FORMAT( self.transactions_history )
		return self.transactions_history

	# 交割款
	def tradex_q_settlements(self):
		self.settlements = self.trade_sdk.get_settlements()
		if ( self.verbose == True ):
			JSON_FORMAT( self.settlements )
		return self.settlements

	# 交易訊息
	def tradex_o_response(self):
		if ( self.verbose == True ):
			JSON_FORMAT( self.trade_sdk.last_order )
		return self.trade_sdk.last_order

	#Action
	#  Buy	"B"	買
	#  Sell	"S"	賣
	#APCode
	#  Common	"1"	整股, 張, 1 ~ 499
	#  AfterMarket	"2"	盤後定價, 張, 1 ~ 499
	#  Odd	"3"	盤後零股, 股, 1 ~ 999
	#  Emg	"4"	興櫃, 股, 1 ~ 999, 1000 ~ 499000 (超過 1000 後，最小升降單位為 1000)
	#  IntradayOdd	"5"	盤中零股, 股, 1 ~ 999
	def tradex_o_helper(self, stock_no, price, quantity, buy_sell, ap_code):
		self.trade_sdk.last_cmd = OrderObject(
																																								stock_no = stock_no,
																																								price = price,
																																								quantity = quantity,
																																								buy_sell = buy_sell,
																																								ap_code = ap_code,
																																								)
		self.trade_sdk.last_order = self.trade_sdk.place_order( self.trade_sdk.last_cmd )
		return self.tradex_o_response()

	# 整張買進
	def tradex_o_buy(self, stock_no, price, quantity):
		return self.tradex_o_helper(stock_no, price, quantity, Action.Buy, APCode.Common)

	# 整張買進-盤後
	def tradex_o_buy_after(self, stock_no, price, quantity):
		return self.tradex_o_helper(stock_no, price, quantity, Action.Buy, APCode.AfterMarket)

	# 零股買進
	def tradex_o_buy_odd(self, stock_no, price, quantity):
		return self.tradex_o_helper(stock_no, price, quantity, Action.Buy, APCode.IntradayOdd)

	# 零股買進-盤後
	def tradex_o_buy_odd_after(self, stock_no, price, quantity):
		return self.tradex_o_helper(stock_no, price, quantity, Action.Buy, APCode.Odd)

	# 整張賣出
	def tradex_o_buy(self, stock_no, price, quantity):
		return self.tradex_o_helper(stock_no, price, quantity, Action.Sell, APCode.Common)

	# 整張賣出-盤後
	def tradex_o_buy_after(self, stock_no, price, quantity):
		return self.tradex_o_helper(stock_no, price, quantity, Action.Sell, APCode.AfterMarket)

	# 零股賣出
	def tradex_o_buy_odd(self, stock_no, price, quantity):
		return self.tradex_o_helper(stock_no, price, quantity, Action.Sell, APCode.IntradayOdd)

	# 零股賣出-盤後
	def tradex_o_buy_odd_after(self, stock_no, price, quantity):
		return self.tradex_o_helper(stock_no, price, quantity, Action.Sell, APCode.Odd)


	#**************************************************
	# 查詢
	#**************************************************
	# 交易額度及權限
	def tradex_q_tradelimit(self):
		self.tradelimit = self.trade_sdk.get_trade_status()
		if ( self.verbose == True ):
			JSON_FORMAT(self.tradelimit)
		return self.tradelimit

	# 銀行餘額
	def tradex_q_balance(self):
		self.balance = self.trade_sdk.get_balance()
		if ( self.verbose == True ):
			JSON_FORMAT(self.balance)
		return self.balance

	# 庫存明細
	def tradex_q_inventories(self):
		self.inventories = self.trade_sdk.get_inventories()
		if ( self.verbose == True ):
			JSON_FORMAT(self.inventories)
		return self.inventories


	#**************************************************
	# 帳號
	#**************************************************
	# 登入
	def tradex_login(self):
		# 讀取設定檔
		self.config = ConfigParser()
		self.config.read(self.config_ini)
		# 登入
		self.trade_sdk = SDK(self.config)
		self.trade_sdk.login()

	# 重設密碼
	def tradex_password(self):
		self.trade_sdk.reset_password()

	# 憑證資訊
	def tradex_q_certinfo(self):
		self.certinfo = self.trade_sdk.certinfo()
		if ( self.verbose == True ):
			JSON_FORMAT( self.certinfo )
		return self.certinfo

	# 金鑰資訊
	def tradex_q_apiKey(self):
		self.apiKey = self.trade_sdk.get_key_info()
		if ( self.verbose == True ):
			JSON_FORMAT( self.apiKey )
		return self.apiKey

	def release(self):
		if ( self.is_quit == 0 ):
			self.is_quit = 1
			DBG_DB_LN(self, "{}".format(DBG_TXT_DONE))

	def ctx_init(self):
		DBG_DB_LN(self, "{}".format(DBG_TXT_ENTER))

	def __init__(self, **kwargs):
		if ( isPYTHON(PYTHON_V3) ):
			super().__init__(**kwargs)
		else:
			super(tradex_ctx, self).__init__(**kwargs)

		self._kwargs = kwargs
		self.ctx_init()

	def parse_args(self, args):
		DBG_TR_LN(self, "{}".format(DBG_TXT_ENTER))
		self._args = args
		self.verbose = args["verbose"]
		self.config_ini = args["config_ini"]

	def start(self, args={}):
		DBG_TR_LN(self, "{}".format(DBG_TXT_START))
		self.parse_args(args)

		self.tradex_login()
