#importing modules
import time

#typewriter function
def t(s):
    for i in s:
        print(i,end='')
        time.sleep(0.01)
    print()


#intro
t('Welcome to this Simple CMD-based Calcultor project in Python.')
t('In this Calcultor, You can perform all the basic arithmetic tasks.')
t('You can give 2 inputs then perform some operation and even use the oputput for further calculations..')


#defining variables
op=0
po=0
i=0 

t(' 1  -  add')
t(' 2  -  subtract')
t(' 3  -  multiply')
t(' 4  -  divide')
t(' 5  -  floor division')
t(' 6  -  remainder')
print()

answ = 'y'
while answ == 'y' :
    if i == 0:
        first_num = int(input('Enter first Number :'))
        print()
    else :
        t('Would u like to use the output of your previous calcultion ('+ str(op) +') here ?(y/n):')
        ans = input()
        print()
        if ans == 'y' :
            first_num = op
        else:
            first_num = int(input('Enter first Number :'))
    
    sec_num = int(input('Enter second Number :'))
    print()
    
    
    oper = int(input('Enter your choice (1->+ , 2->- , 3->* , 4->/ , 5->// , 6->% ):'))
    print()
    if oper == 1 :
        op = first_num + sec_num
        t('Output is '+str(op))
        print()
    elif oper == 2:
        op = first_num - sec_num
        t('Output is '+str(op))
        print()
    elif oper == 3:
        op = first_num * sec_num
        t('Output is '+str(op))
        print()
    elif oper == 4:
        try:
            op = first_num / sec_num
            t('Output is '+str(op))
            print()
        except:
            print('Zero division not possible')
            print()
            continue
    elif oper == 5 :
        op = first_num // sec_num
        t('Output is '+str(op))
        print()
    elif oper == 6:
        op = first_num % sec_num
        t('Output is '+str(op))
        print()
    else:
        t('pls enter a valid option...')
        print()
    print()
    i+=1
    t('Time for the Next calcultion ')        

    answ=input('Do u want to continue(y/n):')
    

