import sys
numbers = [5,1, 3, 6, 2, 9, 10, 4, 8, 7]
animals = ['Newt', 'Owl', 'Horse', 'Tiger', 'Yak', 'Panda']
letters = ['A', 'B', 'C', 'E', 'F', 'G', 'H', 'I', 'J']
fruits = ['orange', 'banana', 'tomato', 'strawberry'] 
# number one 
numbers.sort()
print(numbers)

# number two
letters.insert(3,"d")
print(letters)

# number three 
i = len(animals) - 1
while i > -1:
    print(animals[i])
    i-=1
# number four 
#print(animals[sys.maxsize])
fruits.remove("tomato")
print(fruits)

