"""
File:    http_request
Author:  ouzongwei
Time:   2021/3/14 20:09
Ide_name:PyCharm
"""

import requests


class Http_method:

    def http_request(self,url,data,method,header=None,cookie=None):

        if method.lower() == 'get':
            res=requests.get(url,data,headers=header,cookies=cookie,verify=False)
        elif method.lower() == 'post':
            res=requests.post(url,data,headers=header,cookies=cookie,verify=False)
        else:
            print('method is unsuport')
        return res

if __name__ == '__main__':
    pass
