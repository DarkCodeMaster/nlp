# -*- coding: utf-8 -*-
from nltk.book import *

funs = [['1_1', '1_2', '1_3', '1_4', '1_5',
         '1_6', '1_7', '1_8', '1_9', '1_10'],]

def fun1_1():
    print(12/(4+1))
    
def fun1_2():
    print(26**100)
    
def fun1_3():
    print(['Monty', 'Python']*20)
    print(3*sent1)
    
def fun1_4():
    print(len(text2))
    print(len(set(text2)))
    
def fun1_5():
    print("言情小说")
    
def fun1_6():
    print("暂时不清楚")
    #text2.dispersion_plot(['Elinor', 'Edward', 'Willoughby', 'Marianne'])

def fun1_7():
    print(text5.collocations())
    
def fun1_8():
    print("用途:计数text4中不重复的标识符数量")
    print("将链表text4转换为没有重复元素的集合")
    print("计算集合中的元素数量")
    
def fun1_9():
    my_string = 'HelloWorld'
    print(my_string*3)
    print((my_string + ' ')*3)

def fun1_10():
    my_sent = ['My', 'sent']
    print(' '.join(my_sent))
    print('My Sent'.split(' '))

def select(funname, times):
    if funname in funs[times]:
        globals().get('fun%s' % funname)()
    
if  __name__ == '__main__':
    num = input("请输入要查看第几次作业:")
    times = int(num)-1
    for fun in funs[times]:
        print(fun)
    select(funname = input("请输入要查看的作业编号:"), times=times)