#importing required modules
import random as r
import time 

#initialising variables
com = ['r','p','s']
com_emoji = ['💎','📃','✂']
player_score = 0
computer_score = 0

#typewriter module
def t(s):
    for i in s:
        print(i,end='')
        time.sleep(0.03)
    print()   

def result(u,c):
    global player_score
    global computer_score
    if u == 'r':
        if c == 'r':
            t('👤 -- 💎 x 💎 -- 🤖')
            t('no result')
            t('User score :'+ str(player_score))
            t('CPU score :'+ str(computer_score))
            
        elif c == 'p':
            t('👤 -- 💎 x 📃 -- 🤖')
            t('🤖 won this turn')
            computer_score+=1
            t('User score :'+ str(player_score))
            t('CPU score :'+ str(computer_score))
            
        
        elif c == 's':
            t('👤 -- 💎 x ✂ -- 🤖')
            t('👤 won this turn')
            player_score+=1
            t('User score :'+ str(player_score))
            t('CPU score :'+ str(computer_score))
    elif u == 's':
        if c == 's':
            t('👤 -- ✂ x ✂ -- 🤖')
            t('no result')
            t('User score :'+ str(player_score))
            t('CPU score :'+ str(computer_score))
            
        elif c == 'r':
            t('👤 -- ✂ x 💎 -- 🤖')
            t('🤖 won this turn')
            computer_score+=1
            t('User score :'+ str(player_score))
            t('CPU score :'+ str(computer_score))
            
        
        elif c == 'p':
            t('👤 -- ✂ x 📃 -- 🤖')
            t('👤 won this turn')
            player_score+=1
            t('User score :'+ str(player_score))
            t('CPU score :'+ str(computer_score))
    elif u == 'p':
        if c == 'p':
            t('👤 -- 📃 x 📃 -- 🤖')
            t('no result')
            t('User score :'+ str(player_score))
            t('CPU score :'+ str(computer_score))
            
        elif c == 's':
            t('👤 -- 📃 x ✂ -- 🤖')
            t('🤖 won this turn')
            computer_score+=1
            t('User score :'+ str(player_score))
            t('CPU score :'+ str(computer_score))
            
        
        elif c == 'r':
            t('👤 -- 📃 x 💎 -- 🤖')
            t('👤 won this turn')
            player_score+=1
            t('User score :'+ str(player_score))
            t('CPU score :'+ str(computer_score))
    else:
        t('Pls enter a valid choice...')
        t('-1 points for foul try..')
        player_score-=1
    
flag=False
flag_c=False 
  
def check():
    global flag
    global flag_c
    if player_score >= 5 :
        flag=True
        return True
    if computer_score >= 5:
        flag_c=True
        return False
        

#main game
t('Welcome to this Rock-Paper-Scissor game ')
t('I hope u know the rules , letz begin...')
t('U will have to enter r-Rock , p-Paper , s-Scissor')
t('pls make sure to have turned off ur caps lock 😀')
t('U will have to get 5 points to win...')
while True:
    user_inp = input('Enter your Choice :')
    com_inp = r.choice(com)
    result(user_inp,com_inp)
    dd=check()
    if dd:
        t('U have won this Game..')
        break
    if flag_c == True:
        t('U have lossed the Game')  
        break
    
