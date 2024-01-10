from mod import * 
while True:
    q=input("Are you an Admin? (Y/N/Exit): ")
    if q=="Y" or q=="y":
        while True:
            print("1. Create all accounts")
            print("2. Display all accounts")
            print("3. Search for an account")#customer also: SEARCH
            print("4. Add a new account")
            print("5. Exit") #break
            
            choice1=eval(input("Enter your choice: "))
            
            if choice1==1:
                create()

            elif choice1==2:
                display()

            elif choice1==3:
                ch=eval(input("1. Search by acc no \n2. Search by name\nEnter your choice: "))
                if ch==1:
                    search1()
                elif ch==2:
                    search2()
                else:
                    print("Error")

            elif choice1==4:
                insert()
                display()

            elif choice1==5:
                break
            else:
                print("Error")

            
    elif q=="N" or q=="n":
        while True:
            print("1. Display your account")
            print("2. Deposit amount")#  (Current,Savings,FD)
            print("3. Withdraw amount")           
            print("4. Check balance")
            print("5. Update data in account")           
            print("6. Apply for Credit/Debit Card")
            print("7. Display Credit/Debit Card credentials")            
            print("8. Use Credit/Debit Card")
            print("9. Check the balance in Credit/Debit Card")
            print("10. Pay off credit card debt")
            print("11. Discontinue your card")
            print("12. Issue a cheque")
            print("13. Deposit a cheque")
            print("14. Apply for Loan") 
            print("15. Display Loan payment amount")
            print("16. Repay your loan")
            print("17. Give us your feedback")
            print("18. Exit")

            choice2=eval(input("Enter your choice: "))
            if choice2==1:
                display2()

            elif choice2==2:
                deposit()

            elif choice2==3:
                withdraw()

            elif choice2==4:
                balance()

            elif choice2==5:
                update()

            elif choice2==6:
                applycard()

            elif choice2==7:
                displaycard()
            
            elif choice2==8:
                usecard()
            
            elif choice2==9:
                balancecard()
            
            elif choice2==10:
                paycreditcard()

            elif choice2==11:
                disc()

            elif choice2==12:
                issuecheque()

            elif choice2==13:
                depcheque()

            elif choice2==14:
                loan()

            elif choice2==15:
                displayloan()
            
            elif choice2==16:
                repayloan()

            elif choice2==17:
                print("Give us your feedback at: \nhttps://docs.google.com/forms/d/e/1FAIpQLSfxDeW6TwpxTj1e6sN-Zgru23YX17D72GjgAltPkMss_7fJhA/viewform?vc=0&c=0&w=1&flr=0\n")
            
            elif choice2==18:
                break

            else:
                print("Error")

    elif q=="Exit" or q=="exit":
        break
    else:
        print("Invalid input")
