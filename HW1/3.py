def function(list1 , list2):
    a = dict()
    Min = len(list1)
    if len(list1) > len(list2):
        Min = len(list2)
    for i in range(Min):
        a[list1[i]] = list2[i]
    return a

#example
a = ['key1' , 'key2' , 'key3']
b = [4 , 5 , 9 , 3]
print(function(a , b))

        

