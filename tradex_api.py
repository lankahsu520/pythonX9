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

		def filter_cb(jroot):
			#DBG_DB_LN("{}".format(DBG_TXT_ENTER))
			msg = "[\n\n"
			msg += f"{'idx':>3} - {'可取消狀態':<7} {'委託書編號':<7} {'預約狀態':<7} {'買/賣':<5} {'股票代碼':<6} {'委託股數':<6} {'成交股數':<6} {'取消股數':<6} {'委託價格':<6} {'成交均價':<6}\n"
			for i, item in enumerate(jroot):
				#comma = ",\n" if i < len(jroot) - 1 else ""
				comma = "\n" if i < len(jroot) - 1 else ""

				celable_str = "yes" if item['celable'] == "1" else "no"

				ord_no_str = f"{item['ord_no']}" if item['ord_no'] != "" else f"{item['pre_ord_no']}"

				ord_status_str = "預約單" if item['ord_status'] == "1" else "盤中單"

				buy_sell_str = "買" if item['buy_sell'] == "B" else "賣"

				stk_no_str = f"{item['stock_no']}"

				#qty_sign = "+" if item['buy_sell'] == "B" else "-" if item['buy_sell'] == "S" else ""
				qty_str = f"{item['org_qty_share']}"

				#mat_qty_str = f"{qty_sign}{item['mat_qty_share']}"
				mat_qty_str = f"{item['mat_qty_share']}"

				cel_qty_str = f"{item['cel_qty_share']}"

				od_price_str = f"{item['od_price']}"

				avg_price_str = f"{item['avg_price']}"

				msg += f"{i:>3} - {celable_str:<12} {ord_no_str:<12} {ord_status_str:<8} {buy_sell_str:<6} {stk_no_str:<10} {qty_str:<10} {mat_qty_str:<10} {cel_qty_str:<10} {od_price_str:<10} {avg_price_str:<10}{comma}"
			msg += "\n\n]"
			return msg

		if ( self.verbose == True ):
			JSON_IF_FORMAT(self.orders, jstyle=JSTYLE.ARRAY, filter_cb=filter_cb)
			#JSON_IF_FORMAT(self.orders, jstyle=JSTYLE.ARRAY)
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
			JSON_IF_FORMAT(self.orders_history)
		return self.orders_history

	# 成交明細
	# query_range: 0d|3d|1m|3m
	def tradex_q_transactions(self, query_range="0d"):
		self.transactions = self.trade_sdk.get_transactions(query_range)

		def filter_cb(jroot):
			#DBG_DB_LN("{}".format(DBG_TXT_ENTER))
			msg = "[\n\n"
			msg += f"{'idx':>3} - {'買/賣':<5} {'股票代碼':<6} {'成交股數':<6} {'成交均價 ':<6} {'股票名稱'}\n"
			for i, item in enumerate(jroot):
				#comma = ",\n" if i < len(jroot) - 1 else ""
				comma = "\n" if i < len(jroot) - 1 else ""

				buy_sell_str = "買" if item['buy_sell'] == "B" else "賣"

				stk_no_str = f"{item['stk_no']}"

				qty_sign = "+" if item['buy_sell'] == "B" else "-" if item['buy_sell'] == "S" else ""
				qty_str = f"{qty_sign}{item['qty']}"

				price_str = f"{item['price_avg']}"

				stk_name_str = f"{item['stk_na']}"

				msg += f"{i:>3} - {buy_sell_str:<6} {stk_no_str:<10} {qty_str:<10} {price_str:<10} {stk_name_str}{comma}"
			msg += "\n\n]"
			return msg

		if ( self.verbose == True ):
			JSON_IF_FORMAT(self.transactions, jstyle=JSTYLE.ARRAY, filter_cb=filter_cb)
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
			JSON_IF_FORMAT(self.transactions_history, jstyle=JSTYLE.ARRAY)
		return self.transactions_history

	# 交割款
	def tradex_q_settlements(self):
		self.settlements = self.trade_sdk.get_settlements()
		if ( self.verbose == True ):
			JSON_IF_FORMAT(self.settlements)
		return self.settlements

	def tradex_o_delete_qty(self, order_result, qty_share):
		self.last_delete_response = self.trade_sdk.cancel_order(order_result, qty_share)
		if ( self.verbose == True ):
			JSON_IF_FORMAT(self.last_delete_response)
		return self.last_delete_response

	def tradex_o_delete(self, order_result):
		self.last_delete_response = self.trade_sdk.cancel_order(order_result)
		if ( self.verbose == True ):
			JSON_IF_FORMAT(self.last_delete_response)
		return self.last_delete_response

	# 交易訊息
	def tradex_o_response(self):
		if ( self.verbose == True ) and ( self.last_order_response is not None ):
			JSON_IF_FORMAT(self.last_order_response)
		return self.last_order_response

	#Action
	#  Buy	"B"	買
	#  Sell	"S"	賣
	#APCode
	#  Common	"1"	整股, 張, 1 ~ 499
	#  AfterMarket	"2"	盤後定價, 張, 1 ~ 499
	#  Odd	"3"	盤後零股, 股, 1 ~ 999
	#  Emg	"4"	興櫃, 股, 1 ~ 999, 1000 ~ 499000 (超過 1000 後，最小升降單位為 1000)
	#  IntradayOdd	"5"	盤中零股, 股, 1 ~ 999
	def tradex_o_helper(self, stock_no=None, price=None, quantity=0, buy_sell=Action.Buy, ap_code=APCode.Common):
		if ( self._is_login == True ) and ( stock_no is not None ):
			order_args = {
				"stock_no": stock_no,
				"quantity": quantity,
				"buy_sell": buy_sell,
				"ap_code": ap_code,
			}

			if not price is None:
				order_args["price"] = price

			DBG_DB_LN("(order_args: {})".format(order_args))

			self.last_order = OrderObject(**order_args)

			if ( self.test_only == False ):
				self.last_order_response = self.trade_sdk.place_order( self.last_order )
			else:
				print("測試模式，未執行交易 !")
		else:
			DBG_ER_LN("{}".format("請先登入 !!!"))

		return self.tradex_o_response()

	# 整張買進
	def tradex_o_buy(self, stock_no, price, quantity):
		return self.tradex_o_helper(stock_no, price=price, quantity=quantity, buy_sell=Action.Buy, ap_code=APCode.Common)

	# 整張買進-盤後
	def tradex_o_buy_after(self, stock_no, quantity):
		return self.tradex_o_helper(stock_no, quantity=quantity, buy_sell=Action.Buy, ap_code=APCode.AfterMarket)

	# 零股買進
	def tradex_o_buy_odd(self, stock_no, price, quantity):
		return self.tradex_o_helper(stock_no, price=price, quantity=quantity, buy_sell=Action.Buy, ap_code=APCode.IntradayOdd)

	# 零股買進-盤後
	def tradex_o_buy_odd_after(self, stock_no, price, quantity):
		return self.tradex_o_helper(stock_no, price=price, quantity=quantity, buy_sell=Action.Buy, ap_code=APCode.Odd)

	# 整張賣出
	def tradex_o_sell(self, stock_no, price, quantity):
		return self.tradex_o_helper(stock_no, price=price, quantity=quantity, buy_sell=Action.Sell, ap_code=APCode.Common)

	# 整張賣出-盤後
	def tradex_o_sell_after(self, stock_no, quantity):
		return self.tradex_o_helper(stock_no, quantity=quantity, buy_sell=Action.Sell, ap_code=APCode.AfterMarket)

	# 零股賣出
	def tradex_o_sell_odd(self, stock_no, price, quantity):
		return self.tradex_o_helper(stock_no, price=price, quantity=quantity, buy_sell=Action.Sell, ap_code=APCode.IntradayOdd)

	# 零股賣出-盤後
	def tradex_o_buy_sell_after(self, stock_no, quantity):
		return self.tradex_o_helper(stock_no, quantity=quantity, buy_sell=Action.Sell, ap_code=APCode.Odd)

	def tradex_o_commit(self, action, stock_no, price, quantity, market):
		quantity_lots, quantity_shares = divmod(int(quantity), 1000)

		# 第 5 層
		print("\n========== 交易內容 ==========")
		print(f"買賣：{'買股' if action == 'b' else '賣股'}")
		print(f"代碼：{stock_no}")
		print(f"價格：{price}")
		if quantity_lots > 0 and quantity_shares > 0:
			print(f"股數：{quantity_lots} 張 {quantity_shares} 股")
		elif quantity_lots > 0:
			print(f"股數：{quantity_lots} 張")
		else:
			print(f"股數：{quantity_shares} 股")
		print(f"時段：{'盤中' if market == 'i' else '盤後'}")
		print("==============================")

		# 是否繼續
		answer = input("是否繼續執行？[y/n]：").strip().lower()

		match answer:
			case 'y':
				order = {
					"action": action,
					"market": market
				}
				match order:
					case {"action": 'b', "market": 'i'}:
							if quantity_lots > 0:
								self.tradex_o_buy(stock_no, price, quantity_lots)
							if quantity_shares > 0:
								self.tradex_o_buy_odd(stock_no, price, quantity_shares)

					case {"action": 'b', "market": 'a'}:
							if quantity_lots > 0:
								self.tradex_o_buy_after(stock_no, quantity_lots)
							if quantity_shares > 0:
								self.tradex_o_buy_odd_after(stock_no, price, quantity_shares)

					case {"action": 's', "market": 'i'}:
							if quantity_lots > 0:
								self.tradex_o_sell(stock_no, price, quantity_lots)
							if quantity_shares > 0:
								self.tradex_o_sell_odd(stock_no, price, quantity_shares)

					case {"action": 's', "market": 'a'}:
							if quantity_lots > 0:
								self.tradex_o_sell_after(stock_no, quantity_lots)
							if quantity_shares > 0:
								self.tradex_o_sell_odd_after(stock_no, price, quantity_shares)

					case _:
						DBG_IF_LN("輸入錯誤 !!!")

			case _:
				DBG_IF_LN("取消交易 !")


	#**************************************************
	# 查詢
	#**************************************************
	# 交易額度及權限
	def tradex_q_tradelimit(self):
		self.tradelimit = self.trade_sdk.get_trade_status()
		if ( self.verbose == True ):
			JSON_IF_FORMAT(self.tradelimit)
		return self.tradelimit

	# 銀行餘額
	def tradex_q_balance(self):
		self.balance = self.trade_sdk.get_balance()
		if ( self.verbose == True ):
			JSON_IF_FORMAT(self.balance)
		return self.balance

	# 庫存明細
	def tradex_q_inventories(self):
		self.inventories = self.trade_sdk.get_inventories()
		if ( self.verbose == True ):
			JSON_IF_FORMAT(self.inventories, jstyle=JSTYLE.ARRAY)
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

		self._is_login = True

	# 重設密碼
	def tradex_password(self):
		self.trade_sdk.reset_password()

	# 憑證資訊
	def tradex_q_certinfo(self):
		self.certinfo = self.trade_sdk.certinfo()
		if ( self.verbose == True ):
			JSON_IF_FORMAT(self.certinfo)
		return self.certinfo

	# 金鑰資訊
	def tradex_q_apiKey(self):
		self.apiKey = self.trade_sdk.get_key_info()
		if ( self.verbose == True ):
			JSON_IF_FORMAT(self.apiKey)
		return self.apiKey


	#**************************************************
	# websocket
	#**************************************************
	def threadx_websocket(self):
		# 註冊當 websocket 發生錯誤時的 callback
		@self.trade_sdk.on('error')
		def on_error(err):
			DBG_ER_LN("{}".format( err ))

		# 註冊接收委託回報的 callback
		@self.trade_sdk.on('order')
		def on_order(data):
			DBG_IF_LN("{}".format( data ))

		# 註冊接收成交回報的 callback
		@self.trade_sdk.on('dealt')
		def on_dealt(data):
			DBG_WN_LN("{}".format( data ))

		# 註冊關閉回報的 callback
		@self.trade_sdk.on('close')
		def on_close(ws, close_status_code, close_msg):
			DBG_WN_LN("(close_status_code: {}, close_msg: {})".format( close_status_code, close_msg ))

		self.trade_sdk.connect_websocket()

	#**************************************************
	# thread
	#**************************************************
	def threadx_handler(self):
		#DBG_IF_LN("{}".format(DBG_TXT_ENTER))
		self.threadx_set_inloop(1)
		self.threadx_websocket()
		while ( self.is_quit == 0 ):
			self.threadx_sleep(1)
		self.threadx_set_inloop(0)
		DBG_WN_LN("{}".format(DBG_TXT_BYE_BYE))

	def release(self):
		if ( self.is_quit == 0 ):
			self.is_quit = 1
			if ( self.threadx_inloop() == 1 ):
				self.threadx_wakeup()
			self.trade_sdk.close_websocket()
			#self.trade_sdk.logout()
			self.threadx_join()
			DBG_DB_LN("{}".format(DBG_TXT_DONE))

	def ctx_init(self):
		DBG_DB_LN("{}".format(DBG_TXT_ENTER))

		self.last_order = None
		self.last_order_response = None

		self.trade_sdk = None
		self._is_login = False

	def __init__(self, **kwargs):
		if ( isPYTHON(PYTHON_V3) ):
			super().__init__(**kwargs)
		else:
			super(tradex_ctx, self).__init__(**kwargs)

		DBG_TR_LN("{}".format(DBG_TXT_ENTER))
		self._kwargs = kwargs
		self.ctx_init()

	def parse_args(self, args):
		DBG_TR_LN("{}".format(DBG_TXT_ENTER))
		self._args = args
		self.verbose = args["verbose"]
		self.config_ini = args["config_ini"]
		self.test_only = args["test_only"]

	def start(self, args={}):
		DBG_TR_LN("{}".format(DBG_TXT_START))
		self.parse_args(args)
		self.tradex_login()
		self.threadx_init()

