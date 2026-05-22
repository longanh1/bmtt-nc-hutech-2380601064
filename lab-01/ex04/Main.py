from QuanLySinhVien import QuanLySinhVien
qlsv = QuanLySinhVien()
while (1 == 1):
    print("\n++++++++++++++++++MENU QUAN LY SINH VIEN++++++++++++++++++++")
    print("1. Them sinh vien")
    print("2. Cap nhat thong tin sinh vien theo ID")
    print("3. Xoa sinh vien theo ID")
    print("4. Tim kiem sinh vien theo ten")
    print("5. Sap xep sinh vien theo diem TB")
    print("6. Xap xep sinh vien theo ten chuyen nganh")
    print("7. Hien thi danh sach sinh vien")
    print("0. Thoat chuong trinh")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    key = int(input("Nhap lua chon cua ban: "))
    if (key == 1):
        print("\n1. Them sinh vien")
        qlsv.nhapSinhVien()
        print("Them sinh vien thanh cong!")
    elif (key == 2):
        if (qlsv.soluongSinhVien() > 0):
            print("\n2. Cap nhat thong tin sinh vien theo ID")
            ID = int(input("Nhap ID sinh vien can cap nhat: "))
            qlsv.updateSinhVien(ID)
        else:
            print("Danh sach sinh vien trong!")
    elif (key == 3):
        if (qlsv.soluongSinhVien() > 0):
            print("\n3. Xoa sinh vien theo ID")
            ID = int(input("Nhap ID sinh vien can xoa: "))
            if(qlsv.deleteByID(ID)):
                print("Sinh vien co ID = ", ID, " da duoc xoa!")
        else:
            print("Danh sach sinh vien trong!")
    elif (key == 4):
        if (qlsv.soluongSinhVien() > 0):
            print("\n4. Tim kiem sinh vien theo ten")
            name = input("Nhap ten sinh vien can tim kiem: ")
            seachResult = qlsv.findByName(name)
            qlsv.showSinhVien(seachResult)
        else:
            print("Danh sach sinh vien trong!")
    elif (key == 5):
        if (qlsv.soluongSinhVien() > 0):
            print("\n5. Sap xep sinh vien theo diem TB GPA")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.listSinhVien)
        else:
            print("Danh sach sinh vien trong!")
    elif (key == 6):
        if (qlsv.soluongSinhVien() > 0):
            print("\n6. Xap xep sinh vien theo ten chuyen nganh")
            qlsv.sortByMajor()
            qlsv.showSinhVien(qlsv.listSinhVien)
        else:
            print("Danh sach sinh vien trong!")
    elif (key == 7):
        if (qlsv.soluongSinhVien() > 0):
            print("\n7. Hien thi danh sach sinh vien")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("Danh sach sinh vien trong!")
    elif (key == 0):
        print("Ban da chon thoat chuong trinh!")
        break
    else:        
        print("\nKhong co chuc nang nay, vui long chon lai!")
        print("\nHay chon chuc nang khac trong menu!")