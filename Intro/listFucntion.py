subjects = ["C","C++", "java", "python", "Basic"]
print(len(subjects))
subjects.append("Toc")
subjects.insert(3,"ox")
print(subjects)
subjects.remove("Basic")
print(subjects)
subjects.sort()
print(subjects)

print("Number")
numbers = [12,34,13,54,2,6,756,39]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers.pop()
print(numbers)
numbers.clear()
print(numbers)
numbers = [12,34,13,54,2,2,6,75,2,6,39]
# num = numbers.copy()
num = subjects.copy()
sub = numbers.copy()
print(num)
print(sub)
position = numbers.index(34)
count=numbers.count(2)
print(position)
print(count)


