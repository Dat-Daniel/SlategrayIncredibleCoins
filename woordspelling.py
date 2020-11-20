import random
from cijferBerekenen import cijferBerekenen
from goedeReactie import goedeReactie

#Functie Taal
def woordspelling():
  aantalGoed= 0
  aantalFout= 0

  #De lijsten met woorden
  lijstGoedeWoorden = ["elektrisch", "ironisch", "fantastisch", "revolutie", "situatie", "vakantie", "politici", "publiciteit", "waarheid", "artisticiteit", "diversiteit", "staren", "verjaardag", "reddeloos", "beschrijfbaar", "ontroostbaar", "lamheid", "humaniteit", "objectiviteit", "collega", "postcode", "afhouden", "verslaving", "gestart", "respect", "havo"]
  lijstFouteWoorden = ["electrisch", "iroisch", "fantasties", "revolutsie", "situatsie", "vacantie", "politicie", "publicitijt", "waarhijd", "artistisiteit", "diverseteit", "staaren", "verjardag", "reddebaar", "beschrijfloos", "ontroostloos", "lamteit", "humaniheid", "objectiviheid", "colega", "postccode", "afhauden", "verslafing", "gestard", "respeckt", "haafo"]
  
  nummer = 25
  
  for i in range(0,10):
    keuzeTaal = (random.randint(0,1))
    #keuze tussen de twee lijsten
    lijstIndex = (random.randint(0,nummer))
    nummer -= 1
    #als keuzetaal == 0 wordt de lijst goede woorden gekozen
    if keuzeTaal == 0:
      print(lijstGoedeWoorden[lijstIndex])
      goedOfFout = input("Is dit woord goed of fout?\n")
      if goedOfFout == "goed" or goedOfFout == "Goed":
      #Als het antwoord gelijk is aan 'goed' of 'Goed' is het antwoord goed
        aantalGoed += 1
        print("\033[1;32;48m" + goedeReactie() + "\033[0;38;48m\n")
        lijstGoedeWoorden.pop(lijstIndex)
        lijstFouteWoorden.pop(lijstIndex)
        #haalt het woord uit beide lijsten 
      else:   
        aantalFout += 1
        print("\033[1;31;48m FOUT het antwoord was goed gespeld\033[0;38;48m\n")
        lijstGoedeWoorden.pop(lijstIndex)
        lijstFouteWoorden.pop(lijstIndex)
        #haalt het woord uit beide lijsten 
        
    elif keuzeTaal == 1:
    #als keuzetaal == 1 wordt de lijst foute woorden gekozen
      print(lijstFouteWoorden[lijstIndex])  
      goedOfFout = input("Is dit woord goed of fout?\n")
      if goedOfFout == "fout" or goedOfFout == "Fout":
      #Als het antwoord gelijk is aan 'fout' of 'Fout' is het antwoord goed
        aantalGoed += 1
        print("\033[1;32;48m" + goedeReactie() + "\033[0;38;48m\n")
        lijstGoedeWoorden.pop(lijstIndex)
        lijstFouteWoorden.pop(lijstIndex)
      #haalt het woord uit beide lijsten 
      else:
        aantalFout += 1
        print("\033[1;31;48m FOUT je antwoord was fout\033[0;38;48m\n")
        print("Het goede antwoord is " "\033[1;32;48m" + lijstGoedeWoorden[lijstIndex] + "\033[0;38;48m\n")
        lijstGoedeWoorden.pop(lijstIndex)
        lijstFouteWoorden.pop(lijstIndex)
        #haalt het woord uit beide lijsten 
  print(cijferBerekenen(aantalGoed, aantalFout))
