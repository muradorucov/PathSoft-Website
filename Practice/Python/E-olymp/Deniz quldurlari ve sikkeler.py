"""
Dəniz quldurları və sikkələr
n dəniz qulduruna m qızıl sikkədən ibarət xəzinəni öz aralarında ədalətli şəkildə bölmək müyəssər oldu – hər kəs öz quldur ranqına (dərəcəsinə) və stajına uyğun ona çatacaq payı aldı. Ən kiçik quldur a sikkə, hər sonrakı quldur özündən əvvəlki yoldaşından bir sikkə artıq götürdü. Axırda kapitan idi, ona planlaşdırıldığından iki dəfə artıq sikkə çatdı və aydındır ki, ondan sonra sikkə qalmadı.

Əgər a və m məlumdursa, kapitanla birlikdə neçə quldur var idi. Komandasız kapitan adi quldurdur, onda n > 1.

Giriş verilənləri
İki natural a və m (1 ≤ a ≤ 100, m < 15150) ədədləri. Bütün giriş verilənləri düzgündür.

Çıxış verilənləri
Quldurların n sayı.
"""

a,m=list(map(int,input().split()))
i=1
while ((m-a)/2>=a):
    i+=1
    m=m-a
    a+=1
print(i)
