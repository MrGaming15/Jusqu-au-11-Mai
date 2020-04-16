import ast
mois = mois = ast.literal_eval(open("mois.txt",'r').read())

def date(temps):
    print("Nous sommes le {} {} {} et il est {}h{} et {}s".format(temps.tm_mday,mois[temps.tm_mon],temps.tm_year,temps.tm_hour+2,temps.tm_min,temps.tm_sec))

def timejhms(temps):
  global finj
  #J'utilise une condition pour svoir quelle façon je vais de voir utiliser pour savoir combien de jours il manque et savoir si le 11 mai est passé
  if temps.tm_mon == 4 and temps.tm_year == 2020:
    finj = 30-temps.tm_mday+11-1
  elif temps.tm_mon == 5 and temps.tm_year == 2020:
    finj = temps.tm_mday+11-1
  else:
    print("Le confinement est théoriquement déjà fini !")
  print("\nLa fin du confinement est donc dans : {} jour(s), {} heure(s), {} minute(s) et {} seconde(s)".format(finj,24-(temps.tm_hour+2)-1,60-temps.tm_min-1,60-temps.tm_sec))

def times(temps):
  fin = 60-temps.tm_sec+60-temps.tm_min * 60+24-(temps.tm_hour+2) * 60**2+finj * 60**2*24
  print("\nCe qui représente {} seconde(s)".format(fin))