from student import Student


class StudentManger(object):
    # 类属性，相当于类的全局变量。
    student_list = []

    # 静态方法，相当于
    @staticmethod
    def __menu_Manager():  # 静态方法不需要self参数。
        # 0、入口提示菜单
        print('-' * 40)
        print('[1] 增加学生信息')
        print('[2] 删除学生信息')
        print('[3] 修改学生信息')
        print('[4] 查询学生信息')
        print('[5] 显示所有学生信息')
        print('[6] 保存学生信息')
        print('[7] 退出学生信息管理系统')
        print('-' * 40)

    def __load_data(self):
        # 在使用系统开始的时候加载数据库中的数据
        try:
            self.file = open(file='students.data', mode='r', encoding='utf-8')
        except FileNotFoundError:
            self.file = open(file='students.data', mode='w', encoding='utf-8')
        else:
            content = self.file.read()
            if len(content) >= 1:
                data = eval(content)
                # 将序列实例化对象。
                self.student_list = [Student(i['no'], i['name'], i['sex'], i['age'], i['mobile']) for i in data]
        finally:
            self.file.close()

    def __add_student(self):
        # 1、增加学生信息
        no = input('请输入学生的编号：')
        for element in self.student_list:
            if element.no == no:
                print('\n您要添加的学生编号已存在，请重新编号。')
                break
        else:
            name = input('请输入学生的姓名：')
            sex = input('请输入学生的性别：')
            age = input('请输入学生的年龄：')
            mobile = input('请输入学生的电话：')
            # # 错误的实例化方法
            # student = student.Student
            # student(no, name, sex, age, mobile)  # 错误的实例化方法，没有实例化实参。
            # self.student_list.append(student)
            # print(self.student_list)  # 结果：[<class 'student.Student'>]
            # print(student)  # 结果：<class 'student.Student'>
            # 正确的实例化方法
            student = Student(no, name, sex, age, mobile)  # 实例化时要同时定义实参，
            # print(student)  # 结果：编号：1，姓名：1，性别：1，年龄：1，电话：1。
            # print(student)  # student.Student没有__str__，返回自身，结果：<student.Student object at 0x000002D8443DFC88>
            # print(type(student))  # 返回实例对象student的类，<class 'student.Student'>
            self.student_list.append(student)
            # print(self.student_list)  # 结果：[<student.Student object at 0x00000178A056FC88>]
            # self.student_list.append(11)  # student_list再追加一个元素。
            # print(self.student_list)  # 结果：[<student.Student object at 0x000001E9639CFC88>, 11]
            # print(type(self.student_list))  # 返回实例对象self.student_list的类，<class 'list'>
            # print(type(self.student_list[0]))  # 返回实例对象self.student_list[0]的类，<class 'student.Student'>
            print('\n通知：学生信息已增加成功。')

    def __del_student(self):
        # 2、删除学生信息
        no = input('请输入需要删除的学生的编号：')
        for element in self.student_list:
            if element.no == no:
                self.student_list.remove(element)
                print('\n学生信息删除成功。')
                break
        else:
            print('\n您要删除的学生信息不存在...')

    def __modify_student(self):
        # 3、修改学生信息
        no = input('请输入需要修改的学生的编号：')
        for element in self.student_list:
            if element.no == no:
                element.no = input('请输入修改后的编号：')
                element.name = input('请输入修改后的姓名：')
                element.sex = input('请输入修改后的性别：')
                element.age = input('请输入修改后的年龄：')
                element.mobile = input('请输入修改后的手机：')
                print('\n学生信息修改成功。')
                break
        else:
            print('\n您要删除的学生信息不存在...')

    def __show_student(self):
        # 4、查询学生信息
        no = input('请输入需要查询的学生的编号：')
        for element in self.student_list:
            if element.no == no:
                print(element)
                break
        else:
            print('\n您要查询的学生信息不存在...')

    def __show_all(self):
        # 5、查询所有学生信息
        for element in self.student_list:
            print(element)

    def __save_students(self):
        # 6、保存学生信息
        file = open(file='students.data', mode='w', encoding='utf-8')
        # object.__dict__能将对象转换为 key=属性名:value=属性值 字典。
        save_list = [element.__dict__ for element in self.student_list]  # 在[]内使用推导式增加元素，不需要用append方法。
        file.write(str(save_list))
        file.close()
        print('\n学生信息保存成功。')

    def Manager_server(self):
        # 7、学生管理系统接口
        self.__load_data()
        while True:
            self.__menu_Manager()  # 运行接口之前首先运行提示菜单。
            user_num = int(input('请选择您需要进行的操作：'))

            if user_num == 1:
                self.__add_student()

            elif user_num == 2:
                self.__del_student()

            elif user_num == 3:
                self.__modify_student()

            elif user_num == 4:
                self.__show_student()

            elif user_num == 5:
                self.__show_all()

            elif user_num == 6:
                self.__save_students()

            elif user_num == 7:
                print('感谢使用学生信息管理系统V2.0...')
                break

            else:
                print('您输入的操作有误，请重新输入')


# 主模块调试代码
if __name__ == '__main__':
    system = StudentManger()
    system.Manager_server()
