class Foo:
    def __init__(self, x = None):
        self.__x = x

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x += x

    @x.deleter
    def x(self):
        self.__x = -20


foo = Foo(10)
print(foo.x)
foo.x = 10
print(foo.x)
del foo.x
print(foo.x)