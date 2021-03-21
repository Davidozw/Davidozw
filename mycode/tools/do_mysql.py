"""
File:    ddo_mysql
Author:  Mr.ou
Time:   2021/3/20 21:10
Ide_name: PyCharm
"""

import mysql.connector
#创建一个数据库连接
cnn=mysql.connector.connect()
#传入配置信息
confif={'host':'db4free.net',
        'user':'ozwtest',
        'password':'Changeme_123',
        'port':3306,
        'database':'1111'}