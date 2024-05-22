def frequency(string) :
       
    dict = {}
    for i in string:
        if i in dict: 
            dict[i]+= 1
        else:
            dict[i] = 1
    print(dict)

if __name__ == '__main__': 
     string = input("enter a string: ")
     frequency(string)