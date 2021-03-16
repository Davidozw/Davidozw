"""
File:    do_excel
Author:  ouzongwei
Time:   2021/3/14 23:47
Ide_name:PyCharm
"""
from openpyxl import load_workbook


class Do_excel:
    def __init__(self,filename,sheetname):
        self.filename=filename
        self.sheetname=sheetname
        self.wb=load_workbook(self.filename)
        self.sheet=self.wb[self.sheetname]
    def get_header(self):
        '''获取第一行的标题行'''
        header=[]

        for line in range(1,self.sheet.max_column+1):
            header.append(self.sheet.cell(1,line).value)
        return header

    def getdata(self,mode='all'):
        # wb=load_workbook(filename)
        # sheet=wb[sheetname]
        test_data=[]
        header=self.get_header()
        # header=['case_id','url','data','method']
        # for i in range(1,sheet.max_column):
        #     print(sheet.cell(1,i).value)
        for i in range(2,self.sheet.max_row+1):
            data = {}
            for j in range(1,self.sheet.max_column):
                data[header[j-1]]=self.sheet.cell(i,j).value
            test_data.append(data)
        if mode == 'all':
            fina_data=test_data
        else:
            fina_data=[]
            for item in test_data:
                if item['case_id'] in mode:
                    fina_data.append(item)
        return fina_data

if __name__ == '__main__':
    filename=r'E:\mycode\test_data\testdata.xlsx'
    sheetname='python'
    mode=[1,2,3]
    td=Do_excel(filename,sheetname).getdata(mode)
    # hd=Do_excel(filename,sheetname).get_header()
    print(td)
    # print(hd)