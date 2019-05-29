
# coding: utf-8

# In[ ]:



##we  store initial data here 
import shelve #it is a simple persistant storage option
from getpass import getpass#this module prints prompt then reads input
import os#this module provides functions for interacting with the operating system
import time#this module handle time related tasks


acc1 = { 'name':'ram','bal':20000,'password':'123'}
acc2 = { 'name':'shyam','bal':15000,'password':'@hello'}
acc3 = { 'name':'ghyanshaym','bal':1000,'password':'bye@'}
acc4 = { 'name':'radheshyam','bal':12000,'password':'redhat'}

db = shelve.open("Bank/bank.db")
db['1001'] = acc1
db['1002'] = acc2
db['1003'] = acc3
db['1004'] = acc4 

db.close()

#This is the main menu from where our application will start
#by which you can login and signup and exit
#it has extra feature like admin can also login
def main_menu():
    try:
        
        s = """\t\t1. Login\n\t\t2.Signup\n\t\t3.admin \n\t\t4.Exit"""
        print(s)
        ch = int(input("Enter your Choice : "))
        if ch == 1 :
            acc_no = input("\t\t\t\tEnter your acc number : ").strip()
            password = getpass("\t\t\t\tEnter your password : ")
            if login(acc_no,password) :
                os.system("cls")#this function is use to clear the screen on the terminal
                menu(acc_no)
            else :
                os.system("cls")
                main_menu()
        elif ch==2:
            os.system("cls")
            sign_up()
        elif ch==3:
            os.system("cls")
            admin()
        elif ch==4:
            os.system("cls")
            Exit()
        else:
            os.system("cls")
            print("\t\t\t\tInvalide choice")
            time.sleep(4)#this functions sleep the program for given seconds for providing
            os.system("cls")#realistic environment
            main_menu()
    except BaseException as arg:#this block use to catch the exceptions
        os.system("cls")
        print("Error !",arg)
        main_menu()
        
# This function process the functionality of login system
def login(acc_no,password):
    try:
        db = shelve.open('Bank/bank.db')
        data = db.get(acc_no,False)
        if data : 
            if data.get('password') == password :
                os.system("cls")
                print("\t\t\t\tLogin Sucessfull")
                m = time.ctime()+":"+"login :"+"user :"+acc_no +"\n"
                f = open('log.txt','a')
                f.write(m)
                f.close()
                time.sleep(4)
                return True 
            else : 
                os.system("cls")
                print("\t\t\t\tInvalid Password")
                print("\t\t\t\tTry Again")
                m = time.ctime()+":"+"Error :"+"invalid password for user  :"+acc_no+"\n"
                f = open('log.txt','a')
                f.write(m)
                f.close()
                time.sleep(4)
                return False 
        else :
            os.system("cls")
            print("\t\t\t\tInvalid Account Number")
            print("\t\t\t\tIf you don't have any account please signup")
            #below code use for log purpose 
            m = time.ctime()+":"+"Error :"+" invalid account number :"+ acc_no +"\n"
            f = open('log.txt','a')
            f.write(m)
            f.close()
            time.sleep(4)
            return False
        db.close()
    except BaseException as arg:
        print("Error !",arg)
        os.system("cls")
        main_menu()
# This is the menu which provide to the user after login to do the transactions        
def menu(acc_no):
    try:
        s = """\t\t1. Credit\n\t\t2.Debit\n\t\t3.Check Balance\n\t\t4.Update Password\n\t\t5.exit"""
        print(s)
        ch = int(input("\t\t\t\tEnter your choice : "))
        if ch==1:
            os.system("cls")
            credit(acc_no)
        elif ch==2:
            os.system("cls")
            debit(acc_no)
        elif ch==3:
            os.system("cls")
            check_details(acc_no)
        elif ch == 4 :
            os.system("cls")
            update_password(acc_no)
        elif ch==5:
            os.system("cls")
            exit()
        else:
            os.system("cls")
            print("\t\t\t\tInvalid choice")
            print("\t\t\t\tyou are at menu of logged in function")
            time.sleep(4)
            os.system("cls")
            main_menu()
    except BaseException as arg:
        os.system("cls")
        print("Error !",arg)
        main_menu()
        # This function use to credit the balance from user account
def credit(acc_no):
    try:
        amount=float(input("\t\t\Enter the amount which you want to credit into your account  :"))
        db = shelve.open('Bank/bank.db',writeback=True)
        old_balance=db[acc_no]["bal"]
        print(old_balance)
        new_balance=old_balance+amount
        print(new_balance)
        db[acc_no]["bal"]=new_balance
        update=db[acc_no]["bal"]
        print("\t\t\t\tYour balance is updated.",update)
        db.close()
        m = time.ctime()+":"+" credited : "+str(amount)+"  in account  "+acc_no+"\n" 
        f = open('log.txt','a')
        f.write(m)
        f.close()
        time.sleep(4)
        os.system("cls")
        menu(acc_no)
    except BaseException as arg:
        print("Error !",arg)
        time.sleep(4)
        os.system("cls")
        main_menu()
        # This function use to debit the amount to the user account
def debit(acc_no):
    try:
        amount=float(input("\t\t\t\tEnter the amount which you want to debit"))
        db = shelve.open('Bank/bank.db',writeback=True)
        old_balance=db[acc_no]["bal"]
        if old_balance<amount:
            print("\tSorry ! we can not debit that much money from your account\n due to insufficient balance.")
            time.sleep(4)
            os.system("cls")
            debit(acc_no)
        else:
            new_balance=old_balance-amount
            db[acc_no]["bal"]=new_balance
            print("\t\t\t\tSuccessfully debited.")
            update=db[acc_no]["bal"]
            print("\t\t\t\tYour current updated balance is\n\t",update)
            db.close()
            m = time.ctime()+":"+" debited : "+" amount : "+str(amount)+" in "+acc_no+"\n"
            f = open('log.txt','a')
            f.write(m)
            f.close()
            time.sleep(4)
            os.system("cls")
            menu(acc_no)
    except BaseException as arg:
        print("Error !",arg)
        time.sleep(4)
        os.system("cls")
        main_menu()
        # This function provide the details about the user account including their password
def check_details(acc_no):
    try:
        db = shelve.open('Bank/bank.db',writeback=True)
        details=db[acc_no]
        print(f"\t\t\t\tYour account details is \t\n\t {details}")
        db.close()
        m = time.ctime()+" : "+" check details  : " + "for account  "+acc_no+"\n"
        f = open('log.txt','a')
        f.write(m)
        f.close()
        time.sleep(4)
        os.system("cls")
        menu(acc_no)
    except BaseException as arg:
        print("Error !",arg)
        time.sleep(4)
        os.system("cls")
        main_menu()
        # By this function any user can update their password
    
def update_password(acc_no):
    try:
        p1 = getpass("\t\t\t\tEnter password : ")
        p2 = getpass("\t\t\t\tVerify password :")
        if p1 == p2 : 
            db = shelve.open('Bank/bank.db',writeback=True)
            db[acc_no]['password'] = p1
            print("\t\t\t\tpassword sucessfully updated")
            print("\t\t\t\tPlease Login Again to verify ")
            db.close()
            m = time.ctime()+":"+" update password : "+"of account "+acc_no+" new password is :"+p1+":\n"
            f = open('log.txt','a')
            f.write(m)
            f.close()
            time.sleep(4)
            os.system("cls")
            main_menu()
        else : 
            print("\t\t\t\tPassword does not match ")
            print("\t\t\t\tTry Again")
            time.sleep(4)
            os.system("cls")
            update_password(acc_no)
    except BaseException as arg:
        print("Error !",arg)
        time.sleep(4)
        os.system("cls")
        main_menu()
def exit():
    print("\t\t\t\tThanks for using our services.")
    time.sleep(4)
    os.system("cls")
    main_menu()
    #if any user is new and want to open their account in the bank then he/she can use this 
    #function for sign-up 
    #they can open their account from 0 balance too
def sign_up():
    try:

        db = shelve.open('Bank/bank.db',writeback=True)
        acc_no=int(input("\t\t\t\tEnter your account number "))
        data=list(map(int,db.keys()))
        print(data)
        if acc_no in data:
            print("\t\t\t\tSorry ! This account number is already exit.")
            print("\t\t\t\tTry Again .")
            time.sleep(4)
            os.system("cls")
            sign_up()
        else:
            print("\t\t\t\tPlease enter your details")
            new_user={
                    'name':input("Enter your name.").strip().lower(),
                    'bal':int(input("Enter your opening balance.")) ,
                    'password': getpass("Enter your password.")
                }
            db[str(acc_no)]=new_user
            db.close()
            print("\t\t\t\tyour accound is succesfully added.")
            m = time.ctime()+":"+" Sign up : "+str(acc_no)+" \n"
            f = open('log.txt','a')
            f.write(m)
            f.close()
            time.sleep(4)
            os.system("cls")
            main_menu()
    except BaseException as arg:
        print("Error !",arg)
        time.sleep(4)
        os.system("cls")
        main_menu()
    #due to this function user will able to exit from the menu 
def Exit():
    print("\t\t\t\tThanks for using our services.")
    #This function is only made for the admin 
    #only admin can access this function with the help of password
    #password is in-built so it will provide by the developer 
def admin():
    try:
        exits_password="mai hun don"
        password=getpass("\t\t\t\tEnter yous password admin : ")
        if exits_password==password:
            print("\t1.Reset password\t\n2.Delete Account \t\n3. Account details\t\n4main_menu")
            ch=int(input("\t\t\t\tEnter your choice : "))
            if ch==1:
                os.system("cls")
                reset_password()
            elif ch==2:
                os.system("cls")
                delete_account()
            elif ch==3:
                os.system("cls")
                account_details()
            elif ch==4:
                os.system("cls")
                main_menu()
            else:
                print("\t\t\t\tInvalid choice.")
                time.sleep(4)
                os.system("cls")
                admin()
        else:
            print("\t\t\t\tIncorrect Password")
            print("\t\t\t\tTry again .")
            m = time.ctime()+":"+" admin "+" try to login "+"\n"
            f = open('log.txt','a')
            f.write(m)
            f.close()
            time.sleep(4)
            os.system("cls")
            main_menu()
    except BaseException as arg:
        print("Error !",arg)
        time.sleep(4)
        os.system("cls")
        main_menu()
        #This function is made for the admin to reset the password of users
def reset_password():
    try:
        acc_no=input("\t\t\t\tEnter account number ").strip()
        password=input("\t\t\t\tEnter the new password ")
        password_2=input("\t\t\t\tEnter the new password again .")
        if password==password_2:
            db = shelve.open('Bank/bank.db',writeback=True)
            db[acc_no]["password"]=password
            db.close()
            print("\t\t\t\tUser's password succesfully change.")
            time.sleep(4)
            m=time.ctime()+":"+" Admin reset the password of account "+acc_no+" password is "+password+"\n"
            f=open("log.txt","a")
            f.write(m)
            f.close()
            os.system("cls")
            main_menu()
        else:
            print("\t\t\t\tPassword does not match\t\t\n Please try again !")
            time.sleep(4)
            os.system("cls")
            admin()
    except BaseException as arg:
        print("Error !",arg)
        time.sleep(4)
        os.system("cls")
        main_menu()
        #this fucntion is also made for admin to delete any account
def delete_account():
    try:
        acc_no=input("\t\t\t\tEnter account number which you want to delete.").strip()
        db = shelve.open('Bank/bank.db',writeback=True)
        del db[acc_no]
        print("\t\t\t\tAccount is deleted")
        db.close()
        m=time.ctime()+":"+" Admin deleted an account "+" number is "+acc_no+"\n"
        time.sleep(4)
        os.system("cls")
        main_menu()
    except BaseException as arg:
        print("Error !",arg)
        time.sleep(4)
        os.system("cls")
        main_menu()
        #with the help of this function admin can check the details of their users
def account_details():
    try:
        db = shelve.open('Bank/bank.db',writeback=True)
        account=int(input("\t\t\t\tEnter the account Number "))
        data=list(map(int,db.keys()))
        print(data)
        if account in data:
            details=db[str(account)]
            print(details)
            db.close()
            time.sleep(4)
            os.system("cls")
            admin()
        else:
            print("\t\t\t\tAccount is not present")
            time.sleep(4)
            os.system("cls")
            admin()
    except BaseException as arg:
        print("Error !",arg)
        time.sleep(4)
        os.system("cls")
        main_menu()
    #This is the information function which provide the starting inteerface for the users
def info():
    details="Welcome to Bank Management System".center(510,"*")
    print(details)
    print("\t\t\t\tCreated by - Afzal Ali")
    time.sleep(4)
    os.system("cls")
if __name__=="__main__":#if we use this file as a script then the below code will be excute
                        #if we use this file as a module then the below code won't be excute
                    #but still we can  use all the functionality of the code by importing it.
    #The below code will automatically excute whenever we run this code as a script.
    info()
    main_menu()
    print("\t\t\t\t\t-----existing-----")
    time.sleep(3)
    os.system("cls")


# #### 
