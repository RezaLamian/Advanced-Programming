def function(dictionary):
    a = tuple()
    b = set()
    for key , value in dictionary.items():
        a = (key , value)
        b.add(a)
    return b

#example
a = {'key1':4 , 'key2':9 , 'key3':0}
print(function(a))
