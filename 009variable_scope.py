#LEGB--------local, Enclosing, Global, Built-in
# order of assigning variable
# x= 'global x'
# # global variable
# def test(b):
#     global a
# # global variable inside the function will only work after calling of function we cannot acess it without calling our function
#     a='inside func global'
#     y ='local y'
#     print(y)
#     print(b)
#     # local variable
#
# test('passed to function ')
# print(a)
# import builtins
# print(dir(builtins))
# # it will show our all builtins functions
# m = min([1,4,5,6,7,5,3,6,7,9])
# # min is built in type function
# print(m)
def outer():
    x = 'outer x'
    Enclosing varable
    def inner():
        # x='inner x'
        print(x)
    inner()
    print(x)
outer()