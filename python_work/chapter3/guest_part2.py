guest = ['prince', 'elvis', 'tesla']
name = guest[0].title()
print(name + ", can you come to my BBQ?")
name = guest[1].title()
print(name + ", can you come to my BBQ?")
name = guest[2].title()
print(name + ", can you come to my BBQ?")
name = guest[0].title()
print("\nSorry, " + name + " can't make it to the BBQ.")
del(guest[0])
guest.insert(0, 'stonecold')
name = guest[0].title()
print(name + ", can you come to my BBQ?")
name = guest[1].title()
print(name + ", can you come to my BBQ?")
name = guest[2].title()
print(name + ", can you come to my BBQ?")

