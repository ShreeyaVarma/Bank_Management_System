import pickle
def create():
    f1=open("Banking Management System.dat","wb")
    n=eval(input("Enter total no. of accounts: "))
    l=[]
    for i in range (n):   
        name=input("Enter name: ")
        acc=eval(input("Enter acc no: "))
        pin=eval(input("Enter pin: "))
        emid=eval(input("Enter Emirates ID: "))
        dob=eval(input("Enter DoB in the form of list: "))
        phone=eval(input("Enter phone no: "))
        email=input("Enter email address: ")
        address=input("Enter home address: ")
        current=eval(input("Enter amount in current account: "))
        cdate=eval(input("Enter current account creation date in the form of list: "))
        savings=eval(input("Enter amount in savings account: "))
        sdate=eval(input("Enter savings account creation date in the form of list: "))
        fd=eval(input("Enter amount in term deposit account: "))
        fddate=eval(input("Enter term deposit account creation date in the form of list: "))
        l1=[name,acc,pin,emid,dob,phone,email,address,current,cdate,savings,sdate,fd,fddate]
        l.append(l1)
    pickle.dump(l,f1)
    f1.close()

    f2=open("creditcard.dat","ab")
    l=[]
    pickle.dump(l,f2)
    f2.close()

    f3=open("debitcard.dat","ab")
    l=[]
    pickle.dump(l,f3)
    f3.close()
    
    f4=open("studentloan.dat","ab")
    l=[]
    pickle.dump(l,f4)
    f4.close()
    
    f5=open("mortgageloan.dat","ab")
    l=[]
    pickle.dump(l,f5)
    f5.close()
    
    f6=open("personalloan.dat","ab")
    l=[]
    pickle.dump(l,f6)
    f6.close()
    
def display():    
    f2=open("Banking Management System.dat","rb")
    try:
        while True:
            s=pickle.load(f2)
            for i in s:
                print(i)
    except EOFError:
        f2.close()

def search1():  #by accno
    f=open("Banking Management System.dat","rb")
    a=eval(input("Enter acc no to search: "))
    try:
        while True:
            s=pickle.load(f)
            for i in s:
                if i[1]==a:
                    print(i)
    except EOFError:
        f.close()
    
def search2():  #by name
    f=open("Banking Management System.dat","rb")
    a=input("Enter name to search: ")
    try:
        while True:
            s=pickle.load(f)
            for i in s:
                if i[0]==a:
                    print(i)
    except EOFError:
        f.close()
    
def insert():
    f=open("Banking Management System.dat","ab")
    n=eval(input("Enter total no of accounts: "))
    l=[]
    for i in range (n):   
        name=input("Enter name: ")
        acc=eval(input("Enter acc no: "))
        pin=eval(input("Enter pin: "))
        emid=eval(input("Enter Emirates ID: "))
        dob=eval(input("Enter DoB in the form of list: "))
        phone=eval(input("Enter phone no: "))
        email=input("Enter email address: ")
        address=input("Enter home address: ")
        current=eval(input("Enter amount in current account: "))
        cdate=eval(input("Enter current account creation date in the form of list: "))
        savings=eval(input("Enter amount in savings account: "))
        sdate=eval(input("Enter savings account creation date in the form of list: "))
        fd=eval(input("Enter amount in term deposit account: "))
        fddate=eval(input("Enter term deposit account creation date in the form of list: "))
        l1=[name,acc,pin,emid,dob,phone,email,address,current,cdate,savings,sdate,fd,fddate]
        l.append(l1)
    pickle.dump(l,f)
    f.close()

          

#CUSTOMER
       
def display2():
    f1=open("Banking Management System.dat","rb")
    a=eval(input("Enter your account number: "))
    try:
        while True:
            s=pickle.load(f1)
            for i in s:
                if i[1]==a:
                    print("Name: ", i[0])
                    print("Acc no: ", i[1])
                    print("Pin: ", i[2])
                    print("Emirates ID: ", i[3])
                    print("Date of birth: ", i[4])
                    print("Phone no: ", i[5])
                    print("Email ID: ", i[6])
                    print("Address: ", i[7])
                    print("Amount in Current account: ", i[8])
                    print("Current account creation date: ", i[9])
                    print("Amount in Savings account: ", i[10])
                    print("Saving account creation date: ", i[11])
                    print("Amount in Term deposit account: ", i[12])
                    print("Term deposit account creation date: ", i[13])

    except EOFError:
        f1.close()

def deposit():
    f1=open("Banking Management System.dat","rb")
    a=eval(input("Enter acc no. to search: "))
    pin=eval(input("Enter pin: "))
    flag=0
    try:
        while True:
            l=pickle.load(f1)
            for i in l:
                if i[1]==a and i[2]==pin:
                    flag=1
                    while True:
                        print("1. Deposit into Current acc")
                        print("2. Deposit into Savings acc")
                        print("3. Deposit into Term deposit acc")
                        print("4. Exit")
                        c=eval(input("Enter your choice: "))
                        if c==1:
                            amt=eval(input("Enter amount to deposit: "))
                            i[8]+=amt
                            print(i)
                        elif c==2:
                            amt=eval(input("Enter amount to deposit: "))
                            i[10]+=amt
                            print(i)
                        elif c==3:
                            amt=eval(input("Enter amount to deposit: "))
                            i[12]+=amt
                            print(i)
                        elif c==4:
                            break
            else:
                f1.seek(0)
                pickle.dump(l,f1)
                    
    except EOFError:
        if flag==0:
            print("Account/ Pin invalid")
        f1.close()
        

def withdraw():
    f1=open("Banking Management System.dat","rb+")
    a=eval(input("Enter acc no. to search: "))
    pin=eval(input("Enter pin: "))
    flag=0
    try:
        while True:
            l=pickle.load(f1)
            for i in l:
                if i[1]==a and i[2]==pin:
                    flag=1
                    while True:
                        print("1. Withdraw from Current acc")
                        print("2. Withdraw from Savings acc")
                        print("3. Withdraw from Term deposit acc")
                        print("4. Exit")
                        c=eval(input("Enter your choice: "))
                        if c==1:
                            amt=eval(input("Enter amount to withdraw: "))
                            i[8]-=amt
                            print(i)
                        elif c==2:
                            amt=eval(input("Enter amount to deposit: "))
                            i[10]-=amt
                            print(i)
                        elif c==3:
                            amt=eval(input("Enter amount to deposit: "))
                            i[12]-=amt
                            print(i)
                        elif c==4:
                            break

            else:
                f1.seek(0)
                pickle.dump(l,f1)
            
    except EOFError:
        if flag==0:
            print("Account no./Pin invalid")
        f1.close()

    
def balance():
    #savings, fd, amount
    f1=open("Banking Management System.dat","rb+")
    a=eval(input("Enter acc no. to search: "))
    pin=eval(input("Enter pin: "))
    date=eval(input("Enter today's date in the form of list: "))
    flag=0
    try:
        while True:
            l=pickle.load(f1)
            for i in l:
                if i[1]==a and i[2]==pin:
                    flag=1
                    while True:
                        print("1. Display balance of the Current account")
                        print("2. Display balance of the Savings account")
                        print("3. Display balance of the Term deposit account")
                        print("4. Exit")
                        c=eval(input("Enter your choice: "))
                        if c==1:
                            print("Balance=",i[8])
                        elif c==2:
                            if date[2]==i[11][2]:
                                t=(date[1]-i[11][1])/12 
                            else:
                                y=date[2]-i[11][2]
                                t=((date[1]-i[11][1])+(y*12))/12
                            amt=i[10]
                            amt2=amt*((1+(0.01/12))**(12*t)) #Rate=1%
                            print("Balance=",amt2)
                            i[10]=amt2
                        elif c==3:
                            if date[2]==i[13][2]:
                                t=(date[1]-i[13][1])/12 
                            else:
                                y=date[2]-i[13][2]
                                t=((date[1]-i[13][1])+(y*12))/12
                            amt=i[12]
                            amt2=amt*((1+(0.02/12))**(12*t)) #Rate=2%
                            print("Balance=",amt2)
                            i[12]=amt2
                        elif c==4:
                            break
            else:
                f1.seek(0)
                pickle.dump(l,f1)

    except EOFError:
         if flag==0:
            print("Account no./Pin invalid")
    f1.close()

    
def update():
    try:
        f=open("Banking Management System.dat",'rb+')
        s=pickle.load(f)
        found=0
        A=eval(input("Enter the account no. whose details to be changed: "))
        pin=eval(input("Enter pin: "))
        for i in s:
            if i[1]==A and i[2]==pin:
                found=1
                while True:
                    print("What do you want to change: \n\na) Name \nb) Pin \nc) Emirates ID \nd) Mobile number \ne) Email ID \nf) Address \ng) Exit")
                    c=input("Enter choice: ")
                    if c=='a':   
                        i[0]=input("Enter new name: ")
                    elif c=='b':   
                        i[2]=eval(input("Enter new pin: "))
                    elif c=='c':
                        i[3]=eval(input("Enter new Emirates ID no.: "))                       
                    elif c=='d':
                        i[5]=eval(input("Enter new mobile number: "))
                    elif c=='e':
                        i[6]=input("Enter new email ID: ")
                    elif c=='f':
                        i[7]=input("Enter new address: ")
                    elif c=='g':
                        break
        else:
            f.seek(0)
            pickle.dump(s,f)
    except EOFError:
        if found==0:
            print("Account no./Pin invalid")
        f.close()

def applycard():
    f1=open("Banking Management System.dat","rb")
    a=eval(input("Enter acc number: "))
    pin=eval(input("Enter pin: "))
    flag=0
    try:
        while True:
            s=pickle.load(f1)
            for i in s:
                if i[1]==a and i[2]==pin:
                    flag=1
                    while True:
                        print("1. Apply for Credit card")
                        print("2. Apply for Debit card")
                        print("3. Exit")
                        c=eval(input("Enter your choice: "))
                        if c==1:
                            f2=open("creditcard.dat","rb+")
                            l=pickle.load(f2)
                            l=[]
                            pin=eval(input("Enter credit card pin: "))
                            amt=eval(input("Enter credit limit: "))
                            bill=0
                            createdate=eval(input("Enter creation date in the form of list: "))
                            usedate=eval(input("Enter date of last use in the form of list: "))
                            expdate=[createdate[0],createdate[1],createdate[2]+3]
                            l1=[i[0],i[1],pin,amt,bill,createdate,usedate,expdate]
                            print(l1)
                            l.append(l1)
                            f2.close()
                            f3=open("creditcard.dat","wb")
                            pickle.dump(l,f3)
                            f3.close()
                        elif c==2:
                            f2=open("debitcard.dat","rb+")
                            L=pickle.load(f2)
                            L=[]
                            pin=eval(input("Enter debit card pin: "))
                            amt=i[8]
                            createdate=eval(input("Enter creation date in the form of list: "))
                            usedate=eval(input("Enter date of last use in the form of list: "))
                            expdate=[createdate[0],createdate[1],createdate[2]+3]
                            l1=[i[0],i[1],pin,amt,createdate,usedate,expdate]
                            print(l1)
                            L.append(l1)
                            f2.close()
                            f3=open("debitcard.dat","wb")
                            pickle.dump(L,f3)
                            f3.close()
                        elif c==3:
                            break

    except EOFError:
        if flag==0:
            print("Account no./Pin invalid")
        f1.close()

def displaycard():    
    f1=open("Banking Management System.dat","rb")
    a=eval(input("Enter your account number: "))
    pin=eval(input("Enter pin: "))
    try:
        while True:
            s=pickle.load(f1)
            for i in s:
                if i[1]==a and i[2]==pin:
                    flag=1
                    while True:
                        print("1. Display Credit card")
                        print("2. Display Debit card")
                        print("3. Exit")
                        c=eval(input("Enter your choice: "))
                        if c==1:
                            f2=open("creditcard.dat","rb+")
                            l=pickle.load(f2)
                            for i in l:
                                print("Name: ", i[0])
                                print("Acc no: ", i[1])
                                print("Pin: ", i[2])
                                print("Total amount: ",i[3])
                                print("Bill: ", i[4])
                                print("Application date: ", i[5])
                                print("Date of last use: ", i[6])
                                print("Expiry date: ", i[7])
                                f2.close()
                            
                        elif c==2:
                            f2=open("debitcard.dat","rb+")
                            l=pickle.load(f2)
                            for i in l:
                                print("Name: ", i[0])
                                print("Acc no: ", i[1])
                                print("Pin: ", i[2])
                                print("Total amount: ",i[3])
                                print("Application date: ", i[4])
                                print("Date of last use: ", i[5])
                                print("Expiry date: ", i[6])
                                f2.close()
                            
                        elif c==3:
                            break

    except EOFError:
        if flag==0:
            print("Account no./Pin invalid")
        f1.close()

def usecard():
    f1=open("Banking Management System.dat","rb")
    a=eval(input("Enter acc no.: "))
    flag=0
    try:
        while True:
            print("1. Use Credit card")
            print("2. Use Debit card")
            print("3. Exit")
            c=eval(input("Enter your choice: "))
            if c==1:
                f2=open("creditcard.dat","rb")
                pin=eval(input("Enter credit card pin: "))
                l=pickle.load(f2)
                for i in l:
                    if i[1]==a and i[2]==pin:
                        flag=1
                        bill=eval(input("Enter payment amount: "))
                        i[4]+=bill
                        i[3]-=bill
                        i[6]=eval(input("Enter today's date in the form of list: "))
                
                f2.close()
                f2=open("creditcard.dat","wb")
                pickle.dump(l,f2)
                f2.close()
            
            elif c==2:
                f2=open("debitcard.dat","rb")
                f1=open("Banking Management System.dat","rb")
                pin=eval(input("Enter debit card pin: "))
                L=pickle.load(f2)
                l=pickle.load(f1)
                for i in L:
                    if i[1]==a and i[2]==pin:
                        flag=1
                        bill=eval(input("Enter payment amount: "))
                        i[3]-=bill
                        i[5]=eval(input("Enter today's date in the form of list: "))
                        L=pickle.load(f1)
                        for i in l:
                            if i[1]==a and i[2]==pin:
                                i[8]-=bill
                
                f2.close()
                f2=open("debitcard.dat","wb")
                pickle.dump(l,f2)
                f2.close()
                
            elif c==3:
                break
            
    except EOFError:
        if flag==0:
            print("Account no./Pin invalid")
        f1.close()
        

def balancecard():
    f1=open("Banking Management System.dat","rb")
    a=eval(input("Enter acc no.: "))
    date=eval(input("Enter today's date: "))
    flag=0
    try:
        while True:
            print("1. Check balance in Credit card")
            print("2. Check balance in Debit card")
            print("3. Exit")
            c=eval(input("Enter your choice: "))
            if c==1:
                f2=open("creditcard.dat","rb")
                pin=eval(input("Enter credit card pin: "))
                l=pickle.load(f2)
                for i in l:
                    if i[1]==a and i[2]==pin:
                        flag=1
                        if date[2]==i[6][2]:
                            t=(date[1]-i[6][1])/12 
                        else:
                            y=date[2]-i[6][2]
                            t=((date[1]-i[6][1])+(y*12))/12
                        b=i[4]
                        bill=b*((1+(0.24/12)**(12*t))) #Rate=24%
                        r=bill-b
                        i[4]=bill
                        i[3]-=r
                        print("Balance=",i[3])
                else:
                    f2.seek(0)
                    pickle.dump(l,f2)
                    f2.close()
                
            elif c==2:
                f2=open("debitcard.dat","rb")
                pin=eval(input("Enter debit card pin: "))
                L=pickle.load(f2)
                for i in L:
                    if i[1]==a and i[2]==pin:
                        flag=1
                        print("Balance=",i[3])
                else:
                    f2.seek(0)
                    pickle.dump(l,f2)
                    f2.close()
                    
            elif c==3:
                break
            
    except EOFError:
        if flag==0:
            print("Account no./Pin invalid")
        f1.close()

    
def paycreditcard():
    f1=open("creditcard.dat","rb")
    a=eval(input("Enter acc no.: "))
    flag=0
    try:
        pin=eval(input("Enter credit card pin: "))
        l=pickle.load(f1)
        for i in l:
            if i[1]==a and i[2]==pin:
                flag=1
                bill=i[4]
                print("Credit card debt:",bill)
                p=eval(input("Enter amount paid: "))
                if p<=bill:
                    i[3]+=p
                    i[4]-=p
                else:
                    i[3]+=p
                    i[4]=0
        f1.close()
        f2=open("creditcard.dat","wb")
        pickle.dump(l,f2)
        f2.close()
        
    except EOFError:
        if flag==0:
            print("Account no./Pin invalid")
        f1.close()

  
def disc():
    f1=open("Banking Management System.dat","rb")
    a=eval(input("Enter acc no. of the card to discontinue: "))
    flag=0
    try:
         while True:
            print("1. Discontinue Credit card")
            print("2. Discontinue Debit card")
            print("3. Exit")
            c=eval(input("Enter your choice: "))
            if c==1:
                f2=open("creditcard.dat","rb")
                pin=eval(input("Enter credit card pin: "))
                l=pickle.load(f2)
                for i in l:
                    if i[1]==a and i[2]==pin:
                        flag=1
                        l.remove(i)
                f2.close()
                f2=open("creditcard.dat","wb")
                pickle.dump(l,f2)
                f2.close()
                
            elif c==2:
                f2=open("debitcard.dat","rb")
                pin=eval(input("Enter debit card pin: "))
                l=pickle.load(f2)
                for i in l:
                    if i[1]==a and i[2]==pin:
                        flag=1
                        l.remove(i)
                f2.close()
                f2=open("debitcard.dat","wb")
                pickle.dump(l,f2)
                f2.close()
                
            elif c==3:
                break
            
    except EOFError:
        if flag==0:
            print("Account no./Pin invalid")
        f1.close()
        

def issuecheque():
    f2=open("Banking Management System.dat","rb+")
    a=eval(input("Enter your account number: "))
    p=eval(input("Enter your pin to proceed: "))
    flag=0
    try:
        while True:
            s=pickle.load(f2)
            for i in s:
                if i[1]==a and i[2]==p:
                    flag=1
                    name=input("Enter the name of the person you wish to transfer this amount to: ")
                    amt=eval(input("Enter the total amount you wish to transfer: "))
                    i[8]-=amt
                    print("Pay",name,"AED",amt,"only")
            
            else:
                f2.seek(0)
                pickle.dump(s,f2)
            
    except EOFError:
        if flag==0:
            print("Account no./Pin invalid")
        f2.close()

def depcheque():
    f2=open("Banking Management System.dat","rb+")
    a=eval(input("Enter your account number: "))
    p=eval(input("Enter your pin to proceed: "))
    flag=0
    try:
        while True:
            s=pickle.load(f2)
            for i in s:
                if i[1]==a and i[2]==p:
                    flag=1
                    n=input("Enter the name of the person on the cheque: ")
                    if n==i[0]:
                        amt=eval(input("Enter the total amount to deposit: "))
                        i[8]+=amt
                        print("Deposited",n,"AED",amt,"only")
            else:
                f2.seek(0)
                pickle.dump(s,f2)
                
    except EOFError:
        if flag==0:
            print("Account no./Pin invalid")
        f2.close()

def loan():
    f1=open("Banking Management System.dat","rb")
    a=eval(input("Enter acc no.: "))
    pin=eval(input("Enter pin: "))
    flag=0
    try:
        while True:
            f=open("loans.txt","r")
            print(f.read())
            f.close()
            print("1. Apply for Student loan")
            print("2. Apply for Mortgage loan")
            print("3. Apply for Personal loan")
            print("4. Exit")
            c=eval(input("Enter your choice: "))
            if c==4:
                break
            f1.seek(0)
            s=pickle.load(f1)
            for i in s:
                if i[1]==a and i[2]==pin:
                    flag=1
                    if c==1:
                        f2=open("studentloan.dat","rb+")
                        l=pickle.load(f2)
                        amt=eval(input("Enter loan amount: "))
                        createdate=eval(input("Enter application date in the form of list: "))
                        paydate=eval(input("Enter date of last installment in the form of list: "))
                        l1=[i[0],i[1],i[2],amt,createdate,paydate]
                        print(l1)
                        l.append(l1)
                        f2.close()
                        f1=open("studentloan.dat","wb")
                        pickle.dump(l,f1)
                        f1.close()
                    elif c==2:
                        f2=open("mortgageloan.dat","rb+")
                        l=pickle.load(f2)
                        amt=eval(input("Enter loan amount: "))
                        createdate=eval(input("Enter application date in the form of list: "))
                        paydate=eval(input("Enter date of last installment in the form of list: "))
                        l1=[i[0],i[1], i[2],amt,createdate,paydate]
                        print(l1)
                        l.append(l1)
                        f2.close()
                        f1=open("mortgageloan.dat","wb")
                        pickle.dump(l,f1)
                        f1.close()
                    elif c==3:
                        f2=open("personalloan.dat","rb+")
                        l=pickle.load(f2)
                        amt=eval(input("Enter loan amount: "))
                        createdate=eval(input("Enter application date in the form of list: "))
                        paydate=eval(input("Enter date of last installment in the form of list: "))
                        l1=[i[0],i[1],i[2],amt,createdate,paydate]
                        print(l1)
                        l.append(l1)
                        f2.close()
                        f1=open("personalloan.dat","wb")
                        pickle.dump(l,f1)
                        f1.close()

    except EOFError:
        if flag==0:
            print("Account no./Pin invalid")
        f1.close()

def displayloan(): 
    f1=open("Banking Management System.dat","rb")
    a=eval(input("Enter acc no.: "))
    pin=eval(input("Enter pin: "))
    date=eval(input("Enter today's date in the form of list: "))
    flag=0
    try:
        while True:
            print("1. Display Student loan")
            print("2. Display Mortgage loan")
            print("3. Display Personal loan")
            print("4. Exit")
            c=eval(input("Enter your choice: "))
            if c==1:
                f2=open("studentloan.dat","rb")
                l=pickle.load(f2)
                print(l)
                for i in l:
                    if i[1]==a and i[2]==pin:
                        flag=1
                        if date[2]==i[4][2]:
                            t=(date[1]-i[4][1])/12 
                        else:
                            y=date[2]-i[4][2]
                            t=((date[1]-i[4][1])+(y*12))/12
                        amt=i[3]
                        amount=amt*((1+(0.05/12)**(12*t))) #Rate=5%
                        i[3]=amount
                        print("Balance=",i[3])
                else:
                    f2.seek(0)
                    pickle.dump(l,f2)
                    f2.close()
                    
            elif c==2:
                f2=open("mortgageloan.dat","rb")
                l=pickle.load(f2)
                print(l)
                for i in l:
                    if i[1]==a and i[2]==pin:
                        flag=1
                        if date[2]==i[4][2]:
                            t=(date[1]-i[4][1])/12 
                        else:
                            y=date[2]-i[4][2]
                            t=((date[1]-i[4][1])+(y*12))/12
                        amt=i[3]
                        amount=amt*((1+(0.05/12)**(12*t))) #Rate=5%
                        i[3]=amount
                        print("Balance=",i[3])
                else:
                    f2.seek(0)
                    pickle.dump(l,f2)
                    f2.close()
                    
            elif c==3:
                f2=open("personalloan.dat","rb")
                l=pickle.load(f2)
                print(l)
                for i in l:
                    if i[1]==a and i[2]==pin:
                        flag=1
                        if date[2]==i[4][2]:
                            t=(date[1]-i[4][1])/12 
                        else:
                            y=date[2]-i[4][2]
                            t=((date[1]-i[4][1])+(y*12))/12
                        amt=i[3]
                        amount=amt*((1+(0.05/12)**(12*t))) #Rate=5%
                        i[3]=amount
                        print("Balance=",i[3])
                else:
                    f2.seek(0)
                    pickle.dump(l,f2)
                    f2.close()
                    
            elif c==4:
                break     
    except EOFError:
        if flag==0:
            print("Account no./Pin invalid")
        f1.close() 
               
                   
def repayloan():
    f1=open("Banking Management System.dat","rb")
    a=eval(input("Enter your account number: "))
    pin=eval(input("Enter your pin to proceed: "))
    flag=0
    try:
        while True:
            print("1. Repay Student loan")
            print("2. Repay Mortgage loan")
            print("3. Repay Personal loan")
            print("4. Exit")
            c=eval(input("Enter your choice: "))
            if c==1:
                f2=open("studentloan.dat","rb")
                l=pickle.load(f2)
                for i in l:
                    if i[1]==a and i[2]==pin:
                        flag=1
                        amt=i[3]
                        p=eval(input("Enter amount paid: "))
                        i[3]-=p 
                f2.close()
                f2=open("debitcard.dat","wb")
                pickle.dump(l,f2)
                f2.close()
                
            elif c==2:
                f2=open("mortgageloan.dat","rb")
                l=pickle.load(f2)
                for i in l:
                    if i[1]==a and i[2]==pin:
                        flag=1
                        amt=i[3]
                        p=eval(input("Enter amount paid: "))
                        i[3]-=p 
                f2.close()
                f2=open("debitcard.dat","wb")
                pickle.dump(l,f2)
                f2.close()
                    
            elif c==3:
                f2=open("personalloan.dat","rb")
                l=pickle.load(f2)
                for i in l:
                    if i[1]==a and i[2]==pin:
                        flag=1
                        amt=i[3]
                        p=eval(input("Enter amount paid: "))
                        i[3]-=p
                f2.close()
                f2=open("debitcard.dat","wb")
                pickle.dump(l,f2)
                f2.close()
                    
            elif c==4:
                break     
    except EOFError:
        if flag==0:
            print("Account no./Pin invalid")
        f1.close()
