fruits = {
    'Red' : ['Strawberry', 'Cherry'],
    'Orange' : ['Orange', 'Tangerin']
}

print(fruits['Red'])

print(fruits.get('Yellow'))
print(fruits.get('Red'))

fruits['Green'] = ['Kiwi', 'Watermelon']
print(fruits)

del(fruits['Green'])
print(fruits)

Yellow = {'Yellow' : ['Banana', 'Lemon']}
fruits.update(Yellow)
print(fruits)