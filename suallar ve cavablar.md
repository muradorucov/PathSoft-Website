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
 - Ortaq Data types:
```
    -  String - mətn tipli dəyişən
    -  Number:
            - int(integer) - tama ədələrdən ibarət olan dəyişən tipi 
            - float - onluq ədədlərdən ibarət dəyişən tipi
    -  Boolean -İki dəyərdən ibarət olan dəyişən tipi(true and false)
``` 
## 4.Type Conversion ya da Type Casting nədir? Hansı hallarda ehtiyac duyulur.
 - Type Conversion ya da Type Casting:
```
   - Dəyişəni yeni bir dəyişənə və ya başqa bir məlumat növünə çevirə bmək deməkdir. Bunu iki cür etmək olar javascript    funksiyalarından istifadə etməklə və ya avtomatik javascriptin özü tərəfindən. Məsələn, bele bir proqram yazaq: 
        a=5//number
        b=76//number
        c=a+b=81//number (bu proqramdakı a və b dəyişənləri number tipində olduğuna görə c dəyişənin tipidə number olacaq), lakin bu proqramda ya,
        a=5//number
        b="76" //string
        c=a+b="576"//string (bu proqramda isə a dəyişənin tipi number, b dəyişənin tipi isə stringdir(mətn tipli) , c dəyişənin tipi string olacaqdır, burada ki çevrilmə avtomatik javascript tərəfindən aparılır) 
        
        və ya başqa bir proqram yazaq:
        var b=6
        b = Boolean(b);
        document.write(b + " : " + typeof b);
        bu proqramda ilk olaraq b-dəyişənin tipi number idi, sonra biz onun tipini boolean(true or false) olaraq dəyişdirdik.
   - bu çevirmələrin tipinə Conversion və ya Casting deyilir. 
```
## 5.Operator precedence nədir və əhəmiyyətini izah edin.
 - Operator precedence operatorların bir-birindən üstün olub-olmadığını müəyyən edir. Bu səbəbdən operatorların üstünlük sırası aşağıdakı kimi olur:
```
    1.İlk öncə yazdığımız proqrmada mötərizə varsa onun içərisi hesablanır.
    2.Qüvvət üstlü ədəd varsa onu hesablayır.
    3.Vurma, bölmə varsa onlar həll edilir.
    4.Sonda toplama, çıxma həll edilir.
```
   