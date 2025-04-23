print("type one number ")
x=int(input())
x1 = x//2
T = x-(x1*2)

x2 = x//3
T2 = x-(x2*3)

if  (T==2 or T==1) and (T2==2 or T2==1):
    print("The number is a prime number")
elif  x==2 or x==3  :
    print("The number is a prime number")
elif T==0 or T2 == 0 :
    print("sorry""  ,  ""The number is  NOT a prime number")
else :
    print("sorry""  ,  ""The number is  NOT a prime number")
