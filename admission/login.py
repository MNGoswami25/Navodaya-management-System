from connect import *
import home as h

def input_user_choice():
    while True:
        choice=input("enter your choice : ")
        if choice.isdigit():
            ch= int(choice)
            return ch
        else:
            design()
            print("Invalid Input")
            design()
            continue    
            
def user():
    user=user_ty
    return user


def exit():
    print("press 1 for log out")
    print(" ")
    print("press 2 for cancel ")
    design()
    ch=input_user_choice()
    design()
    return ch

        
def design():
    print(" ")
    print("*"*50)
    print(" ")


#For login user/Admin

def login():
    global user_ty
    print("admin press 1")
    print(" ")
    print("user press 2")
    print(" ")
    print("3 for help ")
    design()
    ch=input_user_choice()
    design()
    user_ty=ch
    if ch==1:
        ty="admin"
        email_admin_check(ty)
        admin()
    elif ch==2:
        ty="user"
        email_admin_check(ty)
        h.index(user_ty)
    elif ch==3:
        ch=help_u()
        if ch==1:
            login()
        else:
            login()
    else:
        design()
        print("Invalid Input,Number has no funtion")
        design()
        login()
        
# To Check Email OF User

def email_admin_check(ty):
    global e_a
    e_a=input("E_mail Id : ")
    print(" ")
    p=input ("Password : ")
    design()
    t=(e_a,p,ty)
    q='''select * from login where email = %s and passwrd =%s
            and type_user = %s'''
    cur.execute(q,t)
    d=cur.fetchone()
    r=cur.rowcount
    print("...............................Processing................")
    print(" ")
    print("............................Wait for a min......................" )
    design()
    if r==1:
        print(".....................Login Successful.............")
        design()
        return()
    else:  
        print("incorrect e_mail or password")
        design()
        login()
        
# Funtion OF Admin     

def admin():
    global user
    print("1 About students ")
    print(" ")
    print("2 add a new user ")
    print(" ")
    print("3 make another  admin ")
    print(" ")
    print("4 help")
    print(" ")
    print("5 exit")
    design()
    ch=input_user_choice()
    design()
    if ch==1:
            h.index(user)
    elif ch==2:
        new_user()
    elif ch==3:
        new_admin()
    elif ch==4:
        c=help_u()
        if c==1:
            admin()
        elif c==2:
            e=exit()
            if e==1:
                login()
            elif e==2:
                admin()
            else:
                admin()
    elif ch==5: 
        e=exit()
        if e==1: 
            print("Thankyou for Using ")
            design()
            login()
        elif e==2:
            admin()
        else:
            print("Enter valid number")
            design()
            admin()
    else:
        print("Invalid Number,Number has no funtion")
        design()
        admin()
#TO add new user:
        
def new_user():
    global nm
    nm=input("enter new user's name: ")
    print(" ")
    e=check_email_user()
    print(" ")
    p=input ("enter  password : ")
    design()
    c=new_user_choice()
    if c==1:
        new_user2(e,p,nm)
        ch=new_admin4()
        if ch==1:
            new_admin3(e)
            print(" ")
            t1=(e_a,)
            q1="select name from login where email = %s"
            cur.execute(q1,t1)
            d=cur.fetchone()
            print(d[0]," from now You are  our User only ")
            design()
            login()
        elif ch==2:
            admin_del()
        elif ch==3:
            admin()
        else:
            design()
            print("Invalid Number")
            design()
            new_admin4()      
    else :
        new_user2(e,p,nm)
        print("New User Added")
        design()
        admin()
        
#TO Get New User Choice:
        
def new_user_choice():
    while True:
        print("1  make admin")
        print(" ")
        print("2  make user only")
        design()
        c_option = [1,2]
        choice=input_user_choice()
        if choice in c_option:
            return choice
        else:
            design()
            print("Invalid Input,Input Number has no funtion")
            design()
            continue    

        
#TO add new user
        
def new_user2(e,p,nm):
    design
    t=(e,p,nm)
    q='''insert into login(email,passwrd,name)
                                    values(%s,%s,%s)'''
    cur.execute(q,t)
    con.commit()
    design()
    return

#To get choice of previous Admin

def new_admin4():
    print("1 Remain as a user : ")
    print(" ")
    print("2 Exit from Admission system:")
    print(" ")
    print("3 exit")
    design()
    c=input_user_choice()
    return c

#To make new Admin:

def new_admin3(e_u):
    t1=(e_a,)
    q1='''update login
        set type_user='user'
        where email=%s'''
    cur.execute(q1,t1)
    con.commit()
    t=(e_u,)
    q2='''update login
        set type_user='admin'
        where email=%s'''
    cur.execute(q2,t)
    con.commit()
    q3='''select name from login where email =%s'''
    cur.execute(q3,t)
    data=cur.fetchone()
    print("Congratulations ",data[0],"You become our new admin")
    design()
    return
    


# To get E mail of new admin:

def new_admin2():
    e_u=input("enter new admin's e_mail Id : ")
    design()
    t=(e_u,)
    q='''select * from login where email = %s'''
    cur.execute(q,t)
    d=cur.fetchone()
    r=cur.rowcount
    if r==1:
        new_admin3(e_u)
        return
        
    else:
        print("E_mail id don't found")
        new_admin2()

              



    
def check_email_user():
    e=input("enter  e_mail Id : ")
    t=(e,)
    q="select * from login where email = %s"
    cur.execute(q,t)
    d=cur.fetchone()
    r=cur.rowcount
    if r==1:
        design()
        print("Email_id alredy exits Try with different one")
        design()
        check_email_user()
    else:
        return e

    



def admin_del():
    new_admin2()
    t1=(e_a,)
    q='''select name from login where email =%s'''
    cur.execute(q,t1)
    d=cur.fetchone()
    print(d[0]," from now You are Not our User ")
    design()
    print(" Thankyou for using")
    q2="delete from login where email = %s"
    cur.execute(q2,t1)
    con.commit()
    design()
    login()

#To Add New Admin

def new_admin():
    ch=new_admin4()
    if ch==1:
        new_admin2()
        t1=(e_a,)
        q1="select name from login where email = %s"
        cur.execute(q1,t1)
        d=cur.fetchone()
        print(d[0]," from now You are  our User only ")
        design()
        login()
    elif ch==2:
        admin_del()
    elif ch==3:
        admin()
    else:
        print("Invalid Number,Input Number has no funtion")
        design()
        new_admin()

#For Help Menu
        
def help_menu():
    while True:
        print("1 for main menu")
        print(" ")
        print("2 for exit")
        design()
        u_cho=[1,2]
        ch=input_user_choice()
        design()
        if ch in u_cho:
            return ch
        else:
            design()
            print("Invalid Input")
            design()
            continue

#For Help To User
    
def help_u():
    f=open("help.txt","r")
    print(" ")
    f1=f.read()
    print(f1)
    f.close()
    design()
    c=help_menu()
    return c


     
