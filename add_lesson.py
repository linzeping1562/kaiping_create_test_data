#utf-8
import sys
import xlwt
def add_lesson():
    num = input("请输入你想要的走班课程数量:")
    lesson_name=input("请输入你想要的走班课程名称前缀:")
    subject=input("请输入走班课程所属科目：")
    name=[]
    stu_code=[]
    i=1
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('sheet1')
    worksheet.write(0, 0, label="subject")
    worksheet.write(0, 1, label="class")
    worksheet.write(0, 2, label="lesson_name")
    worksheet.write(0, 3, label="teacher")
    worksheet.write(0, 4, label="phone")
    y=1
    for i in range(0,int(num)):
        na=lesson_name+str(i)
        name.append(na)
    for names in name:
        worksheet.write(y, 0, label=subject)
        worksheet.write(y, 2, label=names)
        y=y+1
    workbook.save('D:\Excel_Workbook.xls')
