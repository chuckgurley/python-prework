my_list = []
print(type(my_list))
my_list = list()
print(type(my_list))
#index     0  1  2  3      4
numbers = [2, 6, 10, 12.5, 0] #index this is a comment
print(numbers)
print(type(numbers))

print(numbers[1])
print(type(numbers[1]))
print(numbers[1]*2.5)
print(type(numbers[1]*2.50))

# print out 12.5
print(numbers[3])
print(type(numbers[3]))

foods = ["pizza", "tacos", "dim sum", "sushi"]
print(foods[1])
print(type(foods[1]))
print(foods[1].upper())

x = 12
y = 15.5
z = "z"

random_list = [x, y, z]
print(random_list[0])
print(type(random_list[0]))

print(random_list[1])
print(type(random_list[1]))

print(random_list[2])
print(type(random_list[2]))

my_fav_num = random_list[0]
print(my_fav_num)

foods = ["pizza", "tacos", "dim sum", "sushi"]
foods.append("cheese burger")
print(foods)

foods = ["pizza", "tacos", "dim sum", "sushi"]
foods.insert(0, "pho")
print(foods)

foods = ["pizza", "tacos", "dim sum", "sushi"]
foods.insert(0, "pho")

print(foods)


foods = ["pizza", "tacos", "dim sum", "sushi"]
foods.append('pizza')
print(foods)
foods.remove("pizza")
print(foods)


foods = ["pizza", "tacos", "dim sum", "sushi"]
print(foods)
del foods[1]
print(foods)

foods = ["pizza", "tacos", "dim sum", "sushi"]
print (foods.pop())
print(foods)


