import sys

categorie_raee = {
    "R1-Grande bianco freddo": [
        "frigorifero", "congelatore", "condizionatore", "frigorifero doppia porta",
        "frigorifero side-by-side", "frigorifero combinato", "frigorifero da incasso"
    ],

    "R2-Grande bianco non freddo": [
        "lavatrice", "lavastoviglie", "forno",
        "piano cottura", "cappa aspirante", "scaldabagno",
        "friggitrice", "forno a microonde", "piano induzione",
        "cucina a gas", "forno a vapore", "termoconvettore",
        "caldaia", "stufa a pellet", "aspirapolvere centralizzato",
        "robot aspirapolvere"
    ],

    "R3-TV Monitor a tubo catodico": [
        "tv", "monitor", "monitor CRT", "televisore CRT"
    ],

    "R4-Elettronica di consumo, Telecomunicazioni, Informatica, piccoli elettrodomestici, elettroutensili, giocattoli, apparecchi di illuminazione, dispositivi medici": [
        "frullatore", "macchina per il caffè", "bollitore elettrico",
        "robot da cucina", "aspirapolvere", "ferro da stiro", "phon",
        "bilancia da cucina", "tritatutto", "spremiagrumi",
        "macchina per il pane", "centrifuga", "macchina per il gelato",
        "macchina per la pasta", "piastre per la cottura dei panini",
        "tostapane a muffin", "friggitrice ad aria", "macchina per lo yogurt",
        "macchina per il sushi", "router", "stampante", "scanner",
        "telefono fisso", "tastiera e mouse", "webcam",
        "altoparlanti per pc", "microfono", "hard disk esterno",
        "scheda grafica", "proiettore", "joystick", "penna usb",
        "custodia per laptop", "custodia per smartphone",
        "lampadario", "lampada da tavolo", "lampada a sospensione",
        "faretti", "strisce led", "lampioncini da giardino",
        "lampada da lettura", "luce notturna", "lampada da parete",
        "lampada da soffitto", "termometro digitale",
        "misuratore di pressione sanguigna", "bilancia pesapersone",
        "elettrocardiografo portatile", "nebulizzatore",
        "monitor per la glicemia", "sfigmomanometro",
        "aspiratore di secrezioni", "saturimetro",
        "monitor per il sonno", "stimolatore muscolare",
        "apparecchio per la terapia del dolore", "tensimetro",
        "termometro auricolare", "monitor per la respirazione",
        "sonda per ecografia", "monitor per la frequenza cardiaca",
        "termometro senza contatto", "defibrillatore portatile",
        "stimolatore cardiaco esterno"
    ],

    "R5-Sorgenti luminose a scarica": [
        "lampade fluorescenti", "sorgenti luminose compatte"
    ]
}


def stampa_raee():
    for categoria, oggetti in categorie_raee.items():
        print(f"{categoria}:")
        for oggetto in oggetti:
            print(f"- {oggetto}")
        print()


def smista_raee():
    raee = input("Quale rifiuto vuoi smistare: ")
    raee = raee.lower()

    categoria_raee = None

    for categoria, oggetti in categorie_raee.items():
        if raee in oggetti:
            categoria_raee = categoria
            break

    if categoria_raee:
        print(f"\nL'oggetto {raee} appartiene alla categoria {categoria_raee}")
    else:
        print("L'oggetto inserito non corrisponde a nessuna categoria RAEE.")


def menu():
    while True:
        print("Seleziona un'opzione:")
        print("1. Visualizza la lista di di rifiuti RAEE")
        print("2. Smista i rifiuti per categoria RAEE")
        print("0. Esci")

        scelta = input("Scelta: ")

        if scelta == "1":
            stampa_raee()
        elif scelta == "2":
            smista_raee()
        elif scelta == "0":
            sys.exit()
        else:
            print("Scelta non valida. Riprova.")


menu()
