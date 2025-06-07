def a():
    print('a() starts')
    b()
    print('back at a()')
    d()
    print('a() returns')

def b():
    print('b() starts')
    c()
    print('back at b()')
    print('b() returns')

def c():
    print('c() starts')
    print('c() returns')

def d():
    print('d() starts')
    print('d() returns')

a()