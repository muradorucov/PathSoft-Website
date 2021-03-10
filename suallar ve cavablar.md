## 1.Translyator ve assembler nədir? Compiler və interpreter ilə aralarındakı fərqlər nələrdir?
 - Bizim(insanın) başa düşdüyümüz kodları maşın dilinə çevrimək üçün translyator və kompilyator proqramlarından istifadə olunur.
 - Assembler aşağı səviyyəli dildir, o əmrləri maşın kodları şəklində icra edir.
 - Compiler və interpreter ilə aralarındakı fərqlər əsasən bunlardır:
```
    -  Compiler əmrəlri sətirbəsətir icra edir.
    -  Kodu təhlil etmək üçün daha az vaxt gedir. İcra prosesi isə yavaşdır.
    -  Yaddaşı daha səmərəli istifadə edir.
    -  Nümunə olaraq: python və javascript proqramlaşdırma dillərini göstərə bilərik.
    -  interpreter proqram kodlarını hamısını birgə icra edir.
    -  Kodu təhlil etmək üçün daha çox vaxt gedir. İcra prosesi isə sürətlidir.
    -  Yaddaşı daha çox sərf edir.
    -  Nümunə olaraq: Java və C++ proqramlaşdırma dillərini göstərə bilərik.
```
## 2.Rəqəm və ədədlərin maşın dilinə tərcümə olunma prosesini bilirik. Bəs hərflər və simvollar necə tərcümə olunur?
 - Hərflər ve simvolları binary code-a tərcümə eləmək üçün UNİCODE sistemindən istifadə edilir. UNİCODE sistemində hərf və simvollar 16-lıq say sistemində 1 və 0 larla kodlaşdırılır. ASCİİ sistemində 256 simvol kodlaşdırıla bilirdik, amma, UNİCODE sisitemində 65536 simvol kodlaşdıra bilərik.
## 3.Günümüzdə istifadə olunan Js,PHP,Python və C# dillərində ortaq istifadə olunan data növləri hansılardır və qısaca izahatlarını yazın.
 - 