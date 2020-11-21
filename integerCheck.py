def integerCheck(delen1, delen2):
  #er wordt gecheckt of het een positief heel getal boven de 10 is
  goedeWaarde = "false"
  f = delen1 / delen2
  if f.is_integer() and f > 0 and f < 11:
    goedeWaarde = "true"
  else:
    goedeWaarde = "false"
  return goedeWaarde