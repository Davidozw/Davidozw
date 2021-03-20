"""
File:    do_conf
Author:  Mr.ou
Time:   2021/3/15 20:34
Ide_name: PyCharm
"""
import configparser
from common.path_file import *
from common.G_data import Data_common

class Do_conf:

    def config_data(self,filename,section,option):
        cf = configparser.ConfigParser()
        cf.read(filename,encoding='utf-8')
        return cf[section][option]

if __name__ == '__main__':
    filename=conf_path
    # section='MODE'
    # option = 'mode'
    dd=Do_conf().config_data(conf_path,getattr(Data_common,'section'),getattr(Data_common,'option'))
    print(dd)