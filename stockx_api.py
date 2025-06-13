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

import pandas as pd
import requests, json
from time import sleep
import datetime
from pathlib import Path
from calendar import monthrange

class stockx_ctx(pythonX9):

	def fetch_stock_month(self, stock_no, year, month):
		date = f"{year}{month:02d}01"
		#https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20250613&stockNo=0050
		url = f'https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date={date}&stockNo={stock_no}'
		res = requests.get(url)
		res.encoding = 'utf-8'
		data = res.json()
		if data['stat'] != 'OK':
			return pd.DataFrame()

		df = pd.DataFrame(data['data'], columns=data['fields'])

		# 民國年轉西元年（例如 113/01/02 → 2024-01-02）
		df['日期'] = df['日期'].apply(lambda x: f"{1911 + int(x.split('/')[0])}-{x.split('/')[1]}-{x.split('/')[2]}")
		df['日期'] = pd.to_datetime(df['日期'], format="%Y-%m-%d")

		df['收盤價'] = pd.to_numeric(df['收盤價'].str.replace(',', ''), errors='coerce')
		return df[['日期', '收盤價']].rename(columns={'日期': 'DATE', '收盤價': 'CLOSEYEST'})

	def fetch_helper(self):
		all_data = pd.DataFrame()
		print("[{}] ".format(self.stock_no), end="", flush=True)
		for y in self.date_range:
			if ( self.is_quit == 1 ):
				break
			for m in range(1, 13):
					if (y == self.NOW_YEAR and m > self.NOW_MONTH):  # 最多到 6 月
							break
					df = self.fetch_stock_month(self.stock_no, y, m)
					all_data = pd.concat([all_data, df])
					print(".", end="", flush=True)
					sleep(0.5)  # 避免被擋，放慢一點
					if ( self.is_quit == 1 ):
						break
		all_data = all_data.sort_values(by='DATE').reset_index(drop=True)
		if ( self.is_quit == 1 ):
			print(" Quit !!!", flush=True)
		else:
			print(" Completed !!!", flush=True)
		return all_data

	def buy_prices_helper(self):
		self.buy_return = []
		df = self.stock_history

		end_date = pd.Timestamp.today() - pd.Timedelta(days=1)
		short_years_ago = pd.Timestamp.today() - pd.DateOffset(years=self.buy_short)
		medium_years_ago = pd.Timestamp.today() - pd.DateOffset(years=self.buy_medium)
		long_years_ago = pd.Timestamp.today() - pd.DateOffset(years=self.buy_long)

		for day in range(1, 32):  # 每月 1～31 日
			buy_prices_short = []
			buy_prices_medium = []
			buy_prices_long = []

			# --- short ---
			if ( 0 == 1 ):
				for date in pd.date_range(short_years_ago, end_date, freq="MS"):
					year, month = date.year, date.month
					max_day = monthrange(year, month)[1]
					if day <= max_day:
						try_day = pd.Timestamp(year=year, month=month, day=day)

						# 找 try_day 之前的最後一筆記錄（前一筆）
						past_day = df[df["DATE"] < try_day]
						if not past_day.empty:
							prev_record = past_day.iloc[-1]
							DBG_IF_LN(self, "({}, day: {}, try_day: {}, prev_record: {}, {})".format(short_years_ago, day, try_day.strftime("%Y-%m-%d"), prev_record["DATE"].strftime("%Y-%m-%d"), prev_record["CLOSEYEST"]))
							buy_prices_short.append(prev_record["CLOSEYEST"])

			# --- long ---
			for date in pd.date_range(long_years_ago, end_date, freq="MS"):
				year, month = date.year, date.month
				max_day = monthrange(year, month)[1]
				if day <= max_day:
					try_day = pd.Timestamp(year=year, month=month, day=day)

					# 找 try_day 之前的最後一筆記錄（前一筆）
					past_day = df[df["DATE"] < try_day]
					if not past_day.empty:
						prev_record = past_day.iloc[-1]
						#DBG_IF_LN(self, "(day: {}, try_day: {}, prev_record: {}, {})".format(day, try_day.strftime("%Y-%m-%d"), prev_record["DATE"].strftime("%Y-%m-%d"), prev_record["CLOSEYEST"]))
						buy_prices_long.append(prev_record["CLOSEYEST"])

						# --- short ---
						if (try_day>=short_years_ago):
							#DBG_IF_LN(self, "(day: {}, try_day: {}, prev_record: {}, {})".format(day, try_day.strftime("%Y-%m-%d"), prev_record["DATE"].strftime("%Y-%m-%d"), prev_record["CLOSEYEST"]))
							buy_prices_short.append(prev_record["CLOSEYEST"])

						# --- medium ---
						if (try_day>=medium_years_ago):
							#DBG_IF_LN(self, "(day: {}, try_day: {}, prev_record: {}, {})".format(day, try_day.strftime("%Y-%m-%d"), prev_record["DATE"].strftime("%Y-%m-%d"), prev_record["CLOSEYEST"]))
							buy_prices_medium.append(prev_record["CLOSEYEST"])

			# --- 報酬率計算 ---
			def calc_return(prices, final_price):
				if not prices or final_price is None:
						return {
								"return_pct": None,
								"avg_price": None,
								"count": 0
						}

				avg_price = sum(prices) / len(prices)
				return_pct = round((final_price - avg_price) / avg_price * 100, 2)

				return {
						"return_pct": return_pct,
						"avg_price": round(avg_price, 4),
						"count": len(prices)
				}

			#final_price = df[df["DATE"] == end_date]["CLOSEYEST"].values[0]
			final_row = df[df["DATE"] <= end_date].sort_values("DATE", ascending=False).head(1)
			if not final_row.empty:
				final_price = final_row.iloc[0]["CLOSEYEST"]
			else:
				final_price = None  # 或 raise 錯誤 / 給預設值

			self.buy_return.append({
					"Day": day
					,"Short": calc_return(buy_prices_short, final_price)
					,"Medium": calc_return(buy_prices_medium, final_price)
					,"Long": calc_return(buy_prices_long, final_price)
			})
			self.final_price = final_price

	def buy_return_display_on_screen(self):
		# --- 匯出結果 ---
		report_df = pd.DataFrame(self.buy_return)
		#report_df["Day"] = report_df["Day"].astype(int)
		#print(report_df)
		#print(report_df.dtypes)
		print("Day {}-Year                 {}-Year                 {}-Year                 Sum".format(self.buy_short, self.buy_medium, self.buy_long) )
		print(f"{'':<4}{'(%)':<6}{'count':<7}{'average':<10}{'(%)':<6}{'count':<7}{'average':<10}{'(%)':<6}{'count':<7}{'average':<10}(%)")
		for idx, row in report_df.iterrows():
			print("{:<4}".format( int(row['Day']) ), end="")
			print("{:<6}{:<7}{:<10.02f}".format( row['Short']['return_pct'], row['Short']['count'], row['Short']['avg_price'] ), end="")
			print("{:<6}{:<7}{:<10.02f}".format( row['Medium']['return_pct'], row['Medium']['count'], row['Medium']['avg_price'] ), end="")
			print("{:<6}{:<7}{:<10.02f}".format( row['Long']['return_pct'], row['Long']['count'], row['Long']['avg_price'] ), end="" )
			print("{:<10.02f}".format( row['Short']['return_pct'] + row['Medium']['return_pct'] + row['Long']['return_pct'] ) )
			#print("{:<4}{:<6}{:<7}{:<10.02f}{:<6}{:<7}{:<10.02f}".format( int(row['Day']), row['Short']['return_pct'], row['Short']['count'], row['Short']['avg_price'], row['Medium']['return_pct'], row['Medium']['count'], row['Medium']['avg_price']))
			#print("[{}] ".format(self.stock_no), end="", flush=True)

		print("(stock_no: {}, final_price: {})".format( self.stock_no, self.final_price ))

	def history_load_from_csv(self):
		print("Found !!! ({}), Loading ...".format(self.history_filename))
		self.stock_history = pd.read_csv(self.history_filename, encoding="utf-8-sig")
		self.stock_history["DATE"] = pd.to_datetime(self.stock_history["DATE"])
		self.stock_history["CLOSEYEST"] = pd.to_numeric(self.stock_history["CLOSEYEST"], errors="coerce")
		self.stock_history = self.stock_history.sort_values(by='DATE').reset_index(drop=True)

	def history_exists(self):
		return Path(self.history_filename).exists()

	def history_save_to_csv(self):
		# 儲存 CSV（可選）
		if ( self.is_new == True ):
			self.stock_history.to_csv(self.history_filename, index=False, encoding="utf-8-sig")

	def history_display_on_screen(self):
		df = self.stock_history
		# 自訂格式化輸出
		print("{:<12} {:<14}".format( "DATE", "CLOSEYEST") )
		for idx, row in df.iterrows():
			print("{:<12} {:<14.2f}".format( row['DATE'].strftime('%Y-%m-%d'), row['CLOSEYEST']) )

	def release(self):
		if ( self.is_quit == 0 ):
			self.is_quit = 1
			DBG_DB_LN(self, "{}".format(DBG_TXT_DONE))

	def ctx_init(self):
		DBG_DB_LN(self, "{}".format(DBG_TXT_ENTER))

		self.NOW_t = datetime.date.today()
		self.NOW_YEAR = self.NOW_t.year
		self.NOW_MONTH = self.NOW_t.month

	def __init__(self, **kwargs):
		if ( isPYTHON(PYTHON_V3) ):
			super().__init__(**kwargs)
		else:
			super(stockx_ctx, self).__init__(**kwargs)

		self._kwargs = kwargs
		self.ctx_init()

	def parse_args(self, args):
		DBG_TR_LN(self, "{}".format(DBG_TXT_ENTER))
		self._args = args

		self.stock_no = args["stock_no"]
		self.date_range = args["date_range"]
		self.renew = args["renew"]
		self.buy_short = 1
		self.buy_medium = 3
		self.buy_long = 5

		self.history_folder = f"./stock"
		self.history_filename = f"{self.history_folder}/{self.stock_no}_history.csv"

	def start(self, args={}):
		DBG_TR_LN(self, "{}".format(DBG_TXT_START))
		self.parse_args(args)
		if ( self.renew == False) and ( self.history_exists() ):
			self.history_load_from_csv()
			self.is_new = False
		else:
			self.stock_history = self.fetch_helper()
			self.is_new = True

		#self.buy_prices_helper()

#stockx_mgr = stockx_ctx("HelloStockX")
#stockx_mgr.start()
#stockx_mgr.display_on_screen()
#stockx_mgr.save_to_csv()

