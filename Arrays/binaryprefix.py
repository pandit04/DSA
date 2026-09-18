def binaryprefixdivby5(nums):
    result=[]
    remainder = 0

    for bit in nums:
        remainder = (remainder * 2 + bit) % 5

        if remainder == 0:
            result.append(True)
        else:
            result.append(False)

    return result

print(binaryprefixdivby5([0,1,1,0,1,1,0,1,1]))