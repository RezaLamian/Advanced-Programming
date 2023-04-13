def function(dictionary1 , dictionary2):
    a = dict()
    for key1 , value1 in dictionary1.items():
        for key2 , value2 in dictionary2.items():
            if key1 == key2:
                a[key1] = [value1 , value2]
            else:
                a[key1] = [value1]
    return a

#example
a = {'key1':7 , 'key2':8 , 'key3':9}
b = {'key2':3 , 'key3':1}
print(function(a , b))

        