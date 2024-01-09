def max_numbers(arr,dic):
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
print("Test case1:",check(arr,lookup))

arr2=[5,3,8,54,88,16,33]   
lookup2={
    5:[1,2,5,8],
    20:[1,3,5,0],
    25:[88,16,33,14],
    1:[5,3,8,54,88,16,33],
    50:[12,3,53,16]  
}
print("Test case2:",check(arr2,lookup2))

arr3=[20,39,40,0]
lookup3={
    1:[10,10,12],
    2:[12,15,30,34],
    15:[34,53,66,33]
}
print("Test case3:",check(arr3,lookup3))
arr4=[0,0,0,0]
lookup4={
    1:[0,10,0],
    15:[12,3,0,0,0],
    100:[15]
}
print("Test case 4:",check(arr4,lookup4))

arr5=[100,14,53,64,34]
lookup5={
    100:[100,14,64,1533,22,33],
    29:[15,15],
    700:[]
}
print("Test case 5:",check(arr5,lookup5))