class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'


my = MyClass()
#print(locals())
#print(globals())
print(MyClass.method(my))

print(MyClass.classmethod())

# does not need an instance to be called
print(MyClass.staticmethod())
print(my.staticmethod())