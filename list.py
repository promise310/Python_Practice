colors = ['red', 'orange', 'yellow', 'green']

print(colors[2])

print(colors[1:3])

len(colors)

colors.append('blue') # add item at the end
print(colors)

print('\n')
fruits = ['Strawberry', 'Orange']

vegetables = ['Tomato', 'Carrot'] # 이어붙이고자 하는 리스트를 전달받아 그 리스트 속의 아이템들을 전부 추가합니다. 
fruits.extend(vegetables)
print(fruits)

fruits[2] = 'Cherry' # 기존 리스트에 담겨있는 특정 아이템의 값을 변경합니다. 
print(fruits)

print('\n')
numbers = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]

numbers.sort() # 리스트를 오름차순으로 정렬합니다. 
print(numbers)

numbers.reverse() # 리스트를 내림차순으로 정렬합니다. 
print(numbers)

last_number = numbers.pop() # 리스트의 마지막 아이템을 제거할 수 있습니다. 주로 마지막 아이템을 꺼내어 활용하는 목적으로 사용합니다. 
print(last_number)

print(numbers)

print('\n')
numbers = [10, 9, 8, 7, 6, 5, 4, 3, 2]

numbers.insert(1,9) # 콤마를 기준으로 왼쪽은 인덱스 번호, 오른쪽은 그 위치에 넣을 데이터를 적습니다. 
print(numbers)

print(numbers.count(9)) # 해당 값이 리스트 내에 몇 개 있는지 세어줍니다. 

numbers.remove(9) # 리스트에서 특정 값을 지워줍니다. 
print(numbers)

print(numbers.index(3)) # 해당 값이 리스트에서 몇 번째 위치에 있는지 알려줍니다.