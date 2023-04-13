def function(dictionary , number):
    a = list()
    for key , value in dictionary.items():
        if number == value:
            a.append(key)
    return a

#example
a = {'key1':3 , 'key2':5 , 'key3':7 , 'key4':5 }
print(function(a , 5))
