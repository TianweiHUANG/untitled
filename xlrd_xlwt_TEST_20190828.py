
import xlrd
#打开xls文件
workbook=xlrd.open_workbook("xlrd_xlwt_TEST_20190828.xls")
print("表单数量:",workbook.nsheets)
print("表单名称:",workbook.sheet_names())

#获取第1个表单
sheet1=workbook.sheet_by_index(0)
print(u"表单%s共%d行%d列"%(sheet1.name,sheet1.nrows,sheet1.ncols))
print("第二行第三列:",sheet1.cell_value(1, 2))

#遍历所有表单
for s in workbook.sheets():
    for r in range(s.nrows):
        #输出指定行
        print(s.row(r))

"""
import xlwt
#创建xls文件对象
workbook=xlwt.Workbook()
#新增一个表单
sheet1=workbook.add_sheet("sheet1")
#按位置添加数据
sheet1.write(0,0,1234.56)
sheet1.write(1,0,8888)
sheet1.write(2,0,"hello")
sheet1.write(2,1,"world")
#保存xls文件
workbook.save("xlrd_xlwt_DOME_20190828.xls")
"""
"""
from xlrd import open_workbook
from xlutils.copy import copy

#打开xls文件
workbook=open_workbook("xlrd_xlwt_TEST_20190828.xls")
#获取第1个表单
sheet1=workbook.sheet_by_index(0)
print("第二行第三列:",sheet1.cell_value(1,2))

#复制xls文件
copy_workbook=copy(workbook)
#获取第1个表单
copy_sheet1=copy_workbook.get_sheet(0)
#第二行第三列写入数据
copy_sheet1.write(1,2,sheet1.cell_value(1,2)-1)
#保存xls文件
copy_workbook.save("xlrd_xlwt_TEST_20190828.xls")
"""
