import random
toss_user = int(input("Enter your number : "))
toss_sys = random.randint(0,10)
user_choice_evenOdd = input("Which number do you want even or odd\nEnter 0 for even 1 for odd : ")
user_elect = ''
sys_elect = ''
user_score = 0
sys_score = 0
user_current_score = 0
sys_current_score = 0
user_ball = 0
sys_ball = 0
user_status = 1
sys_status = 1
innings = 1


if(toss_user + toss_sys)%2 == user_choice_evenOdd:
    print("Congartulations! , You won the toss.")
    user_elect = input("What will you choose\n1.Batting\t2.Bowling : ")
    if user_elect == 'Batting' :
        sys_elect = 'Bowling'
    else:
        sys_elect = 'Batting'
else:
    print("You lost the toss!")
    sys_elect = random.choice(['Batting','Bowling'])
    print("System selected : " , sys_elect)
    if sys_elect == 'Batting' :
        user_elect = 'Bowling'
    else:
        user_elect = 'Batting'
    
while(innings <= 2):
    if user_elect == 'Batting':
        print("You need to bat now.")
        while user_status != 0:
            user_current_score = int(input("Enter your score : "))
            if user_current_score > 6 :
                print("Invalid score! Score must be less than 7 , Try again!!!")
            else:
                sys_ball = random.randint(0,6)
                print("System ball score is : " , sys_ball)
                if(sys_ball == user_current_score):
                    print('You are out!')
                    user_status = 0
                else:
                    user_score = user_score + user_current_score
        print("Your total score is : ",user_score)
    else:
        print("You need to bowl now.")
        while sys_status != 0:
            user_ball = int(input("Enter your ball score : "))
            if(user_ball > 6):
                print("Invalid score! Score must be less than 7 , Try again!!!")
            else:
                sys_current_score = random.randint(0,6)
                print("System score is : " , sys_current_score)
                if(sys_current_score == user_ball):
                    print("System is out! , you took the wicket!")
                    sys_status = 0
                else:
                    sys_score = sys_score + sys_current_score
        print("System total score is : " , sys_score)
    innings = innings + 1
    if(user_elect == 'Batting'):
        user_elect = 'Bowling'
        sys_elect = 'Batting'
    else:
        sys_elect = 'Bowling'
        user_elect = 'Batting'
        
print("The game is over")
print(f"Your score is : {user_score} \n System score is : {sys_score}")
if(user_score > sys_score):
    print("Congratulations!, You WON the game")
else:
    print("You lost the game!")