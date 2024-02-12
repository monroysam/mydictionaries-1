person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print()
#print(person)
print(person)

print()
# print out the name of the second child
print(person['children'][1])

print()
# print out the name of the cat
print(person['pets']['cat'])

print()
# use a loop to print out the names of each child
for child in person['children']:
    print(child)



print()
# use a loop to print out the pets in the following format:
# The type of pet is: dog and the name of the pet is: Fido
for pet in person['pets']:
    print(f'The type of pet is {pet} and the name of the pet is: {person["pets"][pet]}')
          
for i,j in person['pets'].items():
    print(f'The type of pet is {i} and the name of the pet is: {j}')