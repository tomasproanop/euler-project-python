# Palindrome tester: 

str = 'JaVaJ'  
strstr = str.casefold()  
rev = reversed(str)  
      
if list(str) == list(rev):  
    print("It's a palindrome!")  
else:  
    print("It's not a palindrome!")  
