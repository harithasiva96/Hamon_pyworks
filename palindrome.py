def palindrome(s):
    x=""
    for i in s:
        x = i+x
    if (x == s):
        print ("Its a palindrome")
    else:
        print ("Not a palindrome")

if __name__ == '__main__':
    s = str(input("Enter a string: "))
    palindrome(s)












            

  