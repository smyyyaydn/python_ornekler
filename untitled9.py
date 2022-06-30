# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 12:25:59 2022

@author: smyyy
"""

litre=int(input("benzin: "))
hesap = litre*30.50
vergi = hesap*0.18
print("vergi:", vergi)
print("vergisiz benzinin fiyatı:", hesap)
print("toplam tutar:", hesap + vergi)
