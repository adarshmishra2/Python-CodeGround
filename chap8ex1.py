list_one=[x for x in range(1,10)]
list_two=[x for x in range(2,20,2)]
def chop(my_list):
    del my_list[-1]
    del my_list[0]
    return None

print (list_one)
print (chop(list_one))
print ("chop chop...")
print (list_one),"\n"

def middle(my_list):
    return my_list[1:-1]

print (list_two)
new_list=middle(list_two)
print (new_list)
