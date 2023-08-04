from connect import *
import view as v
import add as a
import update as u
import login as l

def index(user):
    print ("1 for Add  new students ")
    print(" ")
    print ("2 for View students  ")
    print(" ")
    print("3 for update any student data ")
    print(" ")
    print("4 for Previous menu ")
    print(" ")
    print("5  for exit")
    l.design()
    ch=l.input_user_choice()
    l.design()
    if ch==1:
        a.add_student()
    elif ch==2:
        v.view_student()
    elif ch==3:
        u.update_student()
    elif ch==4:
        user=l.user()
        if user==1:
            l.admin()
        else:
            e=l.exit()
            if e==1: 
                print("Thankyou for Using ")
                l.design()
                l.login()
            elif e==2:
                index(user)
            else:
                print("enter valid number")
                l.design()
                index(user())
    elif ch==5: 
        e=l.exit()
        if e==1: 
            print("Thankyou for Using ")
            l.design()
            l.login()
        elif e==2:
            index(user)
        else:
            print("enter valid number")
            l.design()
            index(user)
        
def check(sr):
    t=(sr,)
    q="select * from student_data where sr_no=%s"
    cur.execute(q,t)
    data=cur.fetchone()
    rc=cur.rowcount
    return(rc)

def more():
    print("press 1 for fill further details : ")
    print(" ")
    print("press 2 for main menu : ")
    print(" ")
    print("press 3 for exit")
    lst=[1,2,3]
    ln=len(lst)
    l.design()
    while True:
        ch=l.input_user_choice()
        l.design()
        if ch==1:
            return ch
        elif ch==2:
            return ch
        elif ch==3:
            return ch
        else:
            print("Invalid Input,Given Number Has No Funtion")
            l.design()
            continue


    
