# coding:utf-8


'''
    学生信息库
'''

students = {
    1:{
        'name':'dewei',
        'age':33,
        'class_num':'A',
        'sex':'boy'
    },
    2: {
        'name': 'xiaomu',
        'age': 13,
        'class_num': 'A',
        'sex': 'girl'
    },
    3: {
        'name': 'xiaoman',
        'age': 18,
        'class_num': 'A',
        'sex': 'girl'
    },
    4:{
        'name': 'xiaogao',
        'age': 18,
        'class_num': 'C',
        'sex': 'boy'
    },
    5:{
        'name': 'xiaoyun',
        'age': 18,
        'class_num': 'B',
        'sex': 'girl'
    }
}

def get_all_students():
    for id_,value in students.items():
        print('学号：{}，姓名：{}，年龄：{}，性别：{}，班级：{}'.format(
            id_,value['name'],value['age'],value['sex'],value['class_num']
        ))
    return students

ret = get_all_students()
print('-----',ret)

def check_user_info(**kwargs):
    if 'name' not in kwargs:
        return '缺少学生姓名'
    if 'age' not in kwargs:
        return '缺少学生年龄'
    if 'sex' not in kwargs:
        return '缺少学生性别'
    if 'class_num' not in kwargs:
        return '缺少学生班级'
    return True

def add_student(**kwargs):
    check =  check_user_info(**kwargs)
    if check != True:
        print(check)
        return
    id_ = max(students) + 1
    students[id_] = {
        'name':kwargs['name'],
        'age': kwargs['age'],
        'sex': kwargs['sex'],
        'class_num': kwargs['class_num']
    }

def delete_student(student_id):
    if student_id not in students:
        print('{}不存在'.format(student_id))
    else:
        user_info = students.pop(student_id)
        print('学号是{}，{}同学的信息已被删除'.format(student_id,user_info['name']))

delete_student(1)
add_student(name='小美',age=18,class_num='A',sex='boy')
get_all_students()

def update_student(student_id,**kwargs):
    if student_id not in students:
        print('不存在学号:{}'.format(student_id))
        return
    check = check_user_info(**kwargs)
    if check != True:
        print(check)
        return
    students[student_id] = kwargs
    print('信息已更新')

update_student(2,name='deweidong',age=33,class_num='A',sex='boy')
get_all_students()


def get_user_byid(student_id):
    return students.get(student_id)

print(get_user_byid(3))

def search_users(**kwargs):
    values = list(students.values())
    key = None
    value = None
    ret = []
    if 'name' in kwargs:
        key = 'name'
        value = kwargs[key]
    elif 'sex' in kwargs:
        key = 'sex'
        value = kwargs[key]
    elif 'class_num' in kwargs:
        key = 'class_num'
        value = kwargs[key]
    elif 'age' in kwargs:
        key = 'age'
        value = kwargs[key]
    else:
        print('没有发现搜索的关键字')
        return
    for user in values:
        if user[key] == value:
            ret.append(user)
    return ret
print('------------')
users = search_users(sex='girl')
print(users)