"""
File:    http_testcase
Author:  oudaxia
Time:   2021/3/14 20:15
Ide_name:PyCharm
"""


import unittest
from http_request.http_request import Http_method
import json

class Http_case(unittest.TestCase):


    def __init__(self,methodName,url,data,method):

        super(Http_case, self).__init__(methodName)
        self.url=url
        self.data=data
        self.method=method

    def setUp(self):
        print('test start')
#测试用例层
    def test_api(self):
        try:
            res=Http_method().http_request(self.url,self.data,'get')
            self.assertEqual(res.json()['error_code'],0)
            self.assertEqual(res.status_code,200)
        except Exception as e:
            print('error is {}'.format(e))
            raise e
        finally:
            print(json.dumps(res.json(),ensure_ascii=False))

    def tearDown(self):
        print('test end')

if __name__ == '__main__':
    unittest.main()