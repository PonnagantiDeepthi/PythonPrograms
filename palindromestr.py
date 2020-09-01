#Program to find a string is Palindrome or not
string=input()
rev="".join(reversed(string))
if(string==rev):
    print("Palindrome")
else:
    print("not a palindrome")
    
