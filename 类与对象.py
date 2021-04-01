class employee:
    id = 0
    name = 'zx'

class company:
    def __init__(self):
        self.employeer = employee()


class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __call__(self, *args, **kwargs):
        return args[0], args[1]


p = People('zhangxv', 19)
print(p('zhangxv', 'hello'))
