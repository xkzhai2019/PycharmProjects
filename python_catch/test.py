# coding:utf-8


'''
    学生信息库
'''
class NotArgError(Exception):
    def __int__(self,message):
        self.message = message

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
        try:
            self.check_user_info(**kwargs) # TODO: 添加异常捕获
        except Exception as e:
            raise e
        self.__add(**kwargs)

    def adds(self,new_students):
        for student in new_students:
            try:
                self.check_user_info(**student)
            except Exception as e:
                print(e,student.get('name'))
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

    def deletes(self,ids):
        for id_ in ids:
            if id_ not in self.students:
                print(f'{id_}不在学生库中')
                continue
            student_info = self.students.pop(id_)
            print(f'学号{id_} 学生{student_info['name']} 已被删除')

    def update(self,student_id, **kwargs):
        if student_id not in self.students:
            print('不存在学号:{}'.format(student_id))
            return
        try:
            self.check_user_info(**kwargs)#
        except Exception as e:
            raise e
        self.students[student_id] = kwargs
        print('信息已更新')

    def updates(self,update_students):
        for student in update_students:
            try:
                id_ = list(student.keys())[0] #
            except IndexError as e:
                print(e)
                continue
            if id_ not in self.students:
                print(f'学号{id_}不存在')
                continue
            user_info = student[id_]
            try:
                self.check_user_info(**user_info)#
            except Exception as e:
                print(e)
                continue
            self.students[id_] = user_info
        print('所有用户信息更新完成！')

    def search_users(self,**kwargs):
        assert len(kwargs)==1, '参数数量传递错误'
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
            raise NotArgError('没有发现搜索的关键字')
        for user in values:
            if value in user[key]:
                ret.append(user)
        return ret

    def check_user_info(self,**kwargs):
        assert len(kwargs) == 4, '参数必须是4个'
        if 'name' not in kwargs:
            raise NotArgError('缺少学生姓名')
        if 'age' not in kwargs:
            raise NotArgError('缺少学生年龄')
        if 'sex' not in kwargs:
            raise NotArgError('缺少学生性别')
        if 'class_num' not in kwargs:
            raise NotArgError('缺少学生班级')
        name_value = kwargs['name']
        age_value = kwargs['age']
        sex_value = kwargs['sex']
        class_num_value = kwargs['class_num']
        # isInstance(对比的数据，目标类型）isInstance(1,str)
        if not isinstance(name_value,str):
            raise TypeError('name应该是字符串类型')
        if not isinstance(age_value,int):
            raise TypeError('age应该是整型')
        if not isinstance(sex_value,str):
            raise TypeError('sex应该是字符串类型')
        if not isinstance(class_num_value,str):
            raise TypeError('class_num应该是字符串类型')

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
    print("----------------------")
    student_info.deletes([7,8])
    student_info.get_all_students()
    print("----------------------")

    student_info.updates([
        {1:{'name':'dewei zhang','age':18,'class_num':'B','sex':'boy'}},
        {2: {'name': 'dewei zhang', 'age': 28, 'class_num': 'B'}}
    ])
    student_info.get_all_students()

    ret = student_info.search_users(name='')
    print(ret)





















