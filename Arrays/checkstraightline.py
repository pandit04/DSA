def checkstraightline(cordinates):
    x1,y1 = cordinates[0]
    x2,y2 = cordinates[1]
    
    for x , y in cordinates:
        if (y2-y1)*(x-x1) != (y-y1)*(x2-x1):
            return False
    return True

coordinates = [[2,1],[4,2],[6,4]]
print(checkstraightline(coordinates))