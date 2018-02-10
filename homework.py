# -*- coding: utf-8 -*-

funs = [['1_1'],]

def fun1_1():
    print(12/(4+1))

def select(funname, times):
    if funname in funs[times]:
        globals().get('fun%s' % funname)()
    
if  __name__ == '__main__':
    num = input("请输入要查看第几次作业:")
    times = int(num)-1
    for fun in funs[times]:
        print(fun)
    select(funname = input("请输入要查看的作业编号:"), times=times)