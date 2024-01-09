def max_numbers(size_arr,arr,dic):
    max_count=0
    
    count={}
    for key,values in dic.items():
        
            count[key]=sum(1 for element in arr if element in values)
            
    result=[key for key,value in count.items() if value==max(count.values())]
    return result

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
print("Test case1:",max_numbers(len(arr),arr,lookup))

arr2=[5,3,8,54,88,16,33]   
lookup2={
    5:[1,2,5,8],
    20:[1,3,5,0],
    25:[88,16,33,14],
    1:[5,3,8,54,88,16,33],
    50:[12,3,53,16]  
}
print("Test case2:",max_numbers(len(arr2),arr2,lookup2))

arr3=[20,39,40,0]
lookup3={
    1:[10,10,12],
    2:[12,15,30,34],
    15:[34,53,66,33]
}
print("Test case3:",max_numbers(len(arr3),arr3,lookup3))
arr4=[0,0,0,0]
lookup4={
    1:[0,10,0],
    15:[12,3,0,0],
    100:[15]
}
print("Test case 4:",max_numbers(len(arr4),arr4,lookup4))

arr5=[100,14,53,64,34]
lookup5={
    100:[100,14,64,1533,22,33],
    29:[15,15],
    700:[]
}
print("Test case 5:",max_numbers(len(arr5),arr5,lookup5))