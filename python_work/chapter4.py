foods = ["pizza", "tacos", "dim sum", "sushi"]
 
print(foods[1])
 
#for PLACEHOLDER in THE LIST WE WANT TO LOOK AT:
# put i 4 spaces     
    #this is a code bloclk
    #this  code block
    #will run for every item in the list 
for food in foods:
    print(f"I like {food} because they a yummy")
    if food == "dim sum":
        break

for index in range(len(foods)):
    print(index)
    print(foods[index])

print(list(enumerate(foods)))
for index, food in enumerate(foods):
    print(f"My No {index + 1} food is {food.title()}")

# loop over index
print(list(range(4)))
print(len(foods))

