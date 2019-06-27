# 导入系统的模块
import random

def add(a,b):
    return  a+b

class Father():
    # int num=0 在这里申明的叫静态属性
    # 双下划线开始和结束的函数和属性，都是系统已经定义好的，称为特殊属性和特殊方法
    # 特殊方法：在特定的场景会自动调用
    # __inti__用来初始化对象的属性，因此在创建对象时会自动调用
    def __init__(self, name):
        # self代表当前对象
        print('__init__', id(self))
        self.name = name

    def __del__(self):
        # 此方法会在对象销毁时自动执行
        print('__del__', id(self))

    def show(self):
        print('name:', self.name)

# 默认子类可以调用父类的属性和方法
# 一个下划线开始的变量认为是保护成员，子类可以访问
# 一个下划线开始的方法认为是保护方法，子类可以访问

# 两个下划线开始的变量认为是私有成员，子类不能访问
# 两个下划线开始的方法认为是私有方法，子类不能访问
class Son(Father):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age

    def show(self):
        super().show()
        print(f'Name:{self.name}, Age:{self.age}')


# 如果是当前模块自己运行，则__name__属性就是'__main__'，如果是其他的模块调用，则__name__就是当前包和模块名的组合
# 即pkg.demo01
if(__name__ == '__main__'):
    a=Son('AAA',18)