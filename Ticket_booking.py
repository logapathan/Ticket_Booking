#Train Ticket Booking
class information:
    def __init__(self,from_location,to_location,doj,train_name,class_type,ticket_type,no_of_passengers):
        self.from_location=from_location
        self.to_location=to_location
        self.doj=doj
        self.train_name=train_name
        self.class_type=class_type
        self.ticket_type=ticket_type
        self.no_of_passengers=no_of_passengers



class login:
    def __init__(self,username,password):
        self.username=username
        self.password=password


    def loginpage(self):
        db_username = "ram"  # User information from database
        db_password = "12345"
        if self.username == db_username and self.password == db_password:
            return 2
        elif (self.username != db_username or self.password != db_password) and i < 2:
            return 0
        elif (self.username != db_username or self.password != db_password) and i >= 2:
            return 1

for i in range(3):
    username=input("Enter Your Username:")
    password=input("Enter Your Password:")
    login_obj=login(username,password)
    if login_obj.loginpage()==0:
        print("Incorrect username or password please try again!!!")
        continue
    elif login_obj.loginpage()==1:
        print("Too Many worng attempts try again after 10 minutes")
        break
    elif login_obj.loginpage()==2:
        print("Login Sucessful")

        break

if login_obj.loginpage()==2:
    from_location=input("Enter from location(chennai or bengaluru):")      
    to_location = input("Enter to location(chennai or bengaluru):")
    while((from_location!="chennai" and from_location!="bengaluru") or (to_location!="chennai" and to_location!="bengaluru") or (from_location==to_location)):
        print("Invalid locations Try again")
        from_location = input("Enter from location(chennai or bengaluru):")
        to_location = input("Enter to location(chennai or bengaluru):")
    doj=input("Enter date of journey (DD/MM/YY):")
    train_name=input("Enter train name:")
    class_type=input("Enter class type (sleeper or sitting):")
    while(class_type!="sleeper" and class_type!="sitting"):
        print("Invalid class type try again")
        class_type = input("Enter class type (sleeper or sitting):")
    ticket_type=input("Enter ticket type (general or taktal):")
    while(ticket_type!="general" and ticket_type!="taktal"):
        print("Invalid ticket type try again")
        ticket_type = input("Enter ticket type (general or taktal):")
    no_of_passengers=int(input("Enter no of passengers (should not be more than 6)"))
    while(no_of_passengers>6):
        print("Invalid,no of passengers is greater than 6")
        no_of_passengers = int(input("Enter no of passengers (should not be more than 6)"))
    info=information(from_location,to_location,doj,train_name,class_type,ticket_type,no_of_passengers)
    print("*****************************************************************")
    passenger_details={}
    for i in range(no_of_passengers):
        passenger_name=input(f"Enter passenger{i+1} name:")
        age=int(input(f"Enter passenger{i+1} age:"))
        gender=input(f"Enter passenger{i+1} gender:")
        id_number=input(f"Enter id{i+1} number:")
        print("-----------------------------------------------------------")
        passenger_details["passenger"+str(i)]={"passenger_name":passenger_name,
                                               "age":age,
                                               "gender":gender,
                                               "id_number":id_number,
                                               }
    mobile_number = int(input("Enter mobile number:"))
    email_id = input("Enter Email id:")
    if from_location=="chennai" and to_location=="bengaluru":
        price=1000
    elif from_location=="bengaluru" and to_location=="chennai":
        price=1200
    amount=price*no_of_passengers
    print("********************************************************")
    print(f"""Enter your payment method
              Total amount is {amount}
               1)UPI payment
               2)credit card
               3)debit card
               4)bank transfer
                                """)
    payment_method=int(input())
    while(payment_method>4):
        print("Invalid option try again!!!")
        payment_method = int(input(f"""Enter your payment method
              Total amount is {amount}
               1)UPI payment
               2)credit card
               3)debit card
               4)bank transfer
                                """))

    if payment_method==1:
        upi_id=input("Enter your upi id")
    elif payment_method==2:
        card_number=int(input("Enter your card number"))
        expiry_date=input("Enter Your expiry date")
    elif payment_method==3:
        card_number = int(input("Enter your card number"))
        expiry_date = input("Enter Your expiry date")
    elif payment_method==4:
        account_number=int(input("Enter account number:"))
        name=input("Enter account holder name:")
        ifsc=input("Enter your ifsc code:")
        branch=input("Enter your branch name:")
    print(f"""                               Payment Sucessful
              Ticket has been sent to registed email id {email_id} and mobile number {mobile_number}
""")








































