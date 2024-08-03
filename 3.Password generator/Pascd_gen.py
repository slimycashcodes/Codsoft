#importing required modules
import secrets as s 
import time
import random as r

#typewriter module
def t(d):
    for i in d:
        print(i,end='')
        time.sleep(0.02)
    print()
    
#intro
t('Welcome to this password generator project.')
t('There are basically three types of options in which passwords can be generated ..')
t('lvl-1 --> using only letters')
t('lvl-2 --> using letters and numbers')
t('lvl-3 --> using symbols , leters and numbers ')

a='qazwsxedcrfvtgbyhnujmikolpJHGVGUYBWTYDBLSDIKUNSDJNSB'
dd='AOIUNSAYS*&^%@#!%52317623?:|<>QAASSDUYGUYBYBWugefiuwaebfyb'
f='y'
while f != 'n':
    ch=int(input('Enter yout required lvl:'))
    if ch == 1:
        n=int(input('enter length of password:'))
        d = r.sample(a,n)
        pasd=''
        for i in d:
            pasd+=str(i)
        t('Your Password is :'+pasd)
    elif ch == 2:
        n=int(input('enter length of password:'))
        pasd=s.token_urlsafe(n)
        t('Your Password is :'+pasd)

    elif ch == 3:
        n=int(input('enter length of password:'))
        d = r.sample(dd,n)
        pasd=''
        for i in d:
            pasd+=str(i)
        t('Your Password is :'+pasd)
    else:
        t('Please enter a valid option ....')
    f=input('do u want to continue(y/n):')
