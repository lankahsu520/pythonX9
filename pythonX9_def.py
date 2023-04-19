# -*- coding: utf-8 -*-

import logging

#******************************************************************************
# define
#******************************************************************************
USE_DBG_REMOTE = 0

OS_LINUX = "linux, linux2"
OS_OSX = "darwin"
OS_WINDOWS = "win32"

PYTHON_V2 = 2
PYTHON_V3 = 3

#******************************************************************************
#** DBG **
#******************************************************************************
DBG_TXT_BUSY = "Busy !!!"
DBG_TXT_BYE_BYE = "Bye-Bye !!!"
DBG_TXT_CRC_ERROR = "CRC error !!!"
DBG_TXT_DONE = "Done."
DBG_TXT_ENTER = "Enter ..."
DBG_TXT_FOUND = "Found !!!"
DBG_TXT_GOT = "Got !!!"
DBG_TXT_HELLO_WORLD = "Hello world !!!"
DBG_TXT_INIT = "Init ..."
DBG_TXT_LAUNCH_THREAD = "Launch a new thread !!!"
DBG_TXT_LINKED = "Linked !!!"
DBG_TXT_NON_IMPLEMENT = "Non-implement !!!"
DBG_TXT_NO_SUPPORT = "No support !!!"
DBG_TXT_RUN_LOOP = "Run loop ..."
DBG_TXT_START = "Start !!!"
DBG_TXT_UTF8_ERROR = "UTF-8 error !!!"
DBG_TXT_WRONG = "Wrong !!!"

#** debug **
COLOR_NONE = "\033[0m"
COLOR_RED = "\033[0;32;31m"
COLOR_LIGHT_RED = "\033[1;31m"
COLOR_GREEN = "\033[0;32;32m"
COLOR_LIGHT_GREEN = "\033[1;32m"
COLOR_BLUE = "\033[0;32;34m"
COLOR_LIGHT_BLUE = "\033[1;34m"
COLOR_DARY_GRAY = "\033[1;30m"
COLOR_CYAN = "\033[0;36m"
COLOR_LIGHT_CYAN = "\033[1;36m"
COLOR_PURPLE = "\033[0;35m"
COLOR_LIGHT_PURPLE = "\033[1;35m"
COLOR_BROWN = "\033[0;33m"
COLOR_YELLOW = "\033[1;33m"
COLOR_LIGHT_GRAY = "\033[0;37m"
COLOR_WHITE = "\033[1;37m"

logging.TRACE = logging.DEBUG-5
logging.addLevelName(logging.TRACE, 'TRACE')  
logging.trace = lambda x: logging.log(logging.TRACE, x)

DBG_LVL_CRITICAL = logging.CRITICAL # 50
DBG_LVL_ERROR = logging.ERROR # 40
DBG_LVL_WARN = logging.WARNING # 30
DBG_LVL_INFO = logging.INFO # 20
DBG_LVL_DEBUG = logging.DEBUG # 10
DBG_LVL_TRACE = logging.TRACE # 5
#DBG_LVL_MAX = 5

DBG_LVL_DEFAULT=DBG_LVL_INFO
#DBG_LVL_DEFAULT=DBG_LVL_TRACE
