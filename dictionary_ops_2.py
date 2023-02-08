dict1 = {'ACB': 'Association Club', 'CNN' : 'China News', 'BBC': 'British', 'NFL': ' No Fish', 'SP500': ' Standard'}

#Acces elements
print(dict1['ACB'])
print(dict1['NFL'])
print(dict1['SP500'])
#Acces keys
print(dict1.keys())
#Access values
print(dict1.values())

#Add element
dict1['PEG'] = 'Perfect Eclipse'
print(dict1)

#Delete element
del dict1['NFL']
print(dict1)

#Delete element with pop
dict1.pop('SP500')
print(dict1)

#Delete last added element
dict1.popitem()
print(dict1)

#Sort dictionary alphabetically

#By keys
bykeys = sorted(list(dict1.keys()))
print(bykeys)

#BY values
byvalues = sorted(list(dict1.values()))
print(byvalues)

#Dictionary comprehension
a = {i : i**16 for i in (1,2,3,4,5,6,7,8,9,10)}
print(a)
print(type(a))

#List comprehension
b = [i**2 for i in (1,2,3,4,5,6,7,8,9,10)]
print(b)
print(type(b))
