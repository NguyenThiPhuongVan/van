# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 09:51:02 2024

@author: PhuongVan
"""

a=int(input("nhap so a: "))
b=int(input("nhap so b: "))
s=((a**(1/2)-b**(1/2))/(a**(1/4)-b**(1/4))) - ((a**(1/2)+(a*b)**(1/4))/(a**(1/4)+b**(1/4)))

print("Ket qua la: ",s)