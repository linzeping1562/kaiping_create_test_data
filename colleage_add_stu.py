import xlwt
def add_colleage_stu():
    name=[]
    stu_code=[]
    card_num=[]
    xueyuan=input("请输入你要生成的学生所属学院:")
    zhuangye= input("请输入你要生成的学生所属专业:")
    year=input("请输入你要生成的学生入学年份:")
    class_name=input("请输入你要生成的学生所属班级（如1班）:")
    num=input("请输入你要生成的学生数量:")
    n=input("请输入学生名称前缀:")
    stu_num=input("请输入学生学号前缀:")
    card=input("请输入学生卡号前缀（1到27位均可）:")
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('sheet1')
    worksheet.write(0, 0, label="xueduan")
    worksheet.write(0, 1, label="xueyuan")
    worksheet.write(0, 2, label="major")
    worksheet.write(0, 3, label="start_year")
    worksheet.write(0, 4, label="class")
    worksheet.write(0, 5, label="stu_name")
    worksheet.write(0, 6, label="stu_code")
    worksheet.write(0, 7, label="parent_name")
    worksheet.write(0, 8, label="parent_phone")
    worksheet.write(0, 9, label="card_num")
    y=1
    for i in range(0,int(num)): 
        na=n+str(i)
        name.append(na)
        stu_nums=stu_num+str(i)
        stu_code.append(stu_nums)
        s=card+str(i).zfill(32-len(card))
        card_num.append(s)
    for i in range(0,int(num)):
        worksheet.write(y, 0, label="大学")
        worksheet.write(y, 1, label=xueyuan) 
        worksheet.write(y, 2, label=zhuangye)
        worksheet.write(y, 3, label=int(year))
        worksheet.write(y, 4, label=class_name)
        worksheet.write(y, 5, label=name[i])
        worksheet.write(y, 6, label=stu_code[i])
        worksheet.write(y, 9, label=card_num[i])
        y=y+1
    workbook.save('D:\Excel_Workbook.xls')
