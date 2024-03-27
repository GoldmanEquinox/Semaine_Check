
import datetime

def fonction():
    day = int(input("Jour (0-31) : "))
    month = int(input("Mois (0-12) : "))
    year = int(input("Année : "))
    try:
        date = datetime.date(year, month, day)
        #print("Date is valid.")
    except ValueError:
        print("Date is not valid.")
        raise SystemExit

    date = datetime.date(year, month, day)
    ajd = datetime.date.today()
    delta = date - ajd
    semaine = datetime.timedelta(days=7)
    if delta.days >= semaine.days:
        print("C'est bon il y a au moins 1 semaine (nombre de jours exact : " + str(delta.days) + ")")
    elif delta.days < 0:
        print("C'est pas bon, c'est dans le passé")
    else :
        print("C'est pas bon, il reste moins d'une semaine (nombre de jours exact : " + str(delta.days) + ")")

fonction()
