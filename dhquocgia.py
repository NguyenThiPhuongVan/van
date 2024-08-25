# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 10:03:05 2024

@author: PhuongVan
"""

a= "Đại học Quốc gia, Khu phố 6, P Linh Trung, Q Thủ Đức, Tp Hồ Chí Minh"
s= a.split(",")
print("bang1")
for b in s:
    print(b)
print()
print("bang2")
s2= a.replace("P.","").replace("Q.","").replace("Tp.","")
s3= s2.split(",")
for c in s3:
    print(c)