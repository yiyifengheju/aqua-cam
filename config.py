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
import platform

import toml

# 配置信息
config = toml.load('./config.toml')


class INIT:
    SYSTEM = platform.system()
    AUTHOR = '👨‍💻一一风和橘&ensp;&ensp;👾v0.1.0&ensp;&ensp;🕗20240513'
    THEME = config['THEME']
    MAX_WORKERS = int(config['MAX_WORKERS'])
