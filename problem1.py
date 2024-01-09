def check(arr,dic):
    max_key=0
    max_count=0
    for key in dic:
        
        count=0
        for val in dic[key]:
            if val in arr:
                count+=1
        if count>max_count:
            max_count=count
            max_key=key
    return max_key

arr=[4,13,98,54,88,16,33]      
lookup={
    13:[65,89,98,33,65,878],
    24:[98,54,123,234,67],
    33:[43,76,9],
    41:[4,13,23,56,89,00,87,654,789,54],
    54:[46,32,54,66,87,88,943,16,89,33,6],
    88:[13,33],
    98:[88,76,77,55,32]
    
}
print(check(arr,lookup))