#functies
import random
from cijferBerekenen import cijferBerekenen
from goedeReactie import goedeReactie

#vermenigvuldigen functie
def vermenigvuldigen():
  aantalGoed = 0
  aantalFout = 0
#De functie die 10x herhaald word
  for i in range(1,11):
    vermenigvuldigen1 = (random.randint(0,11))
    vermenigvuldigen2 = (random.randint(0,11))
    antwoordVermenigvuldigen = input("Wat is " + str(vermenigvuldigen1) + "x" + str(vermenigvuldigen2) + "?\n")
#Het antwoord word berekend door de computer
    echtAntwoordVermenigvuldigen = vermenigvuldigen1 * vermenigvuldigen2
    if str(antwoordVermenigvuldigen) == str(echtAntwoordVermenigvuldigen):
      aantalGoed += 1
      print("\033[1;32;48m" + goedeReactie() + "\033[0;38;48m\n")
    else:
      aantalFout += 1
      print("\033[1;31;48m FOUT het antwoord was " + str(echtAntwoordVermenigvuldigen) + "\033[0;38;48m\n")
#Het cijfer wordt weergegeven  
  print(cijferBerekenen(aantalGoed, aantalFout))
