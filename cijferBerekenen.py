def cijferBerekenen(goed, fout):
  #Berekenen van je cijfer
  totaalAantalPunten = goed + fout
  score = (goed / totaalAantalPunten) * 10
  if goed == 1:
    print("\nJe hebt " + str(goed) + " antwoord goed\n")
  else:
    print("\nJe hebt " + str(goed) + " antwoorden goed\n")
  
  if score >= 6:
    return "Je hebt een \033[1;32;48m" + str(round(score, 2)) + "\033[0;38;48m\n \n"
  else:
    return "Je hebt een \033[1;31;48m" + str(round(score, 2)) + "\033[0;38;48m\n \n"
