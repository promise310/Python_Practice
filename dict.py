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

# 각 채널은 Dictionary로 구성하고 여러 채널의 목록은 List로 구성해봅시다. 
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

# 각 채널에 접근할 때에는 index로 접근합니다. 
print(students[1])

# 채널 내부의 정보에 접근할 때에는 key로 접근합니다. 
print(students[1]['name'])