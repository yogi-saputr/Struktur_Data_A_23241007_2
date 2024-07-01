# belajar tipe data 
# tipe data integer : bilangan bulat
bil_integer = 100
print(type(bil_integer))
print("tipe data dari bil_integer adalah : ", type(bil_integer))

#tipe data float : bilangan desimal/pecahan
bil_float = 100
print(type(bil_float))
print("tipe data dari bil_float adalah : ", type(bil_float))

# tiep data boolean : 0/1, true/false, ya/tidak
bil_bol = False
print(type(bil_bol))
print("tipe data dari bil_bol adalah : ", type(bil_bol))

# tipe data string : kumpulan karakter
bil_string = "300000"
print(type(bil_string))
print("tipe data dari bil_string adalah : ", type(bil_string))

# tipe data dari c
from ctypes import c_double
bil_double = c_double(300000000)
print(type(bil_double))