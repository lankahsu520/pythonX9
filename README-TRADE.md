# 證劵交易 API

# 1. Overview

> 主要是透過證劵商提供的交易 API 進行交易，來讓個人的交易更加靈活，

>目前很多證劵商提供相關的交易 API，雖然目的都是操作股票交易，但是還是會存在些許的差異。
>
>文件往往是成敗的關鍵，人的一生能浪費多少時間在這些文件裏，於是想透過再次包裝，提供簡單化的介面，造福大眾。

# 2. Depend on

## 2.1. [玉山證劵交易 API](https://www.esunsec.com.tw/trading-platforms/api-trading/)

### 2.1.1. [申請流程](https://www.esunsec.com.tw/trading-platforms/api-trading/docs/prerequisites)

```bash
$ pip install esun_trade-2.2.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
```

#### A. 申請使用交易 API 服務

```mermaid
flowchart LR

1.1[申請憑證] --> 1.2[簽署同意書] --> 1.3[交易API申請完成通知 email] --> 1.4[等待審核]

```

#### B. 進行模擬測試

> [API 模擬金鑰](https://esuntradingapi.esunsec.com.tw/keys/apikey/SimulationAPIKeyManagement)
>
> 取得 config.simulation.ini (設定檔) & XXXXXXXXXX_XXXXXXXX.p12 (憑證)

> [完成模擬下單](https://www.esunsec.com.tw/trading-platforms/api-trading/docs/prerequisites#完成模擬下單)

```mermaid
flowchart LR

2.1[交易API申請完成通知 email] --> 2.2[申請模擬環境金鑰] --> 2.3[完成模擬下單]
```

#### C. 取得正式金鑰

> [API 正式金鑰](https://esuntradingapi.esunsec.com.tw/keys/apikey/APIKeyManagement)
>
> 取得 config.ini (設定檔) & XXXXXXXXXX_XXXXXXXX.p12 (憑證)

```mermaid
flowchart LR

3.1[交易API正式金鑰申請通知 email] --> 3.2[申請正式金鑰]
```

#### D. 進行正式交易

> 取得正式金鑰後，就可以用原本的程式進行交易或是查詢，請參考[完成模擬下單](https://www.esunsec.com.tw/trading-platforms/api-trading/docs/prerequisites/#完成模擬下單)。

## 2.2. 國泰證劵

# 3. Current Status

> 目前只針對 "玉山證劵交易 API" 進行交易和查詢。

- [x] ####  玉山證劵

```bash
# 新增 close_websocket
$ vi ~/.local/lib/python3.12/site-packages/esun_trade/websocket.py
    def close_websocket(self):
        self.__ws.close()
        self.__ws = None
# 新增 close_websocket
$ vi ~/.local/lib/python3.12/site-packages/esun_trade/sdk.py
    def close_websocket(self):
        self.__wsHandler.close_websocket()
```

- [ ] #### ~~國泰證劵（20260915 目前沒有提供）~~

# 4. Build

# 5. Example or Usage

## - tradex-esun123-sample.py - 玉山證劵模擬交易範例

> 這是官方的交易範例

## - tradex-esun123.py - 玉山證劵交易範例

> -t : 單純測式流程，不會下單 

```bash
$ ./tradex-esun123.py  -d3 -t
[3096/140007269668672] pythonX9.py|argsX_dump:0057 - {'config_ini': '/work/esun/config.ini', 'verbose': True, 'test_only': True}
[3096/140007269668672] tradex_api.py|ctx_init:0283 - Enter ...

主選單-銀行餘額 [b]、庫存明細 [i]、交易額度 [l]、交易下單 [o]、委託紀錄 [r]、成交明細 [t]、離開 [q]： b
[3096/140007269668672] tradex_api.py|tradex_q_balance:0234 - {
  "available_balance": 3389949,
  "exchange_balance": 0,
  "stock_pre_save_amount": 0,
  "is_latest_data": true,
  "updated_at": 1789425864
}

主選單-銀行餘額 [b]、庫存明細 [i]、交易額度 [l]、交易下單 [o]、委託紀錄 [r]、成交明細 [t]、離開 [q]：q
[3096/140007269668672] tradex-esun123.py|main:0280 - Bye-Bye !!! (app_quit_get: 1)

```

# 6. Documentation

## 6.1. 帳號

### 6.2.1. 登入

| 名稱           | 描述     |
| -------------- | -------- |
| tradex_login() | 登入帳號 |

| 證劵商 | API                                                          | 描述 |
| ------ | ------------------------------------------------------------ | ---- |
| 玉山   | [login()](https://www.esunsec.com.tw/trading-platforms/api-trading/docs/trading/reference/python#登入-login) |      |
| 國泰   |                                                              |      |

- #### Input

> None

- #### Response

> None

### 6.2.2. 重設密碼

| 名稱              | 描述     |
| ----------------- | -------- |
| tradex_password() | 重設密碼 |

| 證劵商 | API                                                          | 描述                                                         |
| ------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 玉山   | [reset_password()](https://www.esunsec.com.tw/trading-platforms/api-trading/docs/trading/reference/python#重設密碼-reset_password) | 程式執行到此函數時，會於命令列提示請用戶輸入證券密碼及憑證密碼。 |
| 國泰   |                                                              |                                                              |

- #### Input

> None

- #### Response

> None

### 6.2.3. 憑證資訊

| 名稱                | 描述     |
| ------------------- | -------- |
| tradex_q_certinfo() | 憑證資訊 |

| 證劵商 | API                                                          | 描述               |
| ------ | ------------------------------------------------------------ | ------------------ |
| 玉山   | [certinfo()](https://www.esunsec.com.tw/trading-platforms/api-trading/docs/trading/reference/python#憑證資訊-certinfo) | 取得憑證相關資訊。 |
| 國泰   |                                                              |                    |

- #### Input

> None

- #### Response

> 請見 [certinfo()](https://www.esunsec.com.tw/trading-platforms/api-trading/docs/trading/reference/python#憑證資訊-certinfo)

### 6.2.4. 金鑰資訊

| 名稱              | 描述     |
| ----------------- | -------- |
| tradex_q_apiKey() | 金鑰資訊 |

| 證劵商 | API                                                          | 描述               |
| ------ | ------------------------------------------------------------ | ------------------ |
| 玉山   | [get_key_info()](https://www.esunsec.com.tw/trading-platforms/api-trading/docs/trading/reference/python#金鑰資訊-get_key_info) | 取得金鑰相關資訊。 |
| 國泰   |                                                              |                    |

- #### Input

> None

- #### Response

> 請見 [get_key_info()](https://www.esunsec.com.tw/trading-platforms/api-trading/docs/trading/reference/python#金鑰資訊-get_key_info)

## 6.2. 查詢

### 6.2.1. 交易額度及權限

| 名稱                  | 描述           |
| --------------------- | -------------- |
| tradex_q_tradelimit() | 交易額度及權限 |

| 證劵商 | API                                                          | 描述                                 |
| ------ | ------------------------------------------------------------ | ------------------------------------ |
| 玉山   | [get_trade_status](https://www.esunsec.com.tw/trading-platforms/api-trading/docs/trading/reference/python/#交易額度及權限-get_trade_status) | 取得用戶交易額度、交易權限相關資訊。 |
| 國泰   |                                                              |                                      |

- #### Input

> None

- #### Response

> 請見 [get_trade_status](https://www.esunsec.com.tw/trading-platforms/api-trading/docs/trading/reference/python/#交易額度及權限-get_trade_status)

### 6.2.2. 銀行餘額

| 名稱               | 描述     |
| ------------------ | -------- |
| tradex_q_balance() | 銀行餘額 |

| 證劵商 | API                                                          | 描述                                         |
| ------ | ------------------------------------------------------------ | -------------------------------------------- |
| 玉山   | [get_balance()](https://www.esunsec.com.tw/trading-platforms/api-trading/docs/trading/reference/python#銀行餘額-get_balance) | 取得銀行餘額相關資訊。 (每 180 秒可查詢一次) |
| 國泰   |                                                              |                                              |

- #### Input

> None

- #### Response

| 名稱                  | 型態      | 描述             |
| --------------------- | --------- | ---------------- |
| available_balance     | number    | 可用銀行餘額     |
| exange_balance        | number    | 今日票據交換金額 |
| stock_pre_save_amount | number    | 圈存金額         |
| is_latest_data        | boolean   |                  |
| updated_at            | Timestamp | Local time       |

### 6.2.3. 庫存明細

| 名稱                   | 描述     |
| ---------------------- | -------- |
| tradex_q_inventories() | 庫存明細 |

| 證劵商 | API                                                          | 描述                 |
| ------ | ------------------------------------------------------------ | -------------------- |
| 玉山   | [get_inventories()](https://www.esunsec.com.tw/trading-platforms/api-trading/docs/trading/reference/python#庫存明細-get_inventories) | 取得當下的庫存明細。 |
| 國泰   |                                                              |                      |

- #### Input

> None

- #### Response

> 請見 [get_inventories()](https://www.esunsec.com.tw/trading-platforms/api-trading/docs/trading/reference/python#庫存明細-get_inventories)

## 6.3. 交易下單

### 6.3.1. 買進

| 名稱                                               | 描述            |
| -------------------------------------------------- | --------------- |
| tradex_o_buy(stock_no,  price, quantity)           | 整張買進        |
| tradex_o_buy_after(stock_no,  price, quantity)     | 整張買進 - 盤後 |
| tradex_o_buy_odd(stock_no,  price, quantity)       | 零股買進        |
| tradex_o_buy_odd_after(stock_no,  price, quantity) | 零股買進 - 盤後 |

| 證劵商 | API                                                          | 描述         |
| ------ | ------------------------------------------------------------ | ------------ |
| 玉山   | [place_order(order_object)](https://www.esunsec.com.tw/trading-platforms/api-trading/docs/trading/reference/python#下單-place_orderorder_object) | 送出委託單。 |
| 國泰   |                                                              |              |

- ####  Input

| 名稱     | 型態   | 描述     |
| -------- | ------ | -------- |
| stock_no | string | 股票代號 |
| price    | float  | 委託價格 |
| quantity | int    | 委託數量 |

### 6.3.2. 賣出

| 名稱                                                | 描述            |
| --------------------------------------------------- | --------------- |
| tradex_o_sell(stock_no,  price, quantity)           | 整張賣出        |
| tradex_o_sell_after(stock_no,  price, quantity)     | 整張賣出 - 盤後 |
| tradex_o_sell_odd(stock_no,  price, quantity)       | 零股賣出        |
| tradex_o_sell_odd_after(stock_no,  price, quantity) | 零股賣出 - 盤後 |

| 證劵商 | API                                                          | 描述         |
| ------ | ------------------------------------------------------------ | ------------ |
| 玉山   | [place_order(order_object)](https://www.esunsec.com.tw/trading-platforms/api-trading/docs/trading/reference/python#下單-place_orderorder_object) | 送出委託單。 |
| 國泰   |                                                              |              |

- ##### Input

| 名稱     | 型態   | 描述     |
| -------- | ------ | -------- |
| stock_no | string | 股票代號 |
| price    | float  | 委託價格 |
| quantity | int    | 委託數量 |

### 6.3.3. 委託紀錄

| 名稱              | 描述     |
| ----------------- | -------- |
| tradex_q_orders() | 委託紀錄 |

| 證劵商 | API                                                          | 描述           |
| ------ | ------------------------------------------------------------ | -------------- |
| 玉山   | [get_order_results()](https://www.esunsec.com.tw/trading-platforms/api-trading/docs/trading/reference/python#委託紀錄-get_order_results) | 取得委託列表。 |
| 國泰   |                                                              |                |

- ##### Input

> None

- #### Response

> 請見 [get_order_results()](https://www.esunsec.com.tw/trading-platforms/api-trading/docs/trading/reference/python#委託紀錄-get_order_results)

### 6.3.4. 委託歷史紀錄

> 預設最近前 2日的歷史紀錄

| 名稱                                                         | 描述         |
| ------------------------------------------------------------ | ------------ |
| tradex_q_orders_history(start_date_str=None, end_date_str=None) | 委託歷史紀錄 |

| 證劵商 | API                                                          | 描述                                                         |
| ------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 玉山   | [get_order_results_by_date(start_date, end_date)](https://www.esunsec.com.tw/trading-platforms/api-trading/docs/trading/reference/python#歷史委託-get_order_results_by_datestart_date-end_date) | 取得 start_date, end_date 時間範圍內的歷史委託列表，無法查詢已刪除及預約單。 |
| 國泰   |                                                              |                                                              |

- ##### Input

| 名稱           | 型態   | 描述                         |
| -------------- | ------ | ---------------------------- |
| start_date_str | string | 格式為 yyyy-MM-dd 的開始日期 |
| end_date_str   | string | 格式為 yyyy-MM-dd 的結束日期 |

- #### Response

> 請見 [get_order_results_by_date(start_date, end_date)](https://www.esunsec.com.tw/trading-platforms/api-trading/docs/trading/reference/python#歷史委託-get_order_results_by_datestart_date-end_date)

### ~~6.3.5. 委託改價~~

> 因為限制過多，暫不包裝此功能。

| 名稱 | 描述 |
| ---- | ---- |
|      |      |

| 證劵商 | API                                                          | 描述           |
| ------ | ------------------------------------------------------------ | -------------- |
| 玉山   | [modify_price(order_result, target_price, price_flag)](https://www.esunsec.com.tw/trading-platforms/api-trading/docs/trading/reference/python#改價-modify_priceorder_result-target_price-price_flag) | 修改委託價格。 |
| 國泰   |                                                              |                |

- ##### Input

| 名稱 | 型態 | 描述 |
| ---- | ---- | ---- |
|      |      |      |

- #### Response

> 請見  [modify_price(order_result, target_price, price_flag)](https://www.esunsec.com.tw/trading-platforms/api-trading/docs/trading/reference/python#改價-modify_priceorder_result-target_price-price_flag)

### ~~6.3.6. 委託刪單~~

> 因為限制過多，暫不包裝此功能。

| 名稱 | 描述 |
| ---- | ---- |
|      |      |

| 證劵商 | API                                                          | 描述                           |
| ------ | ------------------------------------------------------------ | ------------------------------ |
| 玉山   | [cancel_order(order_result, **kwargs)](https://www.esunsec.com.tw/trading-platforms/api-trading/docs/trading/reference/python#刪改單-cancel_orderorder_result-kwargs) | 減少委託單量，或刪除單筆委託。 |
| 國泰   |                                                              |                                |

- ##### Input

| 名稱 | 型態 | 描述 |
| ---- | ---- | ---- |
|      |      |      |

- #### Response

> 請見  [cancel_order(order_result, **kwargs)](https://www.esunsec.com.tw/trading-platforms/api-trading/docs/trading/reference/python#刪改單-cancel_orderorder_result-kwargs)

### 6.3.7. 成交明細

| 名稱                                    | 描述     |
| --------------------------------------- | -------- |
| tradex_q_transactions(query_range="0d") | 成交明細 |

| 證劵商 | API                                                          | 描述                               |
| ------ | ------------------------------------------------------------ | ---------------------------------- |
| 玉山   | [get_transactions(query_range)](https://www.esunsec.com.tw/trading-platforms/api-trading/docs/trading/reference/python#近期成交明細-get_transactionsquery_range) | 取得近期特定時間範圍內的成交明細。 |
| 國泰   |                                                              |                                    |

- ##### Input

| 名稱        | 型態   | 描述                                                  |
| ----------- | ------ | ----------------------------------------------------- |
| query_range | string | 時間區間，目前有效數值為 "0d"(當日)、"3d"、"1m"、"3m" |

- #### Response

> 請見 [get_transactions(query_range)](https://www.esunsec.com.tw/trading-platforms/api-trading/docs/trading/reference/python#近期成交明細-get_transactionsquery_range)

### 6.3.8. 成交歷史明細

| 名稱                                                         | 描述         |
| ------------------------------------------------------------ | ------------ |
| tradex_q_transactions_history(start_date_str=None, end_date_str=None) | 成交歷史明細 |

| 證劵商 | API                                                          | 描述                                                         |
| ------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 玉山   | [get_transactions_by_date(start_date, end_date)](https://www.esunsec.com.tw/trading-platforms/api-trading/docs/trading/reference/python#成交明細依指定日期-get_transactions_by_datestart_date-end_date) | 取得 start_date, end_date 時間範圍內的成交明細。<br>取得特定日期區間的成交明細，目前提供查詢的日期範圍，以 180 日為限！<br>若超過這個時間範圍區間，會得到 AW00002 的錯誤訊息！ |
| 國泰   |                                                              |                                                              |

- ##### Input

| 名稱           | 型態   | 描述                         |
| -------------- | ------ | ---------------------------- |
| start_date_str | string | 格式為 yyyy-MM-dd 的開始日期 |
| end_date_str   | string | 格式為 yyyy-MM-dd 的結束日期 |

- #### Response

> 請見 [get_transactions_by_date(start_date, end_date)](https://www.esunsec.com.tw/trading-platforms/api-trading/docs/trading/reference/python#成交明細依指定日期-get_transactions_by_datestart_date-end_date)

### 6.3.9. 交割款

| 名稱                   | 描述   |
| ---------------------- | ------ |
| tradex_q_settlements() | 交割款 |

| 證劵商 | API                                                          | 描述             |
| ------ | ------------------------------------------------------------ | ---------------- |
| 玉山   | [get_settlements()](https://www.esunsec.com.tw/trading-platforms/api-trading/docs/trading/reference/python#交割款-get_settlements) | 取得交割款資訊。 |
| 國泰   |                                                              |                  |

- ##### Input

> None

- #### Response

> 請見 [get_settlements()](https://www.esunsec.com.tw/trading-platforms/api-trading/docs/trading/reference/python#交割款-get_settlements)

| 名稱   | 型態   | 描述              |
| ------ | ------ | ----------------- |
| c_date | string | 交割日期 YYYYMMDD |
| date   | string | 成交日期 YYYYMMDD |
| price  | string | 交割款應收金額    |

## 6.4. 其它

### ~~6.4.1. 市場開盤狀態~~

> 暫不包裝此功能。

| 名稱 | 描述 |
| ---- | ---- |
|      |      |

| 證劵商 | API                                                          | 描述           |
| ------ | ------------------------------------------------------------ | -------------- |
| 玉山   | [get_market_status()](https://www.esunsec.com.tw/trading-platforms/api-trading/docs/trading/reference/python#市場開盤狀態-get_market_status) | 取得開盤狀態。 |
| 國泰   |                                                              |                |

- ##### Input

| 名稱 | 型態 | 描述 |
| ---- | ---- | ---- |
|      |      |      |

- #### Response

> 請見  [get_market_status()](https://www.esunsec.com.tw/trading-platforms/api-trading/docs/trading/reference/python#市場開盤狀態-get_market_status)

### ~~6.4.2. 取得機器時間~~

> 暫不包裝此功能。

| 名稱 | 描述 |
| ---- | ---- |
|      |      |

| 證劵商 | API                                                          | 描述                 |
| ------ | ------------------------------------------------------------ | -------------------- |
| 玉山   | [get_machine_time()](https://www.esunsec.com.tw/trading-platforms/api-trading/docs/trading/reference/python#取得機器時間-get_machine_time) | 取得主機端機器的時間 |
| 國泰   |                                                              |                      |

- ##### Input

| 名稱 | 型態 | 描述 |
| ---- | ---- | ---- |
|      |      |      |

- #### Response

> 請見  [get_machine_time()](https://www.esunsec.com.tw/trading-platforms/api-trading/docs/trading/reference/python#取得機器時間-get_machine_time)

# Appendix

# I. Study

# II. Debug

# III. Glossary

# IV. Tool Usage

# Author

> Created and designed by [Lanka Hsu](lankahsu@gmail.com).

# License

> [pythonX9](https://github.com/lankahsu520/pythonX9) is under the New BSD License (BSD-3-Clause).

