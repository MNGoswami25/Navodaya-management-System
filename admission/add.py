from connect import *
import home as h
import datetime as d
import update as u
import login as l

def input_user_adhr():
    while True:
        choice=input("Aadhar Number : ")
        if choice.isdigit():
            ch= int(choice)
            return ch
        else:
            l.design()
            print("Invalid Input")
            l.design()
            continue    

def input_adhr():
    ad=input_user_adhr()
    ln=len(str(ad))
    if ln==12:
        t=(ad,)
        q="select * from student_data where aadhar = %s"
        cur.execute(q,t)
        d=cur.fetchone()
        r=cur.rowcount
        if r==1:
            l.design()
            print("Invalid aadhar Number/Duplicate Aadhar number: ")
            print(" ")
            print("Please enter right aahar number")
            l.design()
            input_adhr()
        else:
            return ad
    else:
        l.design()
        print("Enter a valid Aadhar Number (it must be of 12 digit ")
        l.design()
        input_adhr()
    
def input_user_number():
    while True:
        choice=input("Contact Number : ")
        if choice.isdigit():
            return choice
        else:
            l.design()
            print("Invalid Input")
            l.design()
            continue    

def input_ph():
    while True:
        p=input_user_number()
        m=len(p)
        if m == 10:
            return p
            
        else:
            l.design()
            print("Invalid Number Please enter valid Number")
            l.design()
            continue

def get_gender():
    while True:
        ln=["m","M","f","F"]
        gen=input("Gender (M/F) : ")
        if gen in ln:
            return gen
        else:
            l.design()
            print("Invalid gender please enter (M/F) only ")
            l.design()
            continue
         
def get_house(g):
    t=(g,)
    q='''SELECT house_id,count(sr_no) from student_data
        where gender = %s
            group by house_id
           order by count(sr_no),house_id '''
    cur.execute(q,t)
    d=cur.fetchall()
    if d[0][0]==10:
        l.design()
        print("You Have Allotted CORBETT HOUSE")
    elif d[0][0]==20:
        l.design()
        print("You Have Allotted GANGOTRI HOUSE")
    elif d[0][0]==30:
        l.design()
        print("You Have Allotted NANDA HOUSE")
    elif d[0][0]==40:
        l.design()
        print("You Have Allotted RAJAJI HOUSE")
    else:
        l.design()
        print("Something Went Wrong ")
        l.design()
        h.index(l.user())
    ho=d[0][0]
    return ho
    
def findsr():
    q='select max(sr_no) from student_data'
    cur.execute(q)
    d=cur.fetchall()
    if d[0][0]==0:
        sr=1
        return sr
    else :
        sr=d[0][0]+1
        return sr

def add_student():
    print("FILL ALL THE DETAILS ABOUT STUDENT")
    sr=findsr()
    l.design()
    print("Your SR_NO is ",sr)
    l.design()
    nm=input("Full name : ")
    print(" ")
    fn=input("Father name : ")
    print(" ")
    mn=input("Mother name : ")
    print(" ")
    ph=input_ph()
    print(" ")
    dob=input("DOB (YYYY-MM-DD): ")
    print(" ")
    g=get_gender()
    print(" ")
    ad=input_adhr()
    print(" ")
    re=input("Religion : ")
    print(" ")
    ct=input("Categary (gen/obc/sc/st) : ")
    print(" ")
    ho=get_house(g)
    am=d.date.today()
    t=(sr,nm,fn,mn,ph,dob,g,ad,re,ct,ho,am)
    q='''insert into student_data (sr_no,name,father_name,mother_name,
                                                    contact_no,
                                                    dob,gender,aadhar,religion,catagery,house_id,
                                                    admission_date)
                                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
    cur.execute(q,t)
    con.commit()
    l.design()
    print("YOU HAVE COMPLEATED ONE STAGE ")
    l.design()
    c=h.more()
    if c==1:
        add_2(sr)
    elif c==2:
        h.index(l.user())
    elif c==3:
        e=l.exit()
        if e==1: 
            print("Thankyou for Using ")
            l.design()
            l.login()
        elif e==2:
            h.more()
        else:
            print("enter valid number")
            l.design()
            h.more()
    else:
        l.design()
        print("Enter right choice : ")
        l.design()
        h.more
        
#address
def add_2(sr):
    print(" ")
    sr_no=sr
    vi=input("Village name : ")
    print(" ")
    po=input("Post office : ")
    print(" ")
    pin=input("Pin_code no : ")
    print(" ")
    bl=input("Block name : ")
    print(" ")
    dist=input("District name : ")
    print(" ")
    st=input("State name : ")
    l.design()
    t=(sr_no,vi,po,pin,bl,dist,st)
    q='''insert into address (sr_no,village,post_office,pin_code,block,district,state)
                                values(%s,%s,%s,%s,%s,%s,%s)'''
    cur.execute(q,t)
    con.commit()
    print("YOU HAVE COMPLEATED SECOND STAGE ")
    l.design()
    ch=h.more()
    if ch==1:
        u.check_2(sr_no)
    elif ch==2:
        h.index(l.user())
    elif ch==3:
        e=l.exit()
        if e==1: 
            print("Thankyou for Using ")
            l.design()
            l.login()
        elif e==2:
            h.more()
        else:
            print("enter valid number")
            l.design()
            h.more()
    else:
        l.design()
        print("Enter right choice : ")
        l.design()
        h.more

#Bank Details
def add_3(sr):
    print(" ")
    sr_no=sr
    bn=input("enter Bank name : ")
    print(" ")
    ac=input("enter Bank Account Number : ")
    print(" ")
    ifc=input("enter IFSC code : ")
    print(" ")
    t=(sr_no,bn,ac,ifc)
    q='''insert into account (sr_no,Bank,Account_no,ifsc)
                                values(%s,%s,%s,%s)'''
    cur.execute(q,t)
    con.commit()
    l.design()
    print("YOU HAVE  FILLED ALL DETAILS")
    l.design()
    h.index(l.user())    




    
