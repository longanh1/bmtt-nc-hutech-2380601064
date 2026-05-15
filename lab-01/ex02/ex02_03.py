#Nhap so tu nguoi dung
so = int(input("Nhap 1 so nguyen: "))
#Kiem tra so do co phai so chan hay khong
if so % 2 == 0:
  print(so, "La so chan")  
else:
    print(so, "Khong phai so chan")