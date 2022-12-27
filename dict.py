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

print("\n")
# Dictionary
student = {
    'name' : 'Jin',
    'age' : 13
}

print(f'The student name is {student["name"]}.')
print(f'The student age is {student["age"]}.')

# List
channel_by_list = ['Jin', 13]

#   0 : name
#   1 : age

print(f'The student name is{channel_by_list[0]}.')
print(f'Student age is {channel_by_list[1]}.')

print("\n")
students = [
    {
        'name' : 'Jin',
        'age' : 13
    },
    {
        'name' : 'Jini',
        'age' : 4
    },
    {
        'name' : 'Tom',
        'age' : 43
    }
]

 
print(students[1])
print(students[1]['name'])