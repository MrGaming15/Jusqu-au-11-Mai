#encoding:utf-8
#RISQUE DE BUG SI CONSULTATION ENTRE 22h ET 2h CAR JE DOIS AJOUTER 2h POUR AVOIR L'HEURE FRANÇAISE
#Importation des modules
import time
from os import system
import command

w = False
while not w :
  system("clear") 
  #Le module "command" est un module où j'ai mis toute les fonctions que j'ai crées pour l'algorithme
  command.date(time.localtime())
  command.timejhms(time.localtime())
  command.times(time.localtime())
  



