x = int(input("Введите сумму выдачи от 1 до 100000: "))
while x > 100000 or x < 1:
    x = int(input("Вы ввели некорректную сумму, попробуйте ещё раз: "))
Summa = []
if x//100000 == 1:
    Summa.append("сто тысяч")
match x//10000:
    case 9:
        Summa.append("девяносто")
    case 8:
        Summa.append("восемьдесят")
    case 7:
        Summa.append("семьдесят")
    case 6:
        Summa.append("шестьдесят")
    case 5:
        Summa.append("пятьдесят")
    case 4:
        Summa.append("сорок")
    case 3:
        Summa.append("тридцать")
    case 2:
        Summa.append("двадцать")
    case 1:
        match x//1000:
            case 19:
                Summa.append("девятнадцать")
            case 18:
                Summa.append("восемнадцать")
            case 17:
                Summa.append("семнадцать")
            case 16:
                Summa.append("шестнадцать")
            case 15:
                Summa.append("пятнадцать")
            case 14:
                Summa.append("четырнадцать")
            case 13:
                Summa.append("тринадцать")
            case 12:
                Summa.append("двенадцать")
            case 11:
                Summa.append("одиннадцать")
            case 10:
                Summa.append("десять")
if x//1000 > 9 and x//1000 < 20:
    Summa.append("тысяч")
else:
    match (x//1000)%10:
        case 9:
            Summa.append("девять тысяч")
        case 8:
            Summa.append("восемь тысяч")
        case 7:
            Summa.append("семь тысяч")
        case 6:
            Summa.append("шесть тысяч")
        case 5:
            Summa.append("пять тысяч")
        case 4:
            Summa.append("четыре тысячи")
        case 3:
            Summa.append("три тысячи")
        case 2:
            Summa.append("две тысячи")
        case 1:
            Summa.append("одна тысяча")
match (x//100)%10:
    case 9:
        Summa.append("девятьсот")
    case 8:
        Summa.append("восемьсот")
    case 7:
        Summa.append("семьсот")
    case 6:
        Summa.append("шестьсот")
    case 5:
        Summa.append("пятьсот")
    case 4:
        Summa.append("четыреста")
    case 3:
        Summa.append("триста")
    case 2:
        Summa.append("двести")
    case 1:
        Summa.append("сто")
match (x//10)%10:
    case 9:
        Summa.append("девяносто")
    case 8:
        Summa.append("восемьдесят")
    case 7:
        Summa.append("семьдесят")
    case 6:
        Summa.append("шестьдесят")
    case 5:
        Summa.append("пятьдесят")
    case 4:
        Summa.append("сорок")
    case 3:
        Summa.append("тридцать")
    case 2:
        Summa.append("двадцать")
    case 1:
        match x%100:
            case 19:
                Summa.append("девятнадцать")
            case 18:
                Summa.append("восемнадцать")
            case 17:
                Summa.append("семнадцать")
            case 16:
                Summa.append("шестнадцать")
            case 15:
                Summa.append("пятнадцать")
            case 14:
                Summa.append("четырнадцать")
            case 13:
                Summa.append("тринадцать")
            case 12:
                Summa.append("двенадцать")
            case 11:
                Summa.append("одиннадцать")
            case 10:
                Summa.append("десять")
if x%100 < 20 and x%100 > 9:
    Summa.append("рублей")
else:
    match x%10:
        case 9:
            Summa.append("девять рублей")
        case 8:
            Summa.append("восемь рублей")
        case 7:
            Summa.append("семь рублей")
        case 6:
            Summa.append("шесть рублей")
        case 5:
            Summa.append("пять рублей")
        case 4:
            Summa.append("четыре рубля")
        case 3:
            Summa.append("три рубля")
        case 2:
            Summa.append("два рубля")
        case 1:
            Summa.append("один рубль")
        case 0:
            Summa.append("рублей")
Summa[0] = Summa[0].capitalize()            #У первого элемента массива меняем первую букву на заглавную
print(*Summa)