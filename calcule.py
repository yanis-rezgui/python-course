def hotel_frais(nuits):
    return nuits * 90


def location_voiture_frais(nbrJ):
    total = nbrJ * 35

    if nbrJ >= 7:
        total -= 50
    elif nbrJ >= 3:
        total -= 20

    return total


def vol_frais(nom):
    if(nom == "Marrakech"):
        return 35
    elif nom == "Paris":
        return 200
    elif nom == "Oran" :
        return 78
    elif nom == "Carthage":
        return 182
    elif nom == "Dakar":
        return 25

def voyage_frais(nom, nbrJ, nbrN, autres):
    return hotel_frais(nbrN) + location_voiture_frais(nbrJ) + vol_frais(nom) + autres

def