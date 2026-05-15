def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]
#Su dung ham vaf in ket qua
input_string = input("Mowi nhap chuoi can dao nguoc: ")
print("Chuoi dao nguoc la: ", dao_nguoc_chuoi(input_string))
