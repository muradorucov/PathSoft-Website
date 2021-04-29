"""Üçrəqəmli ədədin rəqəmlərini dəyişdirmək
Verilmiş üçrəqəmli ədəddə birinci və sonuncu rəqəmlərin yerini dəyişdirin

Giriş verilənləri
Yeganə n (100 ≤ n ≤ 999) natural ədədi.

Çıxış verilənləri
Yerdəyişmədən sonra alınan ədədi verməli."""
n=int(input())
print(n%10,(n//10)%10, n//100, sep="")