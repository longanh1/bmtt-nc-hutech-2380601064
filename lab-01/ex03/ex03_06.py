def xoaphantu(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False
    
my_dict = {'a': 1, 'b':2, 'c':3, 'd':4}
keytodelete = 'b'
result = xoaphantu(my_dict, keytodelete)
if result:
    print("Phan tu da duoc xoa tu dictionary:", my_dict)
else:
    print("Khong tim thay phan tu xoa trong dictionary")
    