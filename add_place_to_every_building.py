#utf-8
import sys
import xlwt
import pymysql
def add_place():
    a = input("请输入你想要的每栋建筑下的场地数: ")
    place_name=input("请输入你想要的场地名称前缀:")
    place_num=int(a)
    name=[]
    conn=pymysql.connect(host='sr-test-mysql-master-1.gz.cvte.cn',user='seewo',password='seewo@cvte',db='seewo_opener_server')
    mycursor=conn.cursor()
    sql='SELECT c_name FROM seewo_opener_server.t_area_building where c_unit_uid="8c2da8466c93eacddd2bc7fa33a545eb" and c_is_deleted=0'
    build_num=mycursor.execute(sql)
    rs = mycursor.fetchall()
    build_names=[]
    for i in range(0,build_num):
        t=str(rs[i]).strip('(,)')
        t=t.strip("'")
        build_names.append(t)
    #print(build_name)
    conn.commit()
    mycursor.close()
    conn.close()
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
    for i in range(0,place_num*build_num):
        n=place_name+ str(i)
        name.append(n)
    for j in range(0,build_num):
        for i in range(0,place_num):
            worksheet.write(y, 0, label=build_names[j])
            worksheet.write(y, 1, label=name[i+j*place_num])
            y=y+1
    workbook.save('D:\Excel_Workbook.xls')



