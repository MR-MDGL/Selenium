import os
import openpyxl
# import XLUtils.py as utils
import XLUtils
#file-----worknook-----sheet-----rows---excel
file=r"E:\BEBO-Tech\gitSelenium\Selenium\Classwork\data driven testing\write.xlsx"

workbook=openpyxl.load_workbook(file)
sheet=workbook.active

for r in range(1,6):
    for c in range(1,6):
        sheet.cell(r,c).value="test data"
workbook.save(file)

