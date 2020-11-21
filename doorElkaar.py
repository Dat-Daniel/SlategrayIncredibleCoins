import random
from cijferBerekenen import cijferBerekenen
from integerCheck import integerCheck
from positiefCheck import positiefCheck
from goedeReactie import goedeReactie

def doorElkaar():
  aantalGoed = 0
  aantalFout = 0
  for i in range (0,10):
    randomkeuze = (random.randint(0,3))
    #vermenigvuldigen
    if randomkeuze == 0:
      vermenigvuldigen1 = (random.randint(0,11))
      vermenigvuldigen2 = (random.randint(0,11))
      antwoordVermenigvuldigen = input("Wat is " + str(vermenigvuldigen1) + "x" + str(vermenigvuldigen2) + "?\n")
      echtAntwoordVermenigvuldigen = str(vermenigvuldigen1 * vermenigvuldigen2)
      if (antwoordVermenigvuldigen) == echtAntwoordVermenigvuldigen:
        aantalGoed += 1
        print("\033[1;32;48m" + goedeReactie() + "\033[0;38;48m\n")
      else:
        aantalFout += 1
        print("\033[1;31;48m FOUT het antwoord was " + str(echtAntwoordVermenigvuldigen) + "\033[0;38;48m\n")
    #delen
    elif randomkeuze == 1:
      goedeWaarde = "false"
      while goedeWaarde == "false":
        delen1 = (random.randint(1,101))
        delen2 = (random.randint(1,11))
        goedeWaarde = integerCheck(delen1, delen2)
      antwoordDelen = input("Wat is " + str(delen1) + "/" + str(delen2) + "?\n")
      echtAntwoordDelen = str(int(delen1 / delen2))
      if antwoordDelen == echtAntwoordDelen:
        aantalGoed += 1
        print("\033[1;32;48m" + goedeReactie() + "\033[0;38;48m\n")
      else:
        aantalFout += 1
        print("\033[1;31;48m FOUT het antwoord was " + str(echtAntwoordDelen) + "\033[0;38;48m\n")
    #optellen
    elif randomkeuze == 2:
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
    #aftrekken
    elif randomkeuze == 3: 
      goedeWaarde = "false"
      while goedeWaarde == "false":
        aftrekken1 = (random.randint(0,101))
        aftrekken2 = (random.randint(0,101))
        goedeWaarde = positiefCheck(aftrekken1, aftrekken2)
      antwoordAftrekken = input("Wat is " + str(aftrekken1) + "-" + str(aftrekken2) + "?\n")
      echtAntwoordAftrekken = str(aftrekken1 - aftrekken2)
      if antwoordAftrekken == echtAntwoordAftrekken:
        aantalGoed += 1
        print("\033[1;32;48m" + goedeReactie() + "\033[0;38;48m\n")
      else:
        aantalFout += 1
        print("\033[1;31;48m FOUT het antwoord was " + str(echtAntwoordAftrekken) + "\033[0;38;48m\n")
  print(cijferBerekenen(aantalGoed, aantalFout))    