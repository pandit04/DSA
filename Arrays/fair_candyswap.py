#Alice: [1, 2, 5]
#Bob: [2, 4]

num1 = [1, 2, 5]
num2 = [2, 4]

a=sum(num1)
b=sum(num2)
result= int((a-b)//2)

bob_set = set(num2) 

for x in num1:
   target_bob_bag = x - result
   if target_bob_bag in bob_set:
    print([x,target_bob_bag])
    break