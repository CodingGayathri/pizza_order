#small pizza = 100 rs
#medium size pizza = 200 rs
#large pizza = 300 rs
#pepper for small pizza is 30 rs
#"""""""" large pizz is 50 rs
#for extra cheese for any pizza is 20 rs

size=input("enter the size of pizza ")
bill=0
if size=='s' or size=='S':
    bill+=100
    print(f"your bill fpor small pizza is 100 rs ")
elif size=='M'or size== 'm':
    bill+=200
    print("your bill fpor medium pizza is 200 rs")
elif size=='L'or size== 'l':
    bill+=300
    print("your bill fpor large pizza is 300 rs")
else:
    print("enter valid size for pizza")

add_papperon = input("D u want pepper(Y/N)")
if add_papperon=='Y'or add_papperon=='y':
    if size=='s'or size=='S':
        bill+=30
    else:
        bill+=50
        
extra_cheese=input("do u want extra cheese? (Y/N)")
if extra_cheese=='y'or extra_cheese=='Y':
    bill+=20
    
print(f"your final bill is {bill}")
    

