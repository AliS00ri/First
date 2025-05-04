print("enter a number")
Number = str(input())
reverse_Number = Number[::-1]

if Number == reverse_Number:
    print("This is a palindrome number ")
else:
    print("This is not a palindrome number")
