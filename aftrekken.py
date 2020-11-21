#delen
import random
from positiefCheck import positiefCheck
from cijferBerekenen import cijferBerekenen
from goedeReactie import goedeReactie

#functie delen
def aftrekken():
  aantalGoed = 0
  aantalFout = 0
#De functie wordt 10x herhaald
  for i in range(0,10):
    goedeWaarde = "false"
    while goedeWaarde == "false":
#2 random waarden worden gegenereerd door de computer
      aftrekken1 = (random.randint(0,101))
      aftrekken2 = (random.randint(0,101))
#Er wordt in de integerCheck gecheckt of het een positief heel getal is
      goedeWaarde = positiefCheck(aftrekken1, aftrekken2)
    antwoordAftrekken = input("Wat is " + str(aftrekken1) + "-" + str(aftrekken2) + "?" + "\n")
#Het goede antwoord wordt berekend door de computer
    echtAntwoordAftrekken = str(aftrekken1 - aftrekken2)
    if antwoordAftrekken == echtAntwoordAftrekken:
      aantalGoed += 1
      #als het antwoord goed is wordt het aantal goede antwoorden met +1 verhoogd
      print("\033[1;32;48m" + goedeReactie() + "\033[0;38;48m\n")
    else:
      aantalFout += 1
    #als het antwoord fout is wordt het aantal foute antwoorden met +1 verhoogd
      print("\033[1;31;48m FOUT het antwoord was " + str(echtAntwoordAftrekken) + "\033[0;38;48m\n")
#Het cijfer wordt weergegeven aan de leerling
  print(cijferBerekenen(aantalGoed, aantalFout))    
