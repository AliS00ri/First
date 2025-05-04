print ("Do you want numbers to be added, subtracted, multiplied, or divided?")
operations = input()

print("enter Number 1")
N1 = int(input())

print("enter Number 2")
N2 = int(input())

if operations == "added" :
    print(N1+N2)
elif operations == "subtracted" :
    print(N1-N2)
elif operations == "multiplied" :
    print(N1*N2)
elif operations == "divided" :
    print(N1/N2)
else :
    print(" sorry, I didn't understand.")