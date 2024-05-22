def frequency(string) :
    dict = {}   
    for i in string: 
        if i in dict:   # check if the characters in string are there in dictionary
            dict[i]+= 1 # Increase count if the check is positive
        else:
            dict[i] = 1 # Remain the value 1 if the check is negative.
    print(dict)

if __name__ == '__main__': 
     string = input("enter a string: ") # Accept a string
     frequency(string)