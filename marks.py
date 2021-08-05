lis = [{ "name" : "Nandini", "age" : 20},
{ "name" : "Manjeet", "age" : 45 },
{ "name" : "Nikhil" , "age" : 19 }]
 
# using sorted and lambda to print list sorted
# by age
print ("The list printed sorting by age: ")
print (sorted(lis, key = lambda i: i['age'],reverse=True))
 
print("\r")

print(list(filter(lambda person: person['name'] == 'Nandgini', lis)))