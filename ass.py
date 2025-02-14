# Exercise 1
age=int(input("Enter your age : "))

if age<3 :
    price =0
elif age<=12:
    price =7;
elif age<=40:
    price= 10;
else :
    price =12;
    
print("The ticket price is :$" + str(price));
# End of Exercise 1
      
# Exercise 2

number=int(input("Enter a number: "))
if number%2==0:
 print("The number is even.")
else:
    print("The number is odd.")
    
# End of Exercise 2
    

#Exercise 3

Musername="admin";
PPassword=1234;

username=input("Enter your username:")
Password=input("Enter your password")
if username==Musername and Password==PPassword:
    print("Access granted")
    
else : print("Access Denied")