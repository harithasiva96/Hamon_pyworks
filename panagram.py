def pangram(s):
    x = "abcdefghijklmnopqrstuvwxyz"
    s = s.lower()          # To make every input string in to lower case.
    for char in x:
        if char not in s:  # check whether every character in the input string is in x
             print("Not a pangram")
             break         # If a letter is not in the the input string ,the code breaks.
    else:
        print("Its a pangram")

if __name__ == '__main__':  
        s = input("Enter a string: ")
        pangram(s)










