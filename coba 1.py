kode_baju = input("Masukkan Kode Baju [AD/NVD] : ")
ukuran_baju = input("Masukkan Ukuran baju [XL/L/M/S] : ")

if kode_baju == "AD" or kode_baju == "ad" :
    merk = "ADIDAS"
    if ukuran_baju == "XL" or ukuran_baju == "xl":
        harga = 300000
    elif ukuran_baju == "L" or ukuran_baju == "l":
        harga = 250000
    elif ukuran_baju == "M" or ukuran_baju == "m":
        harga = 200000
    elif ukuran_baju == "S" or ukuran_baju == "s":
        harga = 150000
    else:
        harga = "Anda salah input ukuran"
elif kode_baju == "NVD" or kode_baju == "nvd":
    merk = "NEVADA"
    if ukuran_baju == "XL" or ukuran_baju == "xl":
        harga = 300000
    elif ukuran_baju == "L" or ukuran_baju == "l":
        harga = 280000
    elif ukuran_baju == "M" or ukuran_baju == "m":
        harga = 250000
    elif ukuran_baju == "S" or ukuran_baju == "s":
        harga = 210000
    else:
        harga = "Anda salah input ukuran"
else :
    merk = "Anda salah input kode merk"
    harga = 0

print("----------------------------")
print("Merk Baju : " +str(merk))
print("Ukuran : " +str(ukuran_baju))
print("Harga :",harga)
print("----------------------------")