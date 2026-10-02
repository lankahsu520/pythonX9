# 1. Overview

> utilsP9 把常用的工具集合在一起，並且將呼叫簡單化。

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
$ make dummy_123
or
$ ./dummy_123.py -d4
[14087/14087] utilsP9.py|argsX_dump:0057 - {}
[14087/14087] dummy_123.py|app_start:0041 - (Python version: 3.12.11, chkPYTHONge(3,7,0): True, chkPYTHONle(3,7,0): False)
[14087/14087] dummy_123.py|app_start:0047 - (IFACE: lo, IFACE_MAC: 00:00:00:00:00:00, IFACE_IPv4: 127.0.0.1)
[14087/14087] dummy_123.py|app_start:0047 - (IFACE: docker0, IFACE_MAC: 02:42:7e:67:48:22, IFACE_IPv4: 172.17.0.1)
[14087/14087] dummy_123.py|app_start:0047 - (IFACE: enp0s8, IFACE_MAC: 08:00:27:1a:c3:a3, IFACE_IPv4: 192.168.56.101)
[14087/14087] dummy_123.py|app_start:0047 - (IFACE: enp0s3, IFACE_MAC: 08:00:27:a1:f8:36, IFACE_IPv4: 192.168.31.17)
[14087/14087] dummy_api.py|__init__:0038 - Enter ...
[14087/14087] dummy_api.py|ctx_init:0030 - Enter ...
[14087/14087] dummy_api.py|start:0047 - Start !!!
[14087/14087] dummy_api.py|parse_args:0043 - Enter ...
[14087/14087] dummy_123.py|app_release:0065 - Enter ...
[14087/14087] dummy_123.py|app_release:0070 - call dummy_ctx.release ...
[14087/14087] dummy_api.py|release:0027 - Done.
[14087/14087] dummy_123.py|app_release:0074 - Done.
[14087/14087] dummy_123.py|app_exit:0085 - Done.
[14087/14087] dummy_123.py|main:0130 - Bye-Bye !!! (app_quit_get: 1)
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
$ make multicast_123
# or
$ ./multicast_123.py -d4
[12879/12879] utilsP9.py|argsX_dump:0057 - {}
[12879/12879] multicast_api.py|__init__:0127 - Enter ...
[12879/12879] multicast_api.py|ctx_init:0108 - Enter ...
[12879/12879] multicast_api.py|start:0136 - Start !!!
[12879/12879] multicast_api.py|parse_args:0132 - Enter ...
[12879/12880] multicast_api.py|serverx:0044 - bind ... (239.255.255.250:3618)
[12879/12880] multicast_api.py|readx:0062 - Run loop ...
[12879/12879] multicast_123.py|app_start:0052 - Send a packet every 2 seconds 239.255.255.250:3618.
[12879/12879] multicast_api.py|writex:0048 - send 239.255.255.250:3618 - b'1'
[12879/12880] multicast_123.py|notify_cb:0035 - buffer[1] - b'1'
[12879/12879] multicast_api.py|writex:0048 - send 239.255.255.250:3618 - b'2'
[12879/12880] multicast_123.py|notify_cb:0035 - buffer[1] - b'2'
[12879/12879] multicast_api.py|writex:0048 - send 239.255.255.250:3618 - b'3'
[12879/12880] multicast_123.py|notify_cb:0035 - buffer[1] - b'3'
[12879/12879] multicast_api.py|writex:0048 - send 239.255.255.250:3618 - b'4'
[12879/12880] multicast_123.py|notify_cb:0035 - buffer[1] - b'4'
^C[12879/12879] multicast_123.py|app_release:0072 - Enter ...
[12879/12879] multicast_123.py|app_release:0077 - call multicast_ctx.release ...
[12879/12879] threadx_api.py|threadx_wakeup:0061 - call notify ...
[12879/12880] multicast_api.py|closex:0038 - Done.
[12879/12880] multicast_api.py|threadx_handler:0096 - Bye-Bye !!!
[12879/12879] multicast_api.py|release:0105 - Done.
[12879/12879] multicast_123.py|app_release:0081 - Done.
[12879/12879] multicast_api.py|writex:0048 - send 239.255.255.250:3618 - b'5'
[12879/12879] multicast_123.py|app_exit:0092 - Done.
[12879/12879] multicast_123.py|main:0137 - Bye-Bye !!! (app_quit_get: 1)
```

## - queuex_123.py - a queue and stack example.

>網路都只會介紹什麼是 queue，但是實際操作經驗零。這邊給你一個很好範例，特別是當你要操作TTY或是一些序列設備時，就會發現這有多好用。

```bash
$ make queuex_123
or
$ ./queuex_123.py -d4
[12862/12862] utilsP9.py|argsX_dump:0057 - {}
[12862/12862] queuex_api.py|ctx_init:0117 - Enter ...
[12862/12862] queuex_123.py|queue_test:0042 - Push an integer every 10/1000 seconds. (is_stack: 0)
[12862/12862] queuex_123.py|queue_test:0047 - call queuex_push ... (item: 1)
[12862/12862] queuex_123.py|queue_test:0047 - call queuex_push ... (item: 2)
[12862/12862] queuex_123.py|queue_test:0047 - call queuex_push ... (item: 3)
[12862/12862] queuex_123.py|queue_test:0047 - call queuex_push ... (item: 4)
[12862/12862] queuex_123.py|queue_test:0047 - call queuex_push ... (item: 5)
[12862/12863] queuex_123.py|exec_cb:0032 - (data: 1)
[12862/12863] queuex_123.py|exec_cb:0032 - (data: 2)
[12862/12863] queuex_123.py|exec_cb:0032 - (data: 3)
[12862/12863] queuex_123.py|exec_cb:0032 - (data: 4)
[12862/12863] queuex_123.py|exec_cb:0032 - (data: 5)
[12862/12862] queuex_123.py|queue_test:0047 - call queuex_push ... (item: 6)
[12862/12863] queuex_123.py|exec_cb:0032 - (data: 6)
[12862/12862] queuex_123.py|queue_test:0047 - call queuex_push ... (item: 7)
[12862/12863] queuex_123.py|exec_cb:0032 - (data: 7)
[12862/12862] queuex_123.py|queue_test:0047 - call queuex_push ... (item: 8)
[12862/12863] queuex_123.py|exec_cb:0032 - (data: 8)
[12862/12862] queuex_123.py|queue_test:0047 - call queuex_push ... (item: 9)
[12862/12863] queuex_123.py|exec_cb:0032 - (data: 9)
[12862/12862] queuex_123.py|queue_test:0047 - call queuex_push ... (item: 10)
[12862/12862] queuex_api.py|ctx_init:0117 - Enter ...
[12862/12863] queuex_123.py|exec_cb:0032 - (data: 10)
[12862/12862] queuex_123.py|queue_test:0042 - Push an integer every 10/1000 seconds. (is_stack: 1)
[12862/12862] queuex_123.py|queue_test:0047 - call queuex_push ... (item: 1)
[12862/12862] queuex_123.py|queue_test:0047 - call queuex_push ... (item: 2)
[12862/12862] queuex_123.py|queue_test:0047 - call queuex_push ... (item: 3)
[12862/12862] queuex_123.py|queue_test:0047 - call queuex_push ... (item: 4)
[12862/12862] queuex_123.py|queue_test:0047 - call queuex_push ... (item: 5)
[12862/12864] queuex_123.py|exec_cb:0032 - (data: 5)
[12862/12864] queuex_123.py|exec_cb:0032 - (data: 4)
[12862/12864] queuex_123.py|exec_cb:0032 - (data: 3)
[12862/12864] queuex_123.py|exec_cb:0032 - (data: 2)
[12862/12864] queuex_123.py|exec_cb:0032 - (data: 1)
[12862/12862] queuex_123.py|queue_test:0047 - call queuex_push ... (item: 6)
[12862/12864] queuex_123.py|exec_cb:0032 - (data: 6)
[12862/12862] queuex_123.py|queue_test:0047 - call queuex_push ... (item: 7)
[12862/12864] queuex_123.py|exec_cb:0032 - (data: 7)
[12862/12862] queuex_123.py|queue_test:0047 - call queuex_push ... (item: 8)
[12862/12864] queuex_123.py|exec_cb:0032 - (data: 8)
[12862/12862] queuex_123.py|queue_test:0047 - call queuex_push ... (item: 9)
[12862/12864] queuex_123.py|exec_cb:0032 - (data: 9)
[12862/12862] queuex_123.py|queue_test:0047 - call queuex_push ... (item: 10)
[12862/12862] queuex_api.py|ctx_init:0117 - Enter ...
[12862/12864] queuex_123.py|exec_cb:0032 - (data: 10)
[12862/12862] utilsP9.py|os_urandom:0334 - (rand_num: 2588174001923390324)
[12862/12862] queuex_123.py|queue_test_dict:0068 - call queuex_push ... (item: {'key': 2588174001923390324, 'idx': 1})
[12862/12862] utilsP9.py|os_urandom:0334 - (rand_num: 1587121373964614091)
[12862/12862] queuex_123.py|queue_test_dict:0068 - call queuex_push ... (item: {'key': 1587121373964614091, 'idx': 2})
[12862/12862] utilsP9.py|os_urandom:0334 - (rand_num: 8972576424494140615)
[12862/12862] queuex_123.py|queue_test_dict:0068 - call queuex_push ... (item: {'key': 8972576424494140615, 'idx': 3})
[12862/12862] utilsP9.py|os_urandom:0334 - (rand_num: 4689097189221691477)
[12862/12862] queuex_123.py|queue_test_dict:0068 - call queuex_push ... (item: {'key': 4689097189221691477, 'idx': 4})
[12862/12862] utilsP9.py|os_urandom:0334 - (rand_num: 8098272801275810401)
[12862/12862] queuex_123.py|queue_test_dict:0068 - call queuex_push ... (item: {'key': 8098272801275810401, 'idx': 5})
[12862/12862] utilsP9.py|os_urandom:0334 - (rand_num: 9039847687270749903)
[12862/12862] queuex_123.py|queue_test_dict:0068 - call queuex_push ... (item: {'key': 9039847687270749903, 'idx': 6})
[12862/12862] utilsP9.py|os_urandom:0334 - (rand_num: 2860399992155630969)
[12862/12862] queuex_123.py|queue_test_dict:0068 - call queuex_push ... (item: {'key': 2860399992155630969, 'idx': 7})
[12862/12865] queuex_123.py|exec_cb:0032 - (data: {'key': 1587121373964614091, 'idx': 2})
[12862/12865] queuex_123.py|exec_cb:0032 - (data: {'key': 2588174001923390324, 'idx': 1})
[12862/12865] queuex_123.py|exec_cb:0032 - (data: {'key': 2860399992155630969, 'idx': 7})
[12862/12865] queuex_123.py|exec_cb:0032 - (data: {'key': 4689097189221691477, 'idx': 4})
[12862/12865] queuex_123.py|exec_cb:0032 - (data: {'key': 8098272801275810401, 'idx': 5})
[12862/12865] queuex_123.py|exec_cb:0032 - (data: {'key': 8972576424494140615, 'idx': 3})
[12862/12865] queuex_123.py|exec_cb:0032 - (data: {'key': 9039847687270749903, 'idx': 6})
[12862/12862] utilsP9.py|os_urandom:0334 - (rand_num: 1438926804533808911)
[12862/12862] queuex_123.py|queue_test_dict:0068 - call queuex_push ... (item: {'key': 1438926804533808911, 'idx': 8})
[12862/12865] queuex_123.py|exec_cb:0032 - (data: {'key': 1438926804533808911, 'idx': 8})
[12862/12862] utilsP9.py|os_urandom:0334 - (rand_num: 4575013626605114099)
[12862/12862] queuex_123.py|queue_test_dict:0068 - call queuex_push ... (item: {'key': 4575013626605114099, 'idx': 9})
[12862/12865] queuex_123.py|exec_cb:0032 - (data: {'key': 4575013626605114099, 'idx': 9})
[12862/12862] utilsP9.py|os_urandom:0334 - (rand_num: 8706136170148948304)
[12862/12862] queuex_123.py|queue_test_dict:0068 - call queuex_push ... (item: {'key': 8706136170148948304, 'idx': 10})
[12862/12862] queuex_123.py|app_release:0101 - Enter ...
[12862/12862] queuex_123.py|app_release:0106 - call queuex_ctx.release ...
[12862/12863] queuex_api.py|threadx_handler:0106 - Bye-Bye !!!
[12862/12865] queuex_123.py|exec_cb:0032 - (data: {'key': 8706136170148948304, 'idx': 10})
[12862/12862] queuex_api.py|release:0114 - Done.
[12862/12862] queuex_123.py|app_release:0106 - call queuex_ctx.release ...
[12862/12864] queuex_api.py|threadx_handler:0106 - Bye-Bye !!!
[12862/12862] queuex_api.py|release:0114 - Done.
[12862/12862] queuex_123.py|app_release:0106 - call queuex_ctx.release ...
[12862/12865] queuex_api.py|threadx_handler:0106 - Bye-Bye !!!
[12862/12862] queuex_api.py|release:0114 - Done.
[12862/12862] queuex_123.py|app_release:0110 - Done.
[12862/12862] queuex_123.py|app_exit:0121 - Done.
[12862/12862] queuex_123.py|main:0166 - Bye-Bye !!! (app_quit_get: 1)
```

## - statex_123.py - state machine example.

```bash
$ make statex_123
# or
$ ./statex_123.py -d4
[12859/12859] utilsP9.py|argsX_dump:0057 - {}
[12859/12859] statex_api.py|ctx_init:0178 - Enter ...
[12859/12859] statex_api.py|statex_push:0072 - (name: Idle)
[12859/12860] statex_123.py|exec_cb_Idle:0061 - (name: Idle)
[12859/12859] statex_api.py|statex_push:0072 - (name: CableLinked)
[12859/12860] statex_123.py|exec_cb_CableLinked:0051 - (name: CableLinked)
[12859/12860] statex_123.py|leave_cb_Idle:0064 - (name: Idle)
[12859/12859] statex_api.py|statex_push:0072 - (name: NetworkOn)
[12859/12860] statex_123.py|exec_cb_NetworkOn:0041 - (name: NetworkOn)
[12859/12860] statex_123.py|leave_cb_CableLinked:0054 - (name: CableLinked)
[12859/12859] statex_api.py|statex_push:0072 - (name: CloudConnected)
[12859/12860] statex_123.py|exec_cb_CloudConnected:0031 - (name: CloudConnected)
[12859/12860] statex_123.py|leave_cb_NetworkOn:0044 - (name: NetworkOn)
[12859/12859] statex_api.py|statex_remove:0109 - (name: NetworkOn)
[12859/12859] statex_api.py|statex_pop:0092 - (name: CloudConnected)
[12859/12859] statex_123.py|exec_cb_CableLinked:0051 - (name: CableLinked)
[12859/12859] statex_123.py|leave_cb_CloudConnected:0034 - (name: CloudConnected)
[12859/12859] statex_123.py|app_release:0116 - Enter ...
[12859/12859] statex_123.py|app_release:0121 - call statex_ctx.release ...
[12859/12860] statex_api.py|threadx_handler:0167 - Bye-Bye !!!
[12859/12859] statex_api.py|release:0175 - Done.
[12859/12859] statex_123.py|app_release:0125 - Done.
[12859/12859] statex_123.py|app_exit:0136 - Done.
[12859/12859] statex_123.py|main:0183 - Bye-Bye !!! (app_quit_get: 1)
```

## - sysinfo_123.py - 查找主機系統資訊，每5秒刷新畫面

```bash
$ make sysinfo_123
# or 
$ ./sysinfo_123.py -d 4
[12843/12843] utilsP9.py|argsX_dump:0057 - {'keyboard': 1, 'interval': 5}
[12843/12843] sysinfo_api.py|__init__:0210 - Enter ...
[12843/12843] sysinfo_api.py|ctx_init:0200 - Enter ...
[12843/12843] sysinfo_api.py|start:0221 - Start !!!
[12843/12843] sysinfo_api.py|parse_args:0215 - Enter ...
[12843/12843] sysinfo_api.py|keyboard_recv:0167 - press q to quit the loop ...
[12843/12844] sysinfo_api.py|os_net_ipaddrs:0083 - lo - 127.0.0.1/8
[12843/12844] sysinfo_api.py|os_net_ipaddrs:0083 - lo - ('::1', 0, 0)/128
[12843/12844] sysinfo_api.py|os_net_ipaddrs:0083 - enp0s3 - 192.168.31.17/24
[12843/12844] sysinfo_api.py|os_net_ipaddrs:0083 - enp0s3 - ('fe80::6cc1:75e9:876c:43e9', 0, 2)/64
[12843/12844] sysinfo_api.py|os_net_ipaddrs:0083 - enp0s8 - 192.168.56.101/24
[12843/12844] sysinfo_api.py|os_net_ipaddrs:0083 - enp0s8 - ('fe80::c5d3:c65a:1734:9ae8', 0, 3)/64
[12843/12844] sysinfo_api.py|os_net_ipaddrs:0083 - docker0 - 172.17.0.1/16
--------------------------------------------------------------------------------
[12843/12844] sysinfo_api.py|sysinfo_show_watch:0114 - (cpu_usage: [0.0, 0.0])
[12843/12844] sysinfo_api.py|sysinfo_show_watch:0115 - (cpu_loadavg: (0.09, 0.09, 0.05))
[12843/12844] sysinfo_api.py|sysinfo_show_watch:0116 - (cpu_count: 2)
[12843/12844] sysinfo_api.py|sysinfo_show_watch:0117 - (cpu_num: 1)
[12843/12844] sysinfo_api.py|sysinfo_show_watch:0119 - (cpu_freq: 2419.2, min: 0.0, max: 0.0)
[12843/12844] sysinfo_api.py|sysinfo_show_watch:0128 - (disk_usage: 37.1 %)
[12843/12844] sysinfo_api.py|sysinfo_show_watch:0130 - (mem_total: 4102107136 bytes, mem_usage: 23.4 %)
[12843/12844] sysinfo_api.py|sysinfo_show_watch:0134 - (battery: 60.0 %, secsleft: 00:00:00, AC: True)
[12843/12844] sysinfo_api.py|sysinfo_show_watch:0141 - (fans: {})
[12843/12844] threadx_api.py|threadx_sleep:0067 - call wait ... (timeout: 5)
[12843/12843] threadx_api.py|threadx_wakeup:0061 - call notify ...
[12843/12844] sysinfo_api.py|threadx_handler:0189 - Bye-Bye !!!
[12843/12843] sysinfo_api.py|release:0197 - Done.
[12843/12843] sysinfo_123.py|app_release:0061 - Enter ...
[12843/12843] sysinfo_123.py|app_release:0066 - call sysinfo_ctx.release ...
[12843/12843] sysinfo_123.py|app_release:0070 - Done.
[12843/12843] sysinfo_123.py|app_exit:0081 - Done.
[12843/12843] sysinfo_123.py|main:0131 - Bye-Bye !!! (app_quit_get: 1)
```
## - youtube_123.py - a streamlink example.

>使用 streamlink  api 方式下載 youtube 影片

```bash
$ make youtube_123

==> python 3.12 - run: youtube_123
#PYTHONPATH=/work/codebase/lankahsu520/utilsP9/python python -m utilsP9.youtube_123 -d 4
./youtube_123.py -d 4
[12838/12838] utilsP9.py|argsX_dump:0057 - {}
[12838/12838] youtube_123.py|app_start:0041 - (Python version: 3.12.11, chkPYTHONge(3,8,0): True, chkPYTHONle(3,8,0): False)
[12838/12838] streamlink_api.py|streams_urlparse:0031 - (stream_url: https://www.youtube.com/watch?v=a_9_38JpdYU)
[12838/12838] streamlink_api.py|streams_urlparse:0032 - (urlparse: ParseResult(scheme='https', netloc='www.youtube.com', path='/watch', params='', query='v=a_9_38JpdYU', fragment=''))
[12838/12838] streamlink_api.py|streams_choice:0051 - (quality: 360p / dict_keys(['360p', 'worst', 'best']))
[12838/12838] streamlink_api.py|streams_savetofile:0080 - (filename: ./240p.mp4, chunksize:1024)
./240p.mp4: 47,866,053 bytes

[12838/12838] streamlink_api.py|streams_streaming:0069 - Download complete !!!
[12838/12838] youtube_123.py|app_release:0062 - Enter ...
[12838/12838] youtube_123.py|app_release:0067 - call streamlink_ctx.release ...
[12838/12838] youtube_123.py|app_release:0071 - Done.
[12838/12838] youtube_123.py|app_exit:0082 - Done.
[12838/12838] youtube_123.py|main:0127 - Bye-Bye !!! (app_quit_get: 1)
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

> [utilsP9](https://github.com/lankahsu520/utilsP9) is under the New BSD License (BSD-3-Clause).
