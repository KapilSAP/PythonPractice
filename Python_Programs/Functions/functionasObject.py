# immutable objects : number, string and float
# mutable objects: list, dictionary, set  
# pass by value for immutable objects, value does not change of outside function scope.
# pass by reference for mutable objects, value does change of outside function scope

#following is example of immutable objects with pass by value

x= 2

def add_num(num): #args pass by value and num is changed as this is within the functional scope and hold difference base address in memory
    num += 2;

add_num(x) #pass by value actually copy the value to the passed args, num will change not x, x is global scope. 

print(x) # this will be 2 or 4, check 

#following is example of mutable objects with pass by reference

def add_to_list(some_list, item): # list is passed by reference not value,for mutable objects base address would not change in memory
    some_list.append(item)

lst = [1,2,4]

add_to_list(lst,5)

print (lst) #lst will change here since list is mutable object

# Question, what will happen if list is also immutable object? 