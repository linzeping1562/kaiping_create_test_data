import xlwt
def add_teacher():
    num=input("请输入你要添加的老师数量:")
    phone_fore=input("请输入手机号首位后的前几位（1至5位数字):")
    id_fore=input("请输入身份证号前缀（1至13位数字):")
    card_fore=input("请输入卡号前缀（1至27位数字或字符):")
    n=input("请输入老师名称前缀：")
    name=[]
    phones=[]
    id_cards=[]
    card_nums=[]
    i=1
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('sheet1')
    worksheet.write(0, 0, label="teacher_name")
    worksheet.write(0, 1, label="phone")
    worksheet.write(0, 2, label="id_card")
    worksheet.write(0, 3, label="sex")
    worksheet.write(0, 4, label="birthday")
    worksheet.write(0, 5, label="card_num")
    y=1
    for i in range(0,int(num)): 
        name.append(n+str(i))
        phone="1"+phone_fore+ str(i).zfill(10-len(phone_fore))
        phones.append(phone)
        id_card=id_fore+str(i).zfill(18-len(id_fore))# 此处每次导入需对应修改前缀和填充0的位数，已满足身份证号的唯一性
        id_cards.append(id_card)
        card_num=card_fore+ str(i).zfill(32-len(card_fore))# 此处的卡号前缀"t"可自行修改，避免和学生的重复
        card_nums.append(card_num)
    for i in range(0,int(num)):
        worksheet.write(y, 0, label=name[i])
        worksheet.write(y, 1, label=phones[i])
        worksheet.write(y, 2, label=id_cards[i])
        worksheet.write(y, 5, label=card_nums[i])
        y=y+1
    workbook.save('D:\Excel_Workbook.xls')
