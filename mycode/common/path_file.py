"""
File:    path_file
Author:  Mr.ou
Time:   2021/3/20 16:40
Ide_name: PyCharm
"""
import os

#此文件用来定义路径

#首先定义项目的绝对路径
project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

#配置测试用例的路径
data_path = os.path.join(project_path,'test_data','testdata.xlsx')

#配置文件的路径
conf_path = os.path.join(project_path,'test_data','config.ini')





if __name__ == '__main__':
    print(project_path)
    print(data_path)
    print(conf_path)