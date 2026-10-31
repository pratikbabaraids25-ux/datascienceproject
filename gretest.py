
numbers = [10, 45, 23]
greatest = max(numbers)
print("The greatest number is:", greatest)

# 2. Using If-Else Logic
a, b, c = 10, 45, 23
if a >= b and a >= c:
    greatest = a
elif b >= a and b >= c:
    greatest = b
else:
    greatest = c
print("The greatest number is:", greatest)
