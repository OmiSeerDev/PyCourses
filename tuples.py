# Tuples are immutable

primals = (1,2,3,5,7,11,13,17,19,23,29)
print(primals)
print(type(primals)) #class 'tuple'

mix = (1,"Joe", False)
# Acceder a elementos
print(mix[1])
print(primals[-1])

#There is no CRUD, read only 
print(primals.index(13))

# But they may be mutated reasigning it into a list
my_list = list(primals)
my_list.pop()
print(my_list)