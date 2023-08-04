from connect import *
import home as h
from prettytable import PrettyTable
import login as l
def int_sr():
     while True:
        choice=input("enter Sr_no : ")
        if choice.isdigit():
            ch= int(choice)
            return ch
        else:
            design()
            print("Invalid Input")
            design()
            continue  

def again_view():
    print("1 for again view menu ")
    print(" ")
    print("2 for main menu ")
    print(" ")
    print("3 for exit")
    l.design()
    ch=l.input_user_choice()
    l.design()
    if ch==1:
        view_student()
    elif ch==2:
        h.index(l.user())
    elif ch==3:
        e=l.exit()
        if e==1: 
            print("Thankyou for Using ")
            l.design()
            l.login()
        elif e==2:
            view_student()
        else:
            print("enter valid number")
            l.design()
            view_student()
    else:
        print("Invalid Choice : ")
        l.design()
        again_view()           
        
def gen():
    print("1 for Boys details ")
    print(" ")
    print("2 for Girls  details")
    print(" ")
    print("3 for view menu")
    print(" ")
    print("4 for main menu")
    print(" ")
    print("5 for exit")
    l.design()
    ch=l.input_user_choice()
    l.design()
    return ch

def view_student():
    print("1 for view all student data")
    print(" ")
    print("2 for view indivisual student data")
    print(" ")
    print("3 for view Housewise student data")
    print(" ")
    print("4 for view blockwise student data")
    print(" ")
    print("5 for view addresswise(village) student data")
    print(" ")
    print("6 for main menu")
    print(" ")
    print("7 for exit")
    l.design()
    ch=l.input_user_choice()
    l.design()
    if ch==1:
        q='''select Sr_no,Name ,Father_Name,Mother_Name,Contact_no,catagery
        from student_data '''
        cur.execute(q)
        data=cur.fetchall()
        x = PrettyTable(["Sr_no","Name ","Father_Name","Mother_Name","Contact_no",
                                "categary"])
        for d in data:
            x.add_row([d[0],d[1],d[2],d[3],d[4],d[5]])
            
        print(x)
        again_view()
    elif ch==2:
        sr=int_sr()
        l.design()
        t=(sr,)
        q='''select Sr_no,Name ,Father_Name,Mother_Name,Contact_no,catagery
        from student_data where sr_no=%s'''
        cur.execute(q,t)
        d=cur.fetchone()
        r=cur.rowcount
        y = PrettyTable(["Sr_no","Name ","Father_Name","Mother_Name","Contact_no",
                                "categary"])
        if r==1:
            y.add_row([d[0],d[1],d[2],d[3],d[4],d[5]])
            print(y)
            again_view()
        else:
            l.design()
            print("Data not found,Something went wrong ")
            print("please try again")
            l.design()
            view_student()
    elif ch==3:
        g=gen()
        if g==1:
            q='''   select h.house_name ,h.HOUSE_MASTER ,count(s.sr_no)
                from student_data s,house h
                where h.house_id = s.house_id and s.gender="m"
                group by h.house_id'''
            cur.execute(q)
            data=cur.fetchall()
            z = PrettyTable(["House Name","House Master Name","Total number of students ",])
            for d in data:
                z.add_row([d[0],d[1],d[2]])
            print(z)
            l.design()
            again_view()
        elif g==2:
            q='''   select h.house_name ,h.HOUSE_MASTER ,count(s.sr_no)
                from student_data s,house h
                where h.house_id = s.house_id and s.gender="F"
                group by h.house_id'''
            cur.execute(q)
            data=cur.fetchall()
            z = PrettyTable(["House Name","House Master Name","Total number of students ",])
            for d in data:
                 z.add_row([d[0],d[1],d[2]])
            print(z)
            l.design()
            again_view()
        elif g==3:
            view_student()
        elif g==4:
            h.index(l.user())
        elif g==5:
            e=l.exit()
            if e==1: 
                print("Thankyou for Using ")
                l.design()
                l.login()
            elif e==2:
                gen()
            else:
                print("enter valid number")
                l.design()
                view_student()
        else:
            print("input valid number")
            view_student()
                    
    elif ch==4:
         q='''select a.block ,count(s.sr_no)
                from student_data s,address a
                where s.sr_no = a.sr_no 
                group by a.block'''
         cur.execute(q)
         data=cur.fetchall()
         m = PrettyTable(["Block Name","Total number of students ",])
         for d in data:
             m.add_row([d[0],d[1]])
         print(m)
         l.design()
         again_view()
    elif ch==5:
        
        q='''select a.village ,count(s.sr_no)
                from student_data s,address a
                where s.sr_no = a.sr_no 
                group by a.village'''
        cur.execute(q)
        data=cur.fetchall()
        n = PrettyTable(["Village Name","Total number of students ",])
        for d in data:
            n.add_row([d[0],d[1]])
        print(n)
        l.design()
        again_view()
        
    elif ch==6:
        h.index(l.user())
    elif ch==7:
        e=l.exit()
        if e==1: 
            print("Thankyou for Using ")
            l.design()
            l.login()
        elif e==2:
            view_student()
        else:
            print("enter valid number")
            l.design()
            view_student()
                    

            


