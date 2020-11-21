#functies
import random
from cijferBerekenen import cijferBerekenen
from goedeReactie import goedeReactie

#optellen
def optellen():
  aantalGoed = 0
  aantalFout = 0
  for i in range(1,11):
    optellen1 = (random.randint(0,101))
    optellen2 = (random.randint(0,101))
    antwoordOptellen = input("Wat is " + str(optellen1) + " + " + str(optellen2) + "?\n")
    echtAntwoordOptellen = str(optellen1 + optellen2)
    if antwoordOptellen == echtAntwoordOptellen:
      aantalGoed += 1
      print("\033[1;32;48m" + goedeReactie() + "\033[0;38;48m\n")
    else:
     aantalFout += 1
     print("\033[1;31;48m FOUT het antwoord was " + str(echtAntwoordOptellen) + "\033[0;38;48m\n")
  print(cijferBerekenen(aantalGoed, aantalFout))