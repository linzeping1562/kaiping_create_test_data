import xlwt
def add_k12_stu():
    name=[]
    stu_code=[]
    card_num=[]
    xueduan=input("请输入你要生成的学生所属学段（小学、初中、高中）:")
    grade= input("请输入你要生成的学生所属年级:")
    class_name=input("请输入你要生成的学生所属班级（如1班）:")
    num=input("请输入你要生成的学生数量:")
    n=input("请输入学生名称前缀:")
    stu_num=input("请输入学生学号前缀:")
    card=input("请输入学生卡号前缀（1到27位均可）:")
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('sheet1')
    worksheet.write(0, 0, label="xueduan")
    worksheet.write(0, 1, label="grade")
    worksheet.write(0, 2, label="class")
    worksheet.write(0, 3, label="stu_name")
    worksheet.write(0, 4, label="stu_code")
    worksheet.write(0, 5, label="parent_name")
    worksheet.write(0, 6, label="parent_phone")
    worksheet.write(0, 7, label="card_num")
    y=1
    for i in range(0,int(num)):
        na=n+str(i)
        name.append(na)
        stu_nums=stu_num+str(i)
        stu_code.append(stu_nums)
        s=card+str(i).zfill(32-len(card))
        card_num.append(s)
    for i in range(0,int(num)):
        worksheet.write(y, 0, label=xueduan) 
        worksheet.write(y, 1, label=grade)
        worksheet.write(y, 2, label=class_name)
        worksheet.write(y, 3, label=name[i])
        worksheet.write(y, 4, label=stu_code[i])
        worksheet.write(y, 7, label=card_num[i])
        y=y+1
    workbook.save('D:\Excel_Workbook.xls')#文件存储路径可自行修改成你自己想修改的路径
