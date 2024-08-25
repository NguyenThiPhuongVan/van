# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 08:07:48 2024

@author: PhuongVan 
"""

a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

s1 = a + b
s2 = a - b
s3 = a * b
s4 = a / b
s5 = a % b
s6 = a // b

print ("Tính tổng, hiệu, tích, thương, chia lấy dư, chia lấy nguyên của 2 số trên:",)

print ("Tổng =", s1)
print ("Hiệu =", s2)
print ("Tích =", s3)
print ("Thương =", round(s4,3))
print ("Chia lấy phần dư =", s5)
print ("Chia lấy phần nguyên =", s6)
