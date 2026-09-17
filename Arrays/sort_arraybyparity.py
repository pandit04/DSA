# Input:  [3, 1, 2, 4]
# Output: [2, 4, 3, 1]

num = [3, 1, 2, 4]

start = 0
end = len(num) - 1

while start < end:

    if num[start] % 2 == 0:
        start += 1

    elif num[end] % 2 != 0:
        end -= 1

    else:
        num[start], num[end] = num[end], num[start]
        start += 1
        end -= 1

print(num)

