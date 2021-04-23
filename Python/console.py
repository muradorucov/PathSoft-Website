


def print_meniu():
    print("""--Salam mini HR proqramına xoş gəlmisiniz--
    Zəhmət olmasa sizə uyğun əmri seçin:
    1.Yeni işçi əlavə etməkçün 1-i daxil edin.
    2.İstifadəçi məlumatlarına baxmaq üçün 2-ni daxil edin.
    3.Ümumi maaş cəmini göstərmək üçün 3-ü daxil edin.
    4.İşçi sayını göstərmək üçün 4-ü daxil edin.
    5.Ən köhnə işçini göstərmək üçün 5-i daxil edin.
    6.Ən yeni işçini göstərmək üçün 6-nı daxil edin.
    7.Əsas menyuya qayıtmaq üçün 0-ı daxil edin""")
while True:
    print_meniu()
    console = int(input())
    if console == 1:
        print("1.Yeni işçi əlavə et")
    elif console == 2:
        print("İstifadəçi məlumatları")
    elif console == 3:
        print("100897 Manat")
    elif console == 4:
        print("10")
    elif console== 5:
        print("Hesen")
    elif console == 6:
        print("Obama")
    elif console == 7:
        print(" ")
    else:
        print("Uğursuz əməliyyat!")
    