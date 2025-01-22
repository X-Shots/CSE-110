
numbers = []
with open("nums-vvertical.txt") as nums:
    for x in nums:
        numbers.append(int(x))
print(sum(numbers))
max = -1000

for num in numbers:
    if num > max:
        max = num
print(max)


with open("nums-horizontal.txt") as nums:
    line = nums[0]
line.strip()
nums = line.split("|")
print(sum(nums))
max = -1000
for num in nums:
    if num > max:
        max = num
print(max)
