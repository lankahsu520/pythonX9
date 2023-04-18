# 1. Overview

pythonX9 把常用的工具集合在一起，並且將呼叫簡單化。

# 2. Depend on

# 3. Current Status


# 4. Build
```bash

```
# 5. Example or Usage

- dummy_123 - 一個簡單的範本。請善用 DBG_XX_LN.
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
	signal.->signal_handler
	
	parse_arg-->show_usage
	app_start-->app_watch
	app_stop-->app_release-->End
```

```bash
$ ./dummy_123.py -d2
[dummy_123.py|app_start:0015] - (Python version: 3.8.10, chkPYTHONge(3,7,0): True, chkPYTHONle(3,7,0): False)
[dummy_123.py|app_start:0019] - (IFACE: enp0s3, STATIC_MAC: 08:00:27:a1:f8:36, STATIC_IP: 192.168.0.92)
[dummy_ctx][dummy_api.py|dummy_init:0011] - enter
[dummy_123.py|app_exit:0053] - enter
[dummy_123.py|app_stop:0046] - enter
[dummy_123.py|app_release:0033] - enter
[dummy_123.py|app_release:0038] - call dummy_ctx.release ...
[dummy_ctx][dummy_api.py|release:0007] - enter
[dummy_123.py|main:0103] - bye bye !!! (is_quit: 1)

```
- sysinfo_123 - 查找主機系統資訊，每5秒刷新畫面
```bash
$ ./sysinfo_123.py -d 4
[sysinfo_ctx][sysinfo_api.py|keyboard_recv:0163] - press q to quit the loop ...
[sysinfo_ctx][sysinfo_api.py|os_net_ipaddrs:0066] - lo - 127.0.0.1/8
[sysinfo_ctx][sysinfo_api.py|os_net_ipaddrs:0066] - lo - ('::1', 0, 0)/128
[sysinfo_ctx][sysinfo_api.py|os_net_ipaddrs:0066] - enp0s3 - 10.0.2.15/24
[sysinfo_ctx][sysinfo_api.py|os_net_ipaddrs:0066] - enp0s3 - ('fe80::7549:bd5f:d0ed:32cf', 0, 2)/64
[sysinfo_ctx][sysinfo_api.py|os_net_ipaddrs:0066] - enp0s9 - 192.168.56.104/24
[sysinfo_ctx][sysinfo_api.py|os_net_ipaddrs:0066] - enp0s9 - ('fe80::e6d1:c758:6c5c:4cbd', 0, 4)/64
[sysinfo_ctx][sysinfo_api.py|os_net_ipaddrs:0066] - docker0 - 172.17.0.1/16
[sysinfo_ctx][sysinfo_api.py|os_net_ipaddrs:0066] - enp0s8 - ('fe80::d49:8acb:9f1b:c4cf', 0, 3)/64
[sysinfo_ctx][sysinfo_api.py|sys_info_show_watch:0094] - --------------------------------------------------------------------------------
[sysinfo_ctx][sysinfo_api.py|sys_info_show_watch:0097] - (cpu_usage: [0.0, 0.0, 0.0, 0.0])
[sysinfo_ctx][sysinfo_api.py|sys_info_show_watch:0098] - (cpu_loadavg: (0.07, 0.06, 0.02))
[sysinfo_ctx][sysinfo_api.py|sys_info_show_watch:0099] - (cpu_count: 4)
[sysinfo_ctx][sysinfo_api.py|sys_info_show_watch:0100] - (cpu_num: 3)
[sysinfo_ctx][sysinfo_api.py|sys_info_show_watch:0102] - (cpu_freq: 2808.0, min: 0.0, max: 0.0)
[sysinfo_ctx][sysinfo_api.py|sys_info_show_watch:0111] - (disk_usage: 17.4 %)
[sysinfo_ctx][sysinfo_api.py|sys_info_show_watch:0113] - (mem_total: 8335740928 bytes, mem_usage: 11.7 %)
[sysinfo_ctx][sysinfo_api.py|sys_info_show_watch:0117] - (battery: 80.0 %, secsleft: 00:00:00, AC: True)
[sysinfo_ctx][sysinfo_api.py|sys_info_show_watch:0124] - (fans: {})
[sysinfo_123.py|app_release:0031] - enter
[sysinfo_123.py|app_release:0036] - call sysinfo_ctx.release ...
[sysinfo_123.py|main:0105] - bye bye !!! (is_quit: 1)

```



# 6. License

pythonX9 is under the New BSD License (BSD-3-Clause).


# 7. Documentation
Run an example and read it.
