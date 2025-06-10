# coding:utf-8


'''
    学生信息库
'''

class StudentInfo(object):
    def __init__(self,students):
        self.students = students

    def get_user_byid(self,student_id):
        return self.students.get(student_id)

    def get_all_students(self):
        for id_, value in students.items():
            print('学号：{}，姓名：{}，年龄：{}，性别：{}，班级：{}'.format(
                id_, value['name'], value['age'], value['sex'], value['class_num']
            ))
        return students

    def add(self,**kwargs):
        check = self.check_user_info(**kwargs)
        if check != True:
            print(check)
            return
        self.__add(**kwargs)

    def adds(self,new_students):
        for student in new_students:
            check = self.check_user_info(**student)
            if check != True:
                print(check,student.get('name'))
                continue
            self.__add(**student)

    def __add(self,**student):
        new_id = max(self.students) + 1
        self.students[new_id] = student

    def delete(self,student_id):
        if student_id not in self.students:
            print('{}不存在'.format(student_id))
        else:
            user_info = students.pop(student_id)
            print('学号是{}，{}同学的信息已被删除'.format(student_id, user_info['name']))

    def update(self,student_id, **kwargs):
        if student_id not in self.students:
            print('不存在学号:{}'.format(student_id))
            return
        check = self.check_user_info(**kwargs)
        if check != True:
            print(check)
            return
        self.students[student_id] = kwargs
        print('信息已更新')

    def search_users(self,**kwargs):
        values = list(self.students.values())
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

    def check_user_info(self,**kwargs):
        if 'name' not in kwargs:
            return '缺少学生姓名'
        if 'age' not in kwargs:
            return '缺少学生年龄'
        if 'sex' not in kwargs:
            return '缺少学生性别'
        if 'class_num' not in kwargs:
            return '缺少学生班级'
        return True


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

if __name__=='__main__':
    student_info = StudentInfo(students)
    user = student_info.get_user_byid(1)
    print(user)
    student_info.add(name='xyz',age=34,sex='boy',class_num='A')
    print(student_info.students)
    users = [
        {'name':'xiaom','age':17,'class_num':'C','sex':'boy'},
        {'name':'xiaomei','age':18,'class_num':'D','sex':'girl'}
    ]
    student_info.adds(users)
    student_info.get_all_students()




















