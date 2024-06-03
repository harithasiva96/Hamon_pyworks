import json
from math import sqrt
emp_list = []


def load_journal():
    # open a json file and allow permission to read the file.
    data = open('journal.json', 'r')
    # Read the file.
    text = data.read()
    # Load the read file.
    file = json.loads(text)
    # print(file)
    return file
load_journal()

  
def compute_phi(journal, event):
    # If the event is present and squirrel is true, both gain a value 1 hence n11.
    n11 = 0
    # if the event is present and squirrel is false, event gain a value 1 and squirrel 0, hence n10
    n10 = 0
    n01 = 0
    n00 = 0
    # Considering each dictionary of the list.
    for dict_1 in journal:
        squirrel = dict_1["squirrel"]
        # Applying conditional statements to find the observation on correlation.
        if event in dict_1["events"] and  squirrel:
            n11+=1
        if event   in dict_1['events'] and not squirrel:
            n10+=1
        if event not in dict_1['events'] and squirrel:
            n01+=1
        if event not in dict_1['events'] and not squirrel:
            n00+=1
    # Considering a single value( either the presence of event or squirrel , or the absence of event or squirrel) irrespective of the other.
    n1_ = n11 + n10 
    n0_ = n00 + n01
    n_1 = n01 + n11
    n_0 = n10 + n00
    phi = (n11 * n00 - n10 * n01) / sqrt(n1_ * n0_ * n_1 * n_0)
    return phi  
        
def compute_correlation():
    journal = load_journal()
    for element in journal:
            # considering the elements of key list of events
            for sub_element in element["events"]:
            # print(sub_element)
            # collecting the key list of events in to an empty list
                emp_list.append(sub_element)
            
            event = set(emp_list)
            list1 = list(event)
    print(list1)
    print(len(event))
    my_dict = {}
    for event in list1:
        my_dict[event] = compute_phi(journal, event)
    return(my_dict)


compute_correlation()

def diagnose():
    correlation = compute_correlation()
    # Find the minimum key value pair using get() attribute
    min_key = min(correlation, key=correlation.get)
    min_value = correlation[min_key]
    print(f"Highly positively correlated key-value pair: {min_key}, {min_value}")
     # Find the maximum key value pair using get() attribute
    max_key = max(correlation, key=correlation.get)
    max_value = correlation[max_key]
    print(f"Highly negatively correlated key-value pair: {max_key}, {max_value}")

diagnose()