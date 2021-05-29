import datetime

name = input("Wpisz swoje imię: ")
byear = int(input("Podaj swój rok urodzenia: "))
bmont = int(input("Podaj swój miesiąc urodzenia: "))
bday = int(input("Podaj swój dzień urodzenia: "))

bdate = datetime.date(byear, bmont, bday)

bday100 = bdate + datetime.timedelta(days=100 * 365.25)
bday100f = bday100.strftime("%d.%m.%Yr")

print("%s, swoje 100. urodziny będziesz obchodził " % name + bday100f + ".")
