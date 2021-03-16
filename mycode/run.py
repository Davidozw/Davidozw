"""
File:    run
Author:  ouzongwei
Time:   2021/3/14 20:08
Ide_name:PyCharm
"""
import unittest
from http_case.http_testcase import Http_case
from http_case import http_testcase
import HtmlTestRunner
from tools.do_excel import Do_excel

# test_data=[{'url':'http://japi.juhe.cn/qqevaluate/qq','data':{'key':'0f7267864a57acb201844d080b98f519','qq':'1986273879'},'method':'get'},
#            {'url':'http://japi.juhe.cn/qqevaluate/qq','data':{'key':'0f7267864a57acb201844d080b98f519','qq':'1197253792'},'method':'get'},
#            {'url':'http://japi.juhe.cn/qqevaluate/qq','data':{'key':'0f7267864a57acb201844d080b98f519','qq':'1986273878'},'method':'get'}
#            ]
filename=r'E:\mycode\test_data\testdata.xlsx'
sheetname='python'
test_data=Do_excel(filename,sheetname).getdata()
#第一种方法
#收集用例
suite=unittest.TestSuite()
# suite.addTest(Http_case('test_api'))
# runner=unittest.TextTestRunner()
# runner.run(suite)
# loader=unittest.TestLoader()
# suite.addTest(loader.loadTestsFromTestCase(Http_case))
for item in test_data:
    suite.addTest(Http_case('test_api',item['url'],eval(item['data']),item['method']))
with open(r'./report/test.html','wb') as f:

    runner=HtmlTestRunner.HTMLTestRunner(stream=f,verbosity=2,title='Mr.ou test report',description='first report',tester='ouzongwei')
    runner.run(suite)

