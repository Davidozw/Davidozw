"""
File:    my_log
Author:  Mr.ou
Time:   2021/3/20 18:33
Ide_name: PyCharm
"""

import logging
#设置logger
mylogger=logging.getLogger('ozw')
#设置日志收集到logger中的级别
mylogger.setLevel('DEBUG')
#设置日志输出格式
foamatter = logging.Formatter("%(asctime)s-%(filename)s-%(levelno)s-%(lineno)s, %(message)s")
#设置handlers
steam_handler = logging.StreamHandler()
file_handler = logging.FileHandler(filename='log.txt',encoding='utf-8')
steam_handler.setLevel('DEBUG')
file_handler.setLevel('DEBUG')
steam_handler.setFormatter(foamatter)
file_handler.setFormatter(foamatter)
mylogger.addHandler(steam_handler)
mylogger.addHandler(file_handler)

mylogger.debug('1111')

