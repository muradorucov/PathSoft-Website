"""Bərabər bölənlər
m natural ədədi n ədədinin o zaman bərabər böləni adlanır ki, n-nin m-ə bölünməsindən alınan tam və qalıq bərabər olsun. Verilmiş n natural ədədinə görə onun bərabər bölənlərinin sayını tapın.

Giriş verilənləri

Müsbət n tam ədədi (1 ≤ n ≤ 106).

Çıxış verilənləri

Tələb olunan say."""

m= int(input())
n=1
i=0
while (n<m):
    if (m//n == m%n):
        i+=1
    n+=1
print(i)