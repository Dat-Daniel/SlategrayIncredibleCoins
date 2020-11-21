#functies
from programmaKeuze import programmaKeuze

#main program
print("WELKOM BIJ HET OEFENPROGRAMMA VOOR REKENEN EN TAAL\n")
nogEenKeer = "hallo"
while nogEenKeer != "nee":
	programma = programmaKeuze()
	nogEenKeer = input("Wil je nog een oefening doen? (ja/nee)\n")
	while nogEenKeer != "ja" and nogEenKeer != "nee":
		nogEenKeer = input(
		    "\033[3;38;48mHelaas is deze keuze niet correct. Voer uw keuze opnieuw in.\033[0;38;48m\n"
		)