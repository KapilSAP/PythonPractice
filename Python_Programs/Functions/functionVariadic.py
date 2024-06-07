#Variadic function which takes arbirarty number of arguments with * sign
#Variadic function which takes arbirarty number of arguments with ** sign
# * and ** are unpacking operator - things to remember
# one * is for positioning arguments 
# two ** for keywords arguments




def print_params(x, *args): #Variadic function which takes arbirarty number of arguments with * sign
    print("x: ", x)
    print("args", args)
    print("args[0]:", args[0])

print_params("a","b","c")

#Output:
# x a
# args ('b', 'c')
# args[0]: b

def print_params1(x, *args, **kwargs): #Variadic function which takes arbirarty number of key value arguments with * sign
    for item in args:
         print("kwargs:", item)
    for val in kwargs.values():
        print("kwargs['first']:", kwargs['first'])
        print("kwargs['second']:", kwargs['second'])


print_params1("a","b","c", first="a", second="b")       

#Output:
# b
# c
# a
# b