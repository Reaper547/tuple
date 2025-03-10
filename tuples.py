my_tuple=(1,2,3)
print(my_tuple)
my_tuple=(1,"Hello",3.4)
print(my_tuple)

my_tuple=('a','b','c','d','e','f')
print(my_tuple[0])
print(my_tuple[4])

n_tuple=("lion",[1,2,3],(4,5,6))
print(n_tuple[0][1])
print(n_tuple[1][2])
print(n_tuple[2][2])

print("Sliced:",my_tuple[1:2])

for letter in (my_tuple):
    print("Hello",letter)