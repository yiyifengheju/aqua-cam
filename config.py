"""
=========================================================================
@File Name: config.py
@Time: 2024/5/13 上午2:55
@Program IDE：PyCharm
@Create by Author: 一一风和橘
@Motto: "The trick, William Potter, is not minding that it hurts."
@Description:
- 
- 
=========================================================================
"""
import os
import platform
import socket
import sys
import threading

import toml

# 配置信息
config = toml.load('./config.toml')


class INIT:
    SYSTEM = platform.system()
    VERSION = 'v2024.8'
    AUTHOR = f'🐸一一风和橘&ensp;&ensp;🍐{VERSION}'
    THEME = config['THEME']
    PY_EXECUTABLE = sys.executable
    PY_FILE = os.path.abspath(__file__)
    PY_VERSION = sys.version_info
    PID = os.getpid()
    TID = threading.get_ident()
    HOSTNAME = socket.gethostname()
    PLATFORM = platform.platform()
    NUM_CPUS = os.cpu_count()
    MAX_WORKERS = NUM_CPUS * 2
