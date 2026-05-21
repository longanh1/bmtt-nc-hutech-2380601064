#Tao 1 danh sach rong de luu ket qua
j = []
# Duyet qua tat ca cac so trong doan tu 2000 den 3200, kiem tra xem so i coschia het cho 7 vaf khong phai la boi cuar so 5 khong
for i in range(2000, 3200):
    if(i % 7 ==0) and (i %5 == 0):
        j.append(str(i))
print(','.join(j))