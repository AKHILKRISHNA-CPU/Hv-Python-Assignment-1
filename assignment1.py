#Question 1
#
a=int(input("Enter the First Number:"))
b=int(input("Enter the Second Number:"))
c=int(input("Enter the Third Number:"))
d=int(input("Enter the Fourth Number:"))
e=int(input("Enter the Fifth Number :"))
if (a <=0 or b<=0 or c<=0 or d<=0 or e<=0):
    print("Make Sure the Number Entered is Postive")
else: 
    sum=a+b+c+d+e
    x=open('products.txt','a')
    print("The Total Sum of all the Five Numbers is :",sum,file=x) # used to save the file in txt
    print("The Total Sum of all the Five Numbers is :",sum) #used to display the data in the console 
  


# Question 2
# The key value brand name is fetched and the color is taken from the user as a input

Car={'Brandname':'Honda',
     'Color': ''
     }
Car['Color'] = input("Enter the color as per requirement: ")
for key,value in Car.items():
    x=open('products.txt','a')
    print(key,value,file=x) # it is to save the file in txt
    print(key,value)#used to display the data in the console 



