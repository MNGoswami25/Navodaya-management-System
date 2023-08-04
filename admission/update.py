from connect import *
import home as h
import add as a
import view as v
import login as l
def check(sr):
    t=(sr,)
    q="select * from address where sr_no=%s"
    cur.execute(q,t)
    data=cur.fetchone()
    rc=cur.rowcount
    if rc==1:
        check_2(sr)
    else:
        a.add_2(sr)
        check_2(sr)
def check_2(sr):
    t=(sr,)
    q="select * from account where sr_no=%s"
    cur.execute(q,t)
    data=cur.fetchone()
    rc=cur.rowcount
    if rc==1:
        print("All Data already Inserted ")
        l.design()
        h.index(l.user())
    else:
        a.add_3(sr)

def check_row(sr):
    t=(sr,)
    q="select * from student_data where sr_no=%s"
    cur.execute(q,t)
    data=cur.fetchone()
    rc=cur.rowcount
    if rc==1:
        q1='select name from student data where sr_no=%s'
        cur.execute(q,t)
        data=cur.fetchone()
        print("Name :",data[1])
        print("  ")
        check(sr)
    else:
        print("No Student has sr_no",sr)
        l.design()
        h.index(l.user())
    
        
    

def update_student():
    s=v.int_sr()
    l.design()
    check_row(s)
    
