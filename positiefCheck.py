def positiefCheck(aftrekken1, aftrekken2):
  randomWoord = "niks"
  while randomWoord == "niks":
    f = aftrekken1 - aftrekken2
    if f >= 0:
      goedeWaarde = "true"
      randomWoord = "iets"
    else:
      goedeWaarde = "false"
    return goedeWaarde