from nltk.book import *
import sys

funs = [['1_1', '1_2', '1_3', '1_4', '1_5',
         '1_6', '1_7', '1_8', '1_9', '1_10',
         '1_11', '1_12', '1_13', '1_14', '1_15',
         '1_16', '1_17', '1_18', '1_19', '1_20',
         '1_21', '1_22', '1_23', '1_24', '1_25',
         '1_26', '1_27', '1_28', '1_29'],
         [],]

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

def fun1_11():
    phrase1 = ['hello', 'world']
    phrase2 = ['monty', 'python']
    print(len(phrase1)+len(phrase2))
    print(len(phrase1+phrase2))
    
def fun1_12():
    print('第二种更为常用,因为词汇链表更易用且可读性更高')
    
def fun1_13():
    print('sent1中第三个词的第三个字母')
    
def fun1_14():
    for i in range(len(sent3)):
        if sent3[i] == 'the':
            print(i)
    print([i for i in range(len(sent3)) if sent3[i]=='the'])
def fun1_15():
    print(sorted([w for w in set(text5) if w.startswith('b')]))
    
def fun1_16():
    print(range(10))
    print(range(10, 20))
    print(range(10,20,2))
    print(range(10,20,-2))
    
def fun1_17():
    print(text9.index('sunset'))

def fun1_18():
    print(sorted(set(sent1+sent2+sent3+sent4+sent5+sent6+sent7+sent8)))
    
def fun1_19():
    print('第二个的值更大,因为集合里面包括了大写和小写')

def fun1_20():
    print('w.isupper()是全是大写')
    print('not w.islower()是不全是小写')
    
def fun1_21():
    print(text2[-2:])
    
    
def fun1_22():
    fre = FreqDist([w.lower() for w in text5 if len(w)==4])
    print(fre)
    print([[w, fre.get(w)] for w in fre])
    
def fun1_23():
    x = set([w for w in text6 if w.isupper()])
    for w in x:
        print(w)
        
def fun1_24():
    print([w for w in text6 if w.endswith('ize')])
    print([w for w in text6 if 'z' in w])
    print([w for w in text6 if 'pt' in w])
    print([w for w in text6 if w.istitle()])
    
def fun1_25():
    sent = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']
    print([w for w in sent if w.startswith('sh')])
    print([w for w in sent if len(w)>4])
    
def fun1_26():
    print('计算所有文本的总长度')
    print(sum([len(w) for w in text1]) / len(text1))
    
def fun1_27():
    def vocab_size(text):
        return len(text)
    print(vocab_size(text1))
    
def fun1_28():
    def percent(word, text):
        num = len([w for w in text if w==word])
        print('%.2f%%' % (100*(num/len(text))))
    percent('the', text1)

def fun1_29():
    print('判断sent3是否为text1的真子集')
    
def select(funname, times):
    if funname in funs[times]:
        globals().get('fun%s' % funname)()
    
if  __name__ == '__main__':
    while(True):
        num = input('请输入要查看第几次作业:')
        times = int(num)-1
        for fun in funs[times]:
            print(fun)
        select(funname = input('请输入要查看的作业编号:'), times=times)