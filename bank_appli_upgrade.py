import tkinter
from tkinter import *
import tkinter.messagebox as msgbox
# import time
# import os

win = Tk()
win.title("THE BANK APPLICATION_TESTING")

first_notice = Label(win,text="bank application_beta_ver")
first_notice.pack()

def deposit_bck_butn2(x,a,b):
    with open("leftmoney.txt","r") as dp_mn:
        depo_list = dp_mn.readlines()
        d = []
        depo_second_list = []
        for i in range(len(depo_list)):
            if "\n" in depo_list[i]:
                d.append(depo_list[i].replace("\n",""))
        d[a] = str(int(d[a])+int(b))
        for i in range(len(d)):        
            depo_second_list.append(d[i]+"\n") 
        with open("leftmoney.txt","w") as fuck:
            fuck.writelines(depo_second_list)
    msgbox.askquestion("end","finish?")
    msgbox.showinfo("success","success")
    x.withdraw()

def withdraw_bck_butn2(x,a,b):#a는 순서, b는 넣는돈
    with open("leftmoney.txt","r") as dp_mn:
        depo_list = dp_mn.readlines()
        d = []
        depo_second_list = []
        for i in range(len(depo_list)):
            if "\n" in depo_list[i]:
                d.append(depo_list[i].replace("\n",""))
        d[a] = str(int(d[a])-int(b))
        for i in range(len(d)):        
            depo_second_list.append(d[i]+"\n") 
        with open("leftmoney.txt","w") as fuck:
            fuck.writelines(depo_second_list)
    msgbox.askquestion("end","finish?")
    msgbox.showinfo("success","success")
    x.withdraw()

def deposit_check_id_pw(id,pw,x):#아이디 패스워드
    with open("idlist.txt","r") as log_id:
        id_login_list = log_id.readlines()
    with open("pwlist.txt","r") as log_pw:
        pw_login_list = log_pw.readlines()
    if str(id)+"\n" in id_login_list and str(pw)+"\n" in pw_login_list and id_login_list.index(str(id)+"\n")==pw_login_list.index(str(pw)+"\n"):
        deposit_second_page(id_login_list.index(str(id)+"\n"))
        x.withdraw()
    else:
        msgbox.showerror("error","your id is not correct")
        x.withdraw()

def withdraw_check_id_pw(id,pw,x):#아이디 패스워드
    with open("idlist.txt","r") as log_id:
        id_login_list = log_id.readlines()
    with open("pwlist.txt","r") as log_pw:
        pw_login_list = log_pw.readlines()

    if str(id)+"\n" in id_login_list and str(pw)+"\n" in pw_login_list and id_login_list.index(str(id)+"\n")==pw_login_list.index(str(pw)+"\n"):
        withdraw_second_page(id_login_list.index(str(id)+"\n"))
        x.withdraw()
    else:
        msgbox.showerror("error","your id is not correct")
        x.withdraw()

def deposit_butn1():
    win2 = tkinter.Toplevel()
    d_label1 = Label(win2,text="<deposit>")
    d_label2 = Label(win2,text="ID")
    d_entry1 = Entry(win2)
    d_label3=Label(win2,text="PASSWORD") 
    d_entry2 = Entry(win2,show="*")
    d_label1.pack()
    d_label2.pack()
    d_entry1.pack()
    d_label3.pack()
    d_entry2.pack()
    login_btn1= Button(win2,text="LOG IN",
    command=lambda:deposit_check_id_pw(d_entry1.get(),d_entry2.get(),win2))
    login_btn1.pack()

def deposit_second_page(a):
    with open("leftmoney.txt",'r') as lft_mny:
        left_money_list = lft_mny.readlines()
    win2 = tkinter.Toplevel()
    dsp_l1 = Label(win2,text="Current balance")
    dsp_e1 = Label(win2,text=left_money_list[a])
    dsp_l2 = Label(win2,text="Deposit balance")
    dsp_e2= Entry(win2)
    dsp_b1 =Button(win2,text="OK",command=lambda:deposit_bck_butn2(win2,a,dsp_e2.get()))
    dsp_l1.pack()
    dsp_e1.pack()
    dsp_l2.pack()
    dsp_e2.pack()
    dsp_b1.pack()

def withdraw_second_page(a):
    with open("leftmoney.txt",'r') as lft_mny:
        left_money_list = lft_mny.readlines()
    win2 = tkinter.Toplevel()
    dsp_l1 = Label(win2,text="Current balance")
    dsp_e1 = Label(win2,text=left_money_list[a])
    dsp_l2 = Label(win2,text="Withdrawal balance")
    dsp_e2= Entry(win2)
    dsp_b1 =Button(win2,text="OK",command=lambda:withdraw_bck_butn2(win2,a,dsp_e2.get()))
    dsp_l1.pack()
    dsp_e1.pack()
    dsp_l2.pack()
    dsp_e2.pack()
    dsp_b1.pack()

def withdraw_butn1():
    win3 = tkinter.Toplevel()
    w_label1 = Label(win3,text="<withdraw>")
    w_label2 = Label(win3,text="ID")
    w_entry1 = Entry(win3)
    w_label3=Label(win3,text="PASSWORD") 
    w_entry2 = Entry(win3,show="*")
    w_label1.pack()
    w_label2.pack()
    w_entry1.pack()
    w_label3.pack()
    w_entry2.pack()
    w_entry2.pack()
    login_btn1= Button(win3,text="LOG IN",command=lambda:withdraw_check_id_pw(w_entry1.get(),w_entry2.get(),win3))
    login_btn1.pack()

def creat_new_butn1():#새로운 계정 만들기
    win2 = tkinter.Toplevel()
    c_label1 = Label(win2,text="<creat_new_id>")
    c_label2 = Label(win2,text="ID")
    c_entry1 = Entry(win2)
    c_label3=Label(win2,text="PASSWORD") 
    c_entry2 = Entry(win2,show="*")
    c_label4=Label(win2,text="PASSWORD_repeat") 
    c_entry3 = Entry(win2,show="*")
    creat_ok_btn1 = Button(win2,text="OK",command=lambda:creat_new_id_error(c_entry1.get(),c_entry2.get(),c_entry3.get(),win2))
    ps1 = c_entry1.get()
    ps2 = c_entry3.get()
    c_label1.pack()
    c_label2.pack()
    c_entry1.pack()
    c_label3.pack()
    c_entry2.pack()
    c_label4.pack()
    c_entry3.pack()
    creat_ok_btn1.pack()

def creat_new_id_error(new_id,new_pw,new_pw2,x):#새로운 아이디 만들때 생기는 오류
    with open("idlist.txt","r") as idl:
        id_list1 = idl.readlines()
        # a = id_list1.index(new_id+"\n")
        if new_id+"\n" not in id_list1 and new_pw == new_pw2 and len(new_id) > 5 and len(new_pw) > 5:
            with open('idlist.txt',"a") as id:
                # id.write(f'{new_id}\n')
                id.write(new_id + "\n")                
            with open("pwlist.txt","a") as pw:
                pw.write(new_pw + "\n")
            with open("leftmoney.txt","a") as lftmnytxt:
                lftmnytxt.write("0"+"\n")    
            msgbox.showinfo("success","success")
            x.withdraw()
        elif new_id+"\n" in id_list1:
            msgbox.showerror("error","exist id")
        elif len(new_id) < 5:
            msgbox.showerror("error","your id is too short, more than 5 letters plz")
        elif len(new_pw) < 5:
            msgbox.showerror("error","your pw is too short, more than 5 letters plz") 
        elif new_pw != new_pw2:
            msgbox.showerror("error","incorrect pw")

def check_account():
    win2 = tkinter.Toplevel()
    d_label1 = Label(win2,text="<check account>")
    d_label2 = Label(win2,text="ID")
    d_entry1 = Entry(win2)
    d_label3=Label(win2,text="PASSWORD") 
    d_entry2 = Entry(win2,show="*")
    d_label1.pack()
    d_label2.pack()
    d_entry1.pack()
    d_label3.pack()
    d_entry2.pack()
    login_btn1= Button(win2,text="LOG IN",command=lambda:check_account_login(d_entry1.get(),d_entry2.get(),win2))
    login_btn1.pack()

def check_account_login(id,pw,x):
    with open("idlist.txt","r") as log_id:
        id_login_list = log_id.readlines()
    with open("pwlist.txt","r") as log_pw:
        pw_login_list = log_pw.readlines()
    if str(id)+"\n" in id_login_list and str(pw)+"\n" in pw_login_list and id_login_list.index(str(id)+"\n")==pw_login_list.index(str(pw)+"\n"):
        check_account_second_page(id_login_list.index(str(id)+"\n"))
        x.withdraw()
    else:
        msgbox.showerror("error","your id is not correct")
        x.withdraw()

def check_account_second_page(a):
    win2 = tkinter.Toplevel()
    with open("leftmoney.txt","r") as li:
        left_money_list = li.readlines()
    l1 = Label(win2,text="  your left account money:  ")
    l2 = Label(win2,text=left_money_list[a])
    l1.pack()
    l2.pack()

btn = Button(win,text="deposit",command=lambda:deposit_butn1())
btn2 = Button(win,text="withdraw",command=lambda:withdraw_butn1())
btn3 = Button(win,text="creat new",command=lambda:creat_new_butn1())
btn4 = Button(win,text="check my bank account",command=lambda:check_account())
btn.pack()
btn2.pack()
btn4.pack()
btn3.pack()
win.mainloop()