#functies
from vermenigvuldigen import vermenigvuldigen
from optellen import optellen
from delen import delen
from aftrekken import aftrekken
from doorElkaar import doorElkaar
from woordspelling import woordspelling

#funtie programmaKeuze
def programmaKeuze():
  #keuze tussen taal of rekenen
  keuze1 = input("Wat wil je gaan doen? Rekenen of taal?\n")
  while keuze1 != "alkdsnfklsadjfkldsajf" or keuze1 != "zkcxvlndkahdsiofenaklsd":
    if keuze1 == "rekenen" or keuze1 == "Rekenen":
      
      #keuze tussen delen, optellen, aftrekken, vermenigvuldigen, of alles door elkaar
      keuze2 = input("Wil je delen, optellen, aftrekken, vermenigvuldigen of alles door elkaar?\n")
      while keuze2 != "boe" or keuze2 != "hoi":
        if keuze2 == "delen" or keuze2 == "Delen" or keuze2 == "Ties is een simp":
          print("We starten met delen\n")
          return delen()
        elif keuze2 == "optellen" or keuze2 == "Optellen":
          print("We starten met optellen\n")
          return optellen()
        elif keuze2 == "aftrekken" or keuze2 == "Aftrekken": 
          print("We starten met aftrekken\n")
          return aftrekken()
        elif keuze2 == "vermenigvuldigen" or keuze2 == "Vermenigvuldigen":
          print("We starten met vermenigvuldigen\n")
          return vermenigvuldigen()
        elif keuze2 == "alles door elkaar" or keuze2 == "door elkaar" or keuze2 == "Alles door elkaar" or keuze2 == "Door elkaar":
          print("We doen alles door elkaar\n")
          return doorElkaar()
        else:
          keuze2 = input("\033[3;38;48mHelaas is deze keuze niet correct. Voer uw keuze opnieuw in.\033[0;38;48m\n")
    elif keuze1 == "taal" or keuze1 == "Taal":
      print("We starten met taal\n")
      return woordspelling()
    else:
      keuze1 = input("\033[3;38;48mHelaas is deze keuze niet correct. Voer uw keuze opnieuw in.\033[0;38;48m\n")