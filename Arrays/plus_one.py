def plusone(nums):
    num = nums[::-1]
    for i in range(len(num)):
        if num[i] == 9:
            num[i]=0
        else:
            num[i]+=1
            break
    else:
        num.append(1)
    return num[::-1]


print(plusone([1, 2, 3]))
print(plusone([1, 9, 9]))
print(plusone([9, 9, 9]))