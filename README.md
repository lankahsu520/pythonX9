# 1. Overview

> pythonX9 把常用的工具集合在一起，並且將呼叫簡單化。

# 2. Depend on

## - [ifaddr](https://pypi.org/project/ifaddr/)
## - [matplotlib](https://pypi.org/project/matplotlib/)
## - [netifaces (0.11.0)](https://pypi.org/project/netifaces/)
## - [pandas](https://pypi.org/project/pandas/)
## - [psutil](https://pypi.org/project/psutil/)
## - [streamlink](https://pypi.org/project/streamlink/)

> This plugin does not support protected videos, try youtube-dl instead

# 3. Current Status

>不敢臭屁自己寫的有多完美，但是秉持著對 c 的嚴謹態度，至少能維持一定的水平的產出。
>
>雖然 python 入手容易，但是看到那些“不謹慎的成品”，並且掛上 AI 高手的名號，真的心生恐懼！


# 4. Build
```bash
Do nothing
```
# 5. Example or Usage

## - dummy_123.py - a template in python.
```mermaid
flowchart LR
	Start([Start])
	
	main[main]

	signal[[signal.signal]]
	signal_handler[signal_handler]
	parse_arg[[parse_arg]]
	show_usage[show_usage]

	app_start[app_start]
	app_watch[[app_watch]]

	app_stop[[app_stop]]
	app_exit[app_exit]
	
	app_release[[app_release]]
	End([End])
	
	Start-->main-->signal-->parse_arg-->app_start-->app_exit-->app_stop
	signal-->signal_handler
	
	parse_arg-->show_usage
	app_start-->app_watch
	app_stop-->app_release-->End
```

```bash
$ make dummy_123.py
or
$ ./dummy_123.py -d4
[8465/8465] dummy_123.py|app_start:0015 - (Python version: 3.8.10, chkPYTHONge(3,7,0): True, chkPYTHONle(3,7,0): False)
[8465/8465] dummy_123.py|app_start:0019 - (IFACE: enp0s3, IFACE_MAC: 08:00:27:33:73:52, IFACE_IPv4: 10.0.2.15)
[8465/8465] dummy_api.py|__init__:0020 - Enter ...
[8465/8465] dummy_api.py|ctx_init:0012 - Enter ...
[8465/8465] dummy_api.py|start:0029 - Start !!!
[8465/8465] dummy_api.py|parse_args:0025 - Enter ...
[8465/8465] dummy_123.py|app_release:0033 - Enter ...
[8465/8465] dummy_123.py|app_release:0038 - call dummy_ctx.release ...
[8465/8465] dummy_api.py|release:0009 - Done.
[8465/8465] dummy_123.py|app_release:0042 - Done.
[8465/8465] dummy_123.py|app_stop:0051 - Done.
[8465/8465] dummy_123.py|main:0103 - Bye-Bye !!! (is_quit: 1)

```
## - httpd_123.py - a simple Web Server

>負責接收檔案，並將內容存至 ./tmp。
>
>當初有人挑戰我，上傳檔案不能用 "PUT"。
>
>我就解釋給他說，當初 HTTP 剛流行時，上傳檔案，都是用 "PUT"。但不知何時，有的 HTTP Server 是用 "POST"，也有的 HTTP Server 是用 "GET"。
>
>說完這些這些，那位人士說我在唬爛。不過我還是要再教育他，不管是用 "PUT"、"POST" 和 "GET"，都只是 HTTP Server 方有沒有嫁接後面的處理程序，至於對錯只能在 SPEC 上說。
>
>因為你要對接的 HTTP Server不見得你能掌控。

```mermaid
flowchart LR
	httpd_123[httpd_123]
	curl[curl]
	saveto[/tmp/HTTPServer_ctx-3272277516 /]
	curl -->|endianness.jpg|httpd_123-->|saveto|saveto
```
```bash
$ ./httpd_123.py -p 8087
Serving HTTP on 0.0.0.0 port 8087 (http://0.0.0.0:8087/) ...
[httpd_123.py|do_POST:0062] - Enter ...
[httpd_123.py|dump_header:0022] - ** path **
[httpd_123.py|dump_header:0023] - /
[httpd_123.py|dump_header:0024] - ** headers **
[httpd_123.py|dump_header:0025] - Host: 192.168.56.104:8087
User-Agent: curl/7.68.0
Accept: */*
Content-Length: 46535
Content-Type: multipart/form-data; boundary=------------------------405c329812b65da4
Expect: 100-continue


[httpd_123.py|dump_header:0029] - ** Body /tmp/HTTPServer_ctx-3272277516 **
192.168.56.104 - - [19/Apr/2023 15:05:47] "POST / HTTP/1.1" 200 -

```

```bash
$ curl -d @endianness.jpg http://192.168.56.104:8087

$ gimp /tmp/HTTPServer_ctx-3272277516
```

## - multicast_123.py - a multicast example.

```bash
$ make multicast_123.py
or
$ ./multicast_123.py -d4
[4977/4977] multicast_api.py|__init__:0110 - Enter ...
[4977/4977] multicast_api.py|ctx_init:0091 - Enter ...
[4977/4977] multicast_api.py|start:0119 - Start !!!
[4977/4977] multicast_api.py|parse_args:0115 - Enter ...
[4977/4978] multicast_api.py|serverx:0027 - bind ... (239.255.255.250:3618)
[4977/4978] multicast_api.py|readx:0045 - Run loop ...
[4977/4977] multicast_123.py|app_start:0025 - Send a packet every 2 seconds 239.255.255.250:3618.
[4977/4977] multicast_api.py|writex:0031 - send 239.255.255.250:3618 - b'1'
[4977/4978] multicast_123.py|notify_cb:0017 - buffer[1] - b'1'
[4977/4977] multicast_api.py|writex:0031 - send 239.255.255.250:3618 - b'2'
[4977/4978] multicast_123.py|notify_cb:0017 - buffer[1] - b'2'
[4977/4977] multicast_api.py|writex:0031 - send 239.255.255.250:3618 - b'3'
[4977/4978] multicast_123.py|notify_cb:0017 - buffer[1] - b'3'
[4977/4977] multicast_api.py|writex:0031 - send 239.255.255.250:3618 - b'4'
[4977/4978] multicast_123.py|notify_cb:0017 - buffer[1] - b'4'
^C[4977/4977] multicast_123.py|app_release:0042 - Enter ...
[4977/4977] multicast_123.py|app_release:0047 - call multicast_ctx.release ...
[4977/4977] threadx_api.py|threadx_wakeup:0033 - call notify ...
[4977/4978] multicast_api.py|closex:0021 - Done.
[4977/4978] multicast_api.py|threadx_handler:0079 - Bye-Bye !!!
[4977/4977] multicast_api.py|release:0088 - Done.
[4977/4977] multicast_123.py|app_release:0051 - Done.
[4977/4977] multicast_123.py|app_stop:0060 - Done.
[4977/4977] multicast_api.py|writex:0031 - send 239.255.255.250:3618 - b'5'
[4977/4977] multicast_123.py|main:0112 - Bye-Bye !!! (is_quit: 1)

```

## - queuex_123.py - a queue and stack example.

>網路都只會介紹什麼是 queue，但是實際操作經驗零。這邊給你一個很好範例，特別是當你要操作TTY或是一些序列設備時，就會發現這有多好用。

```bash
$ make queuex_123.py
or
$ ./queuex_123.py -d4
[6822/6822] queuex_api.py|ctx_init:0094 - Enter ...
[6822/6822] queuex_123.py|queue_test:0024 - Push an integer every 10/1000 seconds. (is_stack: 0)
[6822/6822] queuex_123.py|queue_test:0028 - call queuex_push ... (idx: 1)
[6822/6822] queuex_123.py|queue_test:0028 - call queuex_push ... (idx: 2)
[6822/6822] queuex_123.py|queue_test:0028 - call queuex_push ... (idx: 3)
[6822/6822] queuex_123.py|queue_test:0028 - call queuex_push ... (idx: 4)
[6822/6822] queuex_123.py|queue_test:0028 - call queuex_push ... (idx: 5)
[6822/6823] queuex_123.py|exec_cb:0014 - (data: 1)
[6822/6823] queuex_123.py|exec_cb:0014 - (data: 2)
[6822/6823] queuex_123.py|exec_cb:0014 - (data: 3)
[6822/6823] queuex_123.py|exec_cb:0014 - (data: 4)
[6822/6823] queuex_123.py|exec_cb:0014 - (data: 5)
[6822/6822] queuex_123.py|queue_test:0028 - call queuex_push ... (idx: 6)
[6822/6823] queuex_123.py|exec_cb:0014 - (data: 6)
[6822/6822] queuex_123.py|queue_test:0028 - call queuex_push ... (idx: 7)
[6822/6823] queuex_123.py|exec_cb:0014 - (data: 7)
[6822/6822] queuex_123.py|queue_test:0028 - call queuex_push ... (idx: 8)
[6822/6823] queuex_123.py|exec_cb:0014 - (data: 8)
[6822/6822] queuex_123.py|queue_test:0028 - call queuex_push ... (idx: 9)
[6822/6823] queuex_123.py|exec_cb:0014 - (data: 9)
[6822/6822] queuex_123.py|queue_test:0028 - call queuex_push ... (idx: 10)
[6822/6822] queuex_api.py|ctx_init:0094 - Enter ...
[6822/6823] queuex_123.py|exec_cb:0014 - (data: 10)
[6822/6822] queuex_123.py|queue_test:0024 - Push an integer every 10/1000 seconds. (is_stack: 1)
[6822/6822] queuex_123.py|queue_test:0028 - call queuex_push ... (idx: 1)
[6822/6822] queuex_123.py|queue_test:0028 - call queuex_push ... (idx: 2)
[6822/6822] queuex_123.py|queue_test:0028 - call queuex_push ... (idx: 3)
[6822/6822] queuex_123.py|queue_test:0028 - call queuex_push ... (idx: 4)
[6822/6822] queuex_123.py|queue_test:0028 - call queuex_push ... (idx: 5)
[6822/6824] queuex_123.py|exec_cb:0014 - (data: 5)
[6822/6824] queuex_123.py|exec_cb:0014 - (data: 4)
[6822/6824] queuex_123.py|exec_cb:0014 - (data: 3)
[6822/6824] queuex_123.py|exec_cb:0014 - (data: 2)
[6822/6824] queuex_123.py|exec_cb:0014 - (data: 1)
[6822/6822] queuex_123.py|queue_test:0028 - call queuex_push ... (idx: 6)
[6822/6824] queuex_123.py|exec_cb:0014 - (data: 6)
[6822/6822] queuex_123.py|queue_test:0028 - call queuex_push ... (idx: 7)
[6822/6824] queuex_123.py|exec_cb:0014 - (data: 7)
[6822/6822] queuex_123.py|queue_test:0028 - call queuex_push ... (idx: 8)
[6822/6824] queuex_123.py|exec_cb:0014 - (data: 8)
[6822/6822] queuex_123.py|queue_test:0028 - call queuex_push ... (idx: 9)
[6822/6824] queuex_123.py|exec_cb:0014 - (data: 9)
[6822/6822] queuex_123.py|queue_test:0028 - call queuex_push ... (idx: 10)
[6822/6822] queuex_123.py|app_release:0049 - Enter ...
[6822/6824] queuex_123.py|exec_cb:0014 - (data: 10)
[6822/6822] queuex_123.py|app_release:0054 - call queuex_ctx.release ...
[6822/6823] queuex_api.py|threadx_handler:0083 - Bye-Bye !!!
[6822/6822] queuex_api.py|release:0091 - Done.
[6822/6822] queuex_123.py|app_release:0054 - call queuex_ctx.release ...
[6822/6824] queuex_api.py|threadx_handler:0083 - Bye-Bye !!!
[6822/6822] queuex_api.py|release:0091 - Done.
[6822/6822] queuex_123.py|app_release:0058 - Done.
[6822/6822] queuex_123.py|app_exit:0070 - Done.
[6822/6822] queuex_123.py|main:0120 - Bye-Bye !!! (is_quit: 1)

```

## - statex_123.py - state machine example.

```bash
$ make statex_123.py
or
$ ./statex_123.py -d4
[7221/7221] statex_api.py|ctx_init:0178 - Enter ...
[7221/7221] statex_api.py|statex_push:0072 - (name: Idle)
[7221/7222] statex_123.py|exec_cb_Idle:0064 - (name: Idle)
[7221/7221] statex_api.py|statex_push:0072 - (name: CableLinked)
[7221/7222] statex_123.py|exec_cb_CableLinked:0054 - (name: CableLinked)
[7221/7222] statex_123.py|leave_cb_Idle:0067 - (name: Idle)
[7221/7221] statex_api.py|statex_push:0072 - (name: NetworkOn)
[7221/7222] statex_123.py|exec_cb_NetworkOn:0044 - (name: NetworkOn)
[7221/7222] statex_123.py|leave_cb_CableLinked:0057 - (name: CableLinked)
[7221/7221] statex_api.py|statex_push:0072 - (name: CloudConnected)
[7221/7222] statex_123.py|exec_cb_CloudConnected:0034 - (name: CloudConnected)
[7221/7222] statex_123.py|leave_cb_NetworkOn:0047 - (name: NetworkOn)
[7221/7221] statex_api.py|statex_remove:0109 - (name: NetworkOn)
[7221/7221] statex_api.py|statex_pop:0092 - (name: CloudConnected)
[7221/7221] statex_123.py|exec_cb_CableLinked:0054 - (name: CableLinked)
[7221/7221] statex_123.py|leave_cb_CloudConnected:0037 - (name: CloudConnected)
[7221/7221] statex_123.py|app_release:0109 - Enter ...
[7221/7221] statex_123.py|app_release:0114 - call statex_ctx.release ...
[7221/7222] statex_api.py|threadx_handler:0167 - Bye-Bye !!!
[7221/7221] statex_api.py|release:0175 - Done.
[7221/7221] statex_123.py|app_release:0118 - Done.
[7221/7221] statex_123.py|app_exit:0130 - Done.
[7221/7221] statex_123.py|main:0180 - Bye-Bye !!! (is_quit: 1)

```

## - stockx_backtesting_123.py - 利用股票的收盤價計算每月存股的報酬率

> 先從`臺灣證券交易所/證券櫃檯買賣中心`取得歷史收盤價，計算`日日存`的報酬率

> 分割計算
>
> ```python
> # stockx_backtesting_api.py
> 
> stock_splits = [ ("0050", pd.Timestamp("2025-06-18"), 1/4) ]
> ```

> 短、中、長期報酬率設定
>
> ```python
> # stockx_backtesting_123.py
> 
> argsX = {
> 	"stock_no": stock_no
> 	,"year_ago": year_ago
> 	,"delta": delta_days
> 	,"buy_short": 1
> 	,"buy_medium": 3
> 	,"buy_long": 5
> 	,"history_folder": f"./stock"
> 	,"renew": False
> 	,"text": False
> 	,"verbose": False
> }
> ```
>
> ```python
> # stockx_backtesting_api.py
> 
> 	def parse_args(self, args):
> 		...
> 		self.buy_short = args["buy_short"]
> 		self.buy_medium = args["buy_medium"]
> 		self.buy_long = args["buy_long"]
> ```

```bash
$ ./stockx_backtesting_123.py
Usage: ./stockx_backtesting_123.py <options...>
  -h, --help
  -d, --debug level
  -s, --stock Stock symbol
  -y, --year N years ago
  -l, --delta N days ago
  -r, --renew
  -t, --text
  -v, --verbose
    0: critical, 1: errror, 2: warning, 3: info, 4: debug, 5: trace
```

```bash
$ make stockx_backtesting_123.py
or
$ ./stockx_backtesting_123.py -d4 -y 10 -s 0050
[8540/140536377751360] pythonX9.py|argsX_dump:0057 - {'stock_no': '0050', 'year_ago': 10, 'delta': 5, 'buy_short': 1, 'buy_medium': 3, 'buy_long': 5, 'history_folder': './stock', 'renew': False, 'text': False, 'verbose': False}
[8540/140536377751360] stockx_backtesting_api.py|history_load_from_csv:0329 - Found !!! (./stock/0050_history.csv), Loading ...
[0050] (stock_last_date：2026-09-09, delta.days: 2, stock_delta_days: 5)  Completed !!!
Day 1-Year                  3-Year                  5-Year                  Sum
    (%)    count  average   (%)    count  average   (%)    count  average   (%)
1   35.47  12     80.94     97.68  36     55.47     139.53 60     45.78     272.68
2   35.02  12     81.21     97.29  36     55.58     139.26 60     45.83     271.57
3   35.19  12     81.11     97.49  36     55.52     139.48 60     45.79     272.16
4   35.09  12     81.17     97.47  36     55.53     139.46 60     45.79     272.02
5   32.69  12     82.63     95.71  36     56.03     137.84 60     46.10     266.24
6   32.11  12     83.00     95.31  36     56.14     137.28 60     46.21     264.70
7   31.98  12     83.08     94.59  36     56.35     136.87 60     46.29     263.44
8   31.74  12     83.23     94.33  36     56.42     136.73 60     46.32     262.80
9   32.23  12     82.92     94.58  36     56.35     136.95 60     46.27     263.76
10  32.07  12     83.03     94.3   36     56.43     136.48 60     46.37     262.85
11  31.73  12     83.24     93.53  36     56.66     135.83 60     46.50     261.09
12  34.77  13     81.36     95.31  37     56.14     135.32 60     46.60     265.40
13  34.45  13     81.55     94.87  37     56.27     135.0  60     46.66     264.32
14  34.56  13     81.49     94.88  37     56.27     134.85 60     46.69     264.29
15  34.92  13     81.27     95.01  37     56.23     134.97 60     46.66     264.90
16  34.29  13     81.65     94.22  37     56.46     134.18 60     46.82     262.69
17  33.9   13     81.89     93.97  37     56.53     133.86 60     46.89     261.73
18  34.72  13     81.39     94.6   37     56.35     134.3  60     46.80     263.62
19  34.78  13     81.35     94.44  37     56.39     134.25 60     46.81     263.47
20  35.36  13     81.00     95.09  37     56.21     134.96 60     46.67     265.41
21  35.11  13     81.15     94.89  37     56.26     134.82 60     46.70     264.82
22  34.5   13     81.52     94.52  37     56.37     134.6  60     46.74     263.62
23  33.57  13     82.09     93.93  37     56.54     134.15 60     46.83     261.65
24  33.69  13     82.02     93.62  37     56.63     133.88 60     46.88     261.19
25  34.2   13     81.70     93.95  37     56.53     134.23 60     46.81     262.38
26  33.17  13     82.34     92.86  37     56.85     133.37 60     46.99     259.40
27  33.55  13     82.10     93.28  37     56.73     133.8  60     46.90     260.63
28  33.01  13     82.44     93.02  37     56.81     133.45 60     46.97     259.48
29  33.41  12     82.19     94.92  35     56.25     134.45 56     46.77     262.78
30  32.84  12     82.54     92.55  34     56.95     133.17 55     47.03     258.56
31  31.9   7      83.13     92.98  21     56.82     135.08 35     46.64     259.96
(stock_no: 0050, final_price: 109.65)
[8540/140536377751360] stockx_backtesting_api.py|buy_return_plot_lines_on_screen:0244 - Plotting lines ...

```

![buy_return_plot_lines_on_screen](./images/buy_return_plot_lines_on_screen.png)

![buy_return_plot_bars_on_screen](./images/buy_return_plot_bars_on_screen.png)

## - sysinfo_123.py - 查找主機系統資訊，每5秒刷新畫面

```bash
$ make sysinfo_123.py
or 
$ ./sysinfo_123.py -d 4
[8510/8510] sysinfo_api.py|__init__:0201 - Enter ...
[8510/8510] sysinfo_api.py|ctx_init:0190 - Enter ...
[8510/8510] sysinfo_api.py|start:0212 - Start !!!
[8510/8510] sysinfo_api.py|parse_args:0206 - Enter ...
[8510/8510] sysinfo_api.py|keyboard_recv:0151 - press q to quit the loop ...
[8510/8511] sysinfo_api.py|os_net_ipaddrs:0067 - lo - 127.0.0.1/8
[8510/8511] sysinfo_api.py|os_net_ipaddrs:0067 - lo - ('::1', 0, 0)/128
[8510/8511] sysinfo_api.py|os_net_ipaddrs:0067 - enp0s3 - 10.0.2.15/24
[8510/8511] sysinfo_api.py|os_net_ipaddrs:0067 - enp0s3 - ('fe80::7549:bd5f:d0ed:32cf', 0, 2)/64
[8510/8511] sysinfo_api.py|os_net_ipaddrs:0067 - enp0s9 - 192.168.56.104/24
[8510/8511] sysinfo_api.py|os_net_ipaddrs:0067 - enp0s9 - ('fe80::e6d1:c758:6c5c:4cbd', 0, 4)/64
[8510/8511] sysinfo_api.py|os_net_ipaddrs:0067 - docker0 - 172.17.0.1/16
[8510/8511] sysinfo_api.py|os_net_ipaddrs:0067 - enp0s8 - ('fe80::d49:8acb:9f1b:c4cf', 0, 3)/64
[8510/8510] sysinfo_api.py|sysinfo_show:0145 - (Python version: 3.8.10 (default, Mar 13 2023, 10:26:41) )
[8510/8510] sysinfo_api.py|syinfo_show_uname:0133 - (os_platform: Linux-5.15.0-67-generic-x86_64-with-glibc2.29)
[8510/8510] sysinfo_api.py|syinfo_show_uname:0134 - (os_system: Linux)
[8510/8510] sysinfo_api.py|syinfo_show_uname:0135 - (os_node: build20-vbx)
[8510/8510] sysinfo_api.py|syinfo_show_uname:0136 - (os_release: 5.15.0-67-generic)
[8510/8510] sysinfo_api.py|syinfo_show_uname:0137 - (os_version: #74~20.04.1-Ubuntu SMP Wed Feb 22 14:52:34 UTC 2023)
[8510/8510] sysinfo_api.py|syinfo_show_uname:0138 - (os_machine: x86_64)
[8510/8510] sysinfo_api.py|syinfo_show_uname:0139 - (os_processor: x86_64)
[8510/8510] sysinfo_api.py|syinfo_show_uname:0141 - (uname_result: uname_result(system='Linux', node='build20-vbx', release='5.15.0-67-generic', version='#74~20.04.1-Ubuntu SMP Wed Feb 22 14:52:34 UTC 2023', machine='x86_64', processor='x86_64'))
[8510/8510] sysinfo_api.py|keyboard_recv:0162 - press q to quit the loop ...
[8510/8511] sysinfo_api.py|sysinfo_show_watch:0095 - --------------------------------------------------------------------------------
[8510/8511] sysinfo_api.py|sysinfo_show_watch:0098 - (cpu_usage: [2.0, 0.0, 1.0, 0.0])
[8510/8511] sysinfo_api.py|sysinfo_show_watch:0099 - (cpu_loadavg: (0.14, 0.07, 0.06))
[8510/8511] sysinfo_api.py|sysinfo_show_watch:0100 - (cpu_count: 4)
[8510/8511] sysinfo_api.py|sysinfo_show_watch:0101 - (cpu_num: 1)
[8510/8511] sysinfo_api.py|sysinfo_show_watch:0103 - (cpu_freq: 2808.0, min: 0.0, max: 0.0)
[8510/8511] sysinfo_api.py|sysinfo_show_watch:0112 - (disk_usage: 17.4 %)
[8510/8511] sysinfo_api.py|sysinfo_show_watch:0114 - (mem_total: 8335757312 bytes, mem_usage: 16.1 %)
[8510/8511] sysinfo_api.py|sysinfo_show_watch:0118 - (battery: 78.0 %, secsleft: 00:00:00, AC: True)
[8510/8511] sysinfo_api.py|sysinfo_show_watch:0125 - (fans: {})
q[8510/8511] sysinfo_api.py|threadx_handler:0173 - Bye-Bye !!!
[8510/8510] sysinfo_api.py|release:0187 - Done.
[8510/8510] sysinfo_123.py|app_release:0031 - Enter ...
[8510/8510] sysinfo_123.py|app_release:0036 - call sysinfo_ctx.release ...
[8510/8510] sysinfo_123.py|app_release:0040 - Done.
[8510/8510] sysinfo_123.py|app_stop:0049 - Done.
[8510/8510] sysinfo_123.py|main:0107 - Bye-Bye !!! (is_quit: 1)

```
## - youtube_123.py - a streamlink example.

>使用 streamlink  api 方式下載 youtube 影片

```bash
$ make youtube_123.py
==> python 3.12 - layer_python: /work/codebase/lankahsu520/pythonX9/python


==> python 3.12 - run: youtube_123.py
PYTHONPATH=/work/codebase/lankahsu520/pythonX9/python ./youtube_123.py -d 4
[10130/139874243954496] youtube_123.py|app_start:0033 - (Python version: 3.12.3, chkPYTHONge(3,8,0): True, chkPYTHONle(3,8,0): False)
[10130/139874243954496] streamlink_api.py|streams_urlparse:0031 - (stream_url: https://www.youtube.com/watch?v=a_9_38JpdYU)
[10130/139874243954496] streamlink_api.py|streams_urlparse:0032 - (urlparse: ParseResult(scheme='https', netloc='www.youtube.com', path='/watch', params='', query='v=a_9_38JpdYU', fragment=''))
[10130/139874243954496] streamlink_api.py|streams_choice:0051 - (quality: 240p / dict_keys(['audio_mp4a', 'audio_opus', '144p', '240p', '360p', '480p', '720p', '1080p', 'worst', 'best']))
[10130/139874243954496] streamlink_api.py|streams_savetofile:0080 - (filename: ./240p.mp4, chunksize:1024)
./240p.mp4: 37,503,875 bytes

[10130/139874243954496] streamlink_api.py|streams_streaming:0069 - Download complete !!!
[10130/139874243954496] youtube_123.py|app_release:0053 - Enter ...
[10130/139874243954496] youtube_123.py|app_release:0058 - call streamlink_ctx.release ...
[10130/139874243954496] youtube_123.py|app_release:0062 - Done.
[10130/139874243954496] youtube_123.py|app_exit:0075 - Done.
[10130/139874243954496] youtube_123.py|main:0125 - Bye-Bye !!! (is_quit: 1)

```

# 6. Documentation

> Run an example and read it.

# Appendix

# I. Study

# II. Debug

## II.1. [`trace`](https://docs.python.org/3/library/trace.html#module-trace) — Trace or track Python statement execution

```bash
# trace line by line
$ python3 -m trace \
	--ignore-dir=/usr/lib/python3.8 \
	--trace ./dummy_123.py -d4
```

# III. Glossary

# IV. Tool Usage

## IV.1. [eric](https://eric-ide.python-projects.org)

> 希望在 ubuntu 有 Python editor 且能 debug，不要求有強大的功能。
>
> eric 安裝方便，所以選擇此 IDE。

> Eric is a full featured Python editor and IDE, written in Python. It is based on the cross platform Qt UI toolkit, integrating the highly flexible Scintilla editor control. It is designed to be usable as everdays' quick and dirty editor as well as being usable as a professional project management tool integrating many advanced features Python offers the professional coder. eric includes a plug-in system, which allows easy extension of the IDE functionality with plug-ins downloadable from the net.
>
> Current stable version is eric7 based on PyQt6 (with Qt6) and Python 3.

```bash
$ sudo apt install -y eric
```

# Author

> Created and designed by [Lanka Hsu](lankahsu@gmail.com).

# License

> [pythonX9](https://github.com/lankahsu520/pythonX9) is under the New BSD License (BSD-3-Clause).
