class MyClass:
    "This is my second class"
    a=10
    def func(self):
        print("Hello")

# Output: 10
print(MyClass.a)

# Output: <function MyClass.func at 0x0000000003079BF8>
print(MyClass.func)

c = MyClass()
del c.a
print(c.a)