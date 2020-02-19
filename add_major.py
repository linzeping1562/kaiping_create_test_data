import xlwt
def add_major():
    num1=input("请输入你要添加的学院数量:")
    num2=input("请输入你要添加的每个学院的专业数:")
    academy_name=input("请输入学院名称前缀:")
    major_name=input("请输入专业名称前缀:")
    xueyuan=[]
    zhuanye=[]
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('sheet1')
    worksheet.write(0, 0, label="academy")
    worksheet.write(0, 1, label="major")
    y=1
    for i in range(0,int(num1)): 
        n=academy_name+str(i)
        xueyuan.append(n)
    for i in range(0,int(num1)*int(num2)):
        zhuanye.append(major_name+str(i))
    for i in range(0,int(num1)):
        for j in range(0,int(num2)):
            worksheet.write(y, 0, label=xueyuan[i])
            worksheet.write(y, 1, label=zhuanye[j+i*int(num2)])
            y=y+1
    workbook.save('D:\Excel_Workbook.xls')
