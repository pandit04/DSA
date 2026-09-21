def equilaentdomino(domino):
    count ={}
    ans =0
    for a , b in domino :
        key = (min(a,b),max(a,b))
        if key in count:
            ans = count[key]+1
        count[key]=count.get(key,0)+1
    return ans
print(equilaentdomino([[1,2],[2,1],[3,4],[4,3]]))