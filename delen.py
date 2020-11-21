#delen
import random
from integerCheck import integerCheck
from cijferBerekenen import cijferBerekenen
from goedeReactie import goedeReactie
#importeerd benodigde waarden

#functie delen
def delen():
  aantalGoed = 0
  aantalFout = 0
  for i in range(0,10):
    #herhaald 10x
    goedeWaarde = "false"
    while goedeWaarde == "false":
      #verwijst naar functie integercheck
      delen1 = (random.randint(1,101))
      delen2 = (random.randint(1,11))
      #kiest 2 random waarden om te delen
#Er wordt gecontroleerd door de computer of het antwoord een positief heel getal is.
      goedeWaarde = integerCheck(delen1, delen2)
    antwoordDelen = input("Wat is " + str(delen1) + "/" + str(delen2) + "?\n")
#Het goede antwoord wordt berekend door de computer
    echtAntwoordDelen = str(int(delen1 / delen2))
    #Het goede antwoord op de vraag
    if antwoordDelen == echtAntwoordDelen:
      #kijkt of het ingevulde antwoord goed is
      aantalGoed += 1
      #als het antwoord goed is wordt het aantal goede antwoorden met +1 verhoogd
      print("\033[1;32;48m" + goedeReactie() + "\033[0;38;48m\n")
    else:
      aantalFout += 1
      #als het antwoord fout is wordt het aantal foute antwoorden met +1 verhoogd
      print("\033[1;31;48m FOUT het antwoord was " + str(echtAntwoordDelen) + "\033[0;38;48m \n")
  print(cijferBerekenen(aantalGoed, aantalFout)) 
  #berekent cijfer  
