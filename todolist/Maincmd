#importing modules
import time
import csv

#opening file and 
fp=open('todolog.csv','a+',newline='\n')
wr=csv.writer(fp)
     
#typewriter method for more user_friendly look
def t(s):
     for i in s:
          print(i,end='')
          time.sleep(0.02)
     print()
#Intro message
t('Welcome to this To-Do list Project')
t('There are basically 3 options for the user in this project......')
print('       1.Add a to-do task with due date')
print("       2.Change the details of a task like it's due-date and status")
print('       3.See the list of completed and remaining to-do list')


#while Loop
run = 'y'
while run != 'n':
     #menu-driven functions
     t('Enter the required choice(1-add new / 2-change details / 3-see list):')
     ch=int(input())
     if ch not in [1,2,3]:
          break
     
     if ch == 1:
          t('so yeah you have chosen to add a task to your T.D.L')
          t("Enter ur task's name .....")
          task_name = input()
          task_time = time.ctime()
          t('Enter Due date of task ..')
          task_duedate = input()
          task_status = 'pending'
          task_det = [task_name , task_time , task_duedate , task_status]
          wr.writerow(task_det)
          fp.flush()
          
     elif ch == 2:
          t('Here is the list of existing tasks in ur T.D.L ..')
          fp.seek(0)
          rd = csv.reader(fp)
          csv_data = []
          for i in rd : 
               print(i)
               csv_data.append(i)
          t('Enter the name of task to be updated ..')
          ch_task = input()
          fl=False
          for i in csv_data :
               if i[0] == ch_task :
                    fl=True
                    t('Pre-existing record is ...'+ str(i[0]) + str(i[2]) )
                    t('Enter the new data below ...:')
                    name = input('New Name :')
                    times = time.ctime()
                    due = input('New Due Date :')
                    sta = input('New Status :')
                    new_data=[name,times,due,sta]
                    csv_data[csv_data.index(i)]=new_data
              
               
          with open('todolog.csv','w+',newline='\n') as file:
               wr = csv.writer(file)
               wr.writerows(csv_data)

           
          

     elif ch == 3:
          data = []
          with open('todolog.csv','r',newline='\n') as dd:
               rd=csv.reader(dd)
               for i in rd:
                    data.append(i)
          t('Here is the pre-existing tasks in your T.D.L..')
          data_com=[]
          data_pen=[]
          for i in data:
               if i[3] == 'completed':
                    data_com.append(i)
               else:
                    data_pen.append(i)
          t('Completed tasks...')
          for i in data_com:
               t(i[0]+'   '+i[2])
          t('pending tasks....')
          for i in data_pen:
               t(i[0]+'   '+i[2])
               
               
     run=input('Do u want to continue (y/n):')    
     

fp.close()
          
          
          

     
