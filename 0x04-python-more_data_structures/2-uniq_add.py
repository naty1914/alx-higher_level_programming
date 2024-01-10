#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq_number = []
    total = 0
    
    for num in my_list:
        if num  not in  uniq_number:
           total += num
           uniq_number.append(num)
          
    return total
