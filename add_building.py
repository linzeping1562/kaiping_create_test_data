import requests
import json
import xlwt
import xlrd
def add_building():
    num=input("请输入你想添加的建筑数量：")
    build_name=input("请输入建筑名称前缀：")
    school_uid=input("请输入学校id")
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('sheet1')
    worksheet.write(0, 0, label="building_name")
    y=1
    for i in range(0,int(num)): 
        n=build_name+str(i)
        worksheet.write(y, 0, label=n)
        y=y+1
    workbook.save('D:\\add_building.xls')
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
    excel = xlrd.open_workbook('D:\\add_building.xls')
    sheet = excel.sheets()[0]
    nrows = sheet.nrows
    a=[]
    for i in range (1,nrows):
        a.append(sheet.row_values(i)[0])
    url="http://coopen.test.seewo.com/admin/apis.json?action=POST_API_BUILDING_V1&timestamp=1576552704840"
    headers={
        'Content-Type': 'application/json;charset=UTF-8',
        'Cookie': 'x-auth-token=%s'%token
        }
    for building_name in a:    
        request_param={
            "params":{
                "buildingName":building_name,
                "rangeLevel":0,
                "parentBuildingUid":school_uid,
                "unitId":school_uid,
                "managerQueryList":[]
                }
            }
        response = requests.post(url, data=json.dumps(request_param), headers=headers,verify=False)

