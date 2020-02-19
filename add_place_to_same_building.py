import xlwt
def add_place():
    num = input("请输入你想要的场地数量: ")
    building_name=input("请输入你想导入场地的所属建筑名称：")
    place_name=input("请输入你想要的场地名称前缀:")
    name=[]
    stu_code=[]
    card_num=[]
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('sheet1')
    worksheet.write(0, 0, label="building")
    worksheet.write(0, 1, label="place_name")
    worksheet.write(0, 2, label="related_class")
    worksheet.write(0, 3, label="floor")
    worksheet.write(0, 4, label="seating")
    worksheet.write(0, 5, label="square")
    worksheet.write(0, 6, label=" Administrator")
    worksheet.write(0, 7, label="sort")
    y=1
    for i in range(0,int(num)):
        n=place_name+ str(i)
        name.append(n)
    for i in range(0,int(num)):
        worksheet.write(y, 0, label=building_name)
        worksheet.write(y, 1, label=name[i])
        y=y+1
    workbook.save('D:\Excel_Workbook.xls')#文件存储路径可自行修改成你自己想修改的路径
