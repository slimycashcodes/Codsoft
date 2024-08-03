#importing modules
import csv
import time 

#opeing file
fp=open('contactlog.csv','a+',newline='\n')
wr=csv.writer(fp)

#defining functions
def t(s):
    for i in s:
        print(i,end='')
        time.sleep(0.01)
    print()

#Intro message
t('Welcome to this Contact Book Project.')
t('You can use this for multiple purposes... ')
t('1.Add New Contact.')
t('2.See the list of existing Contacts.')
t('3.Search the existing Contacts.')
t('4.Update an existing Contact.')
t('5.Delete an existing Contact.')

#Mainpgrm
loop='y'
while loop!='n':
    ch=int(input('Enter your choice :'))
    if ch == 1:
        t('Pls enter the details of the new contact...')
        nm = input('Enter the Store Name :')
        no = int(input('Enter the phone No. :'))
        em = input('Enter Email Address :')
        ad = input('Enter Address :')
        da = [nm , no , em , ad]
        wr.writerow(da)
        fp.flush()
    
    elif ch == 2:
        t('Details of existing Contacts ...')
        with open('contactlog.csv','r') as fs:
            fs.seek(0)
            rd = csv.reader(fs)
            for i in rd:
                t(i[0]+' '+i[1])
    
    elif ch == 3:
        t('Pls enter the Name of the store to be searched ..')
        nme = input('Enter name :')
        flag=False
        with open('contactlog.csv','r',newline='\n') as fs:
            rd = csv.reader(fs)
            for i in rd:
                if i[0] == nme :
                    t('Details found...')
                    t('Store Name :'+i[0])
                    t('Phone no. :'+ i[1])
                    t('Email add. :'+i[2])
                    t('Address :'+i[3])
                    flag=True
            if flag == False :
                print('No Record Found pls try a valid name...')
        
    elif ch == 4:
        with open('contactlog.csv','r',newline='\n') as ff:
            rd=csv.reader(ff)
            data=[]
            for i in rd:
                data.append(i)
        nn = input('Enter name of store to be updated:')
        for i in data:
            if i[0] == nn:
                t('record found')
                t(i)
                nm = input('Enter the updated Store Name :')
                no = int(input('Enter the updated phone No. :'))
                em = input('Enter updated Email Address :')
                ad = input('Enter updated Address :')
                da = [nm , no , em , ad]
                data[data.index(i)]=da
        with open('contactlog.csv','w',newline='\n') as ef:
            wr=csv.writer(ef)
            wr.writerows(data)
            ef.flush()
            t('Updated the record.')
    
    elif ch == 5:
        with open('contactlog.csv','r',newline='\n') as ff:
            rd=csv.reader(ff)
            data=[]
            for i in rd:
                data.append(i)
        nn = input('Enter name of store to be deleted')
        for i in data:
            if i[0] == nn:
                t('record found')
                data.remove(i)
        with open('contactlog.csv','w',newline='\n') as ef:
            wr=csv.writer(ef)
            wr.writerows(data)
            ef.flush()
            t('Deleted the record.')
    loop = input('Do u want to continue(y/n):')

fp.close()
        
                    
