def function(dictionary):
    max_key = min_key = list(dictionary)[0]
    max_value = min_value = list(dictionary.values())[0]
    for key , value in dictionary.items():
        if max_value < value:
            max_value = value
            max_key = key
        if min_value > value:
            min_value = value
            min_key = key
    return max_key , min_key

#example
a = { 'key1':1 , 'key2':8 , 'key3':2 }
print('max & min =' , function(a))

        

