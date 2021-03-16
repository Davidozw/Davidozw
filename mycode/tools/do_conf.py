"""
File:    do_conf
Author:  Mr.ou
Time:   2021/3/15 20:34
Ide_name: PyCharm
"""
import configparser

class Do_conf:

    def __init__(self,filename,section,option):
        self.filename = filename
        self.section = section
        self.option = option

    def config_data(self):
        cf = configparser.ConfigParser()
        cf.read(self.filename,encoding='utf-8')
        return cf[self.section][self.option]

if __name__ == '__main__':
    filename=r'E:\mycode\test_data\config.ini'
    section='MODE'
    option = 'mode'
    dd=Do_conf(filename,section,option).config_data()
    print(dd)