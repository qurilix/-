from colorama import *
init()
a=float(input(Fore.GREEN+"Введите свой рост: "))
b=float(input(Fore.GREEN+"Введите свой вес: "))
c = b /(a/100)**2
print(Fore.BLUE+"Ваш ИТМ: ", c)

if c <= 18.5:
    print(Fore.RED+"У вас недостаточный вес!")
elif c <= 24.9:
    print(Fore.RED+"У вас идеальный вес!")
elif c <= 29.9:
    print(Fore.RED+"У вас имееться лишний вес!")
else:
    print(Fore.RED+"Вы страдаете ожирением!")

input()