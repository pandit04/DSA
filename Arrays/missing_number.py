def missingnumber(nums):
    n = len(nums)
    Expected =sum(range(n+1))
    actual = sum(nums)
    return Expected - actual

print(missingnumber([3,0,1]))
print(missingnumber([0,1]))
print(missingnumber([9,6,4,2,3,5,7,0,1]))