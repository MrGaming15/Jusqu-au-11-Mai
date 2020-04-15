#encoding:utf-8
import time
mois = {4 : "Avril",5 :	"Mai"}
temps = time.localtime()
print("Nous sommes le "+str(temps.tm_mday)+" "+mois[temps.tm_mon]+" "+str(temps.tm_year)+" et il est "+str(temps.tm_hour)+"h"+str(temps.tm_min)+" et "+str(temps.tm_sec)+"s")
if temps.tm_mon == 4 and temps.tm_year == 2020:
	finj = 30-temps.tm_mday+11-1
elif temps.tm_mon == 5 and temps.tm_year == 2020:
	finj = temps.tm_mday+11-1
else:
	print("Le confinement est théoriquement déjà fini !")
	
print("\nLa fin du confinement est donc dans : {} jour(s), {} heure(s), {} minute(s) et {} seconde(s)".format(finj,24-temps.tm_hour-1,60-temps.tm_min-1,60-temps.tm_sec))
fins= 60-temps.tm_sec
finm= 60-temps.tm_min * 60
finh= 24-temps.tm_hour * 60**2
finj = finj * 60**2*24
fin = fins+finm+finh+finj
print("\nCe qui représente "+str(fin)+" secondes")


