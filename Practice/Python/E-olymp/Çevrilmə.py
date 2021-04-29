"""Çevrilmə
Hər hansı bir natural n ədədini götürək. Onu növbəti şəkildə dəyişdirəcəyik: Əgər ədəd cütdürsə, onda onu 2-ə bölək, əgər təkdirsə ona 1 əlavə edək. Bir neçə belə dəyişmədən sonra həmişə 1 alacağıq. Məsələn, 11 ədədindən 12 ədədi alınır, sonra 6, 3, 4, 2 və sonda 1. Beləliklə, 11-dən 1 almaq üçün 6 dəyişiklik etmək lazımdır.

Verilmiş natural ədədə görə 1 alınana qədər onun dəyişmələrinin sayını tapın.

Giriş verilənləri
Natural n (1 ≤ n ≤ 109) ədədi.

Çıxış verilənləri
1 alınana qədər n ədədinin dəyişmələrinin sayını çap edin.
"""

n=int(input())
i=0
while (n>1):
    if n%2==0:
        i+=1
        n=n/2
    elif n%2==1:
       
        n=n+1
        i+=1
print(i)