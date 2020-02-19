#utf-8
import sys
import requests
import json
import xlwt
import xlrd
import pymysql
def add_subject():
    num = input("请输入你想要的科目数量（数量不要超大，怕服务会崩）: ")
    subject=input("请输入你想要的科目名称前缀:")
    unit_id=input("请输入你的学校uid:")
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('sheet1')
    worksheet.write(0, 0, label="building_name")
    y=1
    for i in range(0,int(num)): 
        n=subject+str(i)
        worksheet.write(y, 0, label=n)
        y=y+1
    workbook.save('D:\\add_subject.xls')
    url = "http://coopen.test.seewo.com/admin/login"
    headers = {'Content-Type': 'application/json;charset=UTF-8'}
    request_param ={
        "account":"13719444867",
        "password":"0659c7992e268962384eb17fafe88364",
        "platform":"web",
        "rememberMe":True
        }
    response = requests.post(url, data=json.dumps(request_param), headers=headers,verify=False)
    token = response.json()["data"]["token"]
    excel = xlrd.open_workbook('D:\\add_subject.xls')
    sheet = excel.sheets()[0]
    nrows = sheet.nrows
    a=[]
    for i in range (1,nrows):
        a.append(sheet.row_values(i)[0])
    url="http://coopen.test.seewo.com/admin/apis.json?action=POST_API_SUBJECT_V1_SUBJECT&timestamp=1576568382345"
    headers={
        'Content-Type': 'application/json;charset=UTF-8',
        'Cookie': 'x-auth-token=%s'%token
        }
    for subject_name in a:    
        request_param={
            "params":{
                "unitId":unit_id,
                "subjectName":subject_name
                }
            }
        response = requests.post(url, data=json.dumps(request_param), headers=headers,verify=False)
        print(response.json())
