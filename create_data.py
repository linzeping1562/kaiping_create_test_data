import add_administrative_class
import add_building
import add_lesson
import add_major
import add_place_to_every_building
import add_place_to_same_building
import add_subject
import add_teacher
import colleage_add_stu
import k12_add_stu
choice=input("请选择你想造的数据类型:\n \
A.生成导入k12学段学生的excel文件\n \
B.生成导入大学学段学生的excel文件\n \
C.生成导入老师的excel文件\n \
D.生成在同一建筑下导入多个场地的excel文件\n \
E.生成在学校下所有建筑都导入多个场地的excel文件\n \
F.生成导入专业的excel文件\n \
G.生成导入走班课程的excel文件\n \
H.生成导入行政班课程的excel文件\n \
I.接口添加多个科目\n \
J.接口添加多个建筑\n")
if choice.upper()=='A':
    k12_add_stu.add_k12_stu()
if choice.upper()=='B':
    colleage_add_stu.add_colleage_stu()
if choice.upper()=='C':
    add_teacher.add_teacher()
if choice.upper()=='D':
    add_place_to_same_building.add_place()
if choice.upper()=='E':
    add_place_to_every_building.add_place()
if choice.upper()=='F':
    add_major.add_major()
if choice.upper()=='G':
    add_lesson.add_lesson()
if choice.upper()=='H':
    add_administrative_class.add_lesson()
if choice.upper()=='I':
    add_subject.add_subject()
if choice.upper()=='J':
    add_building.add_building()
