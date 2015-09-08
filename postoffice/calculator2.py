def weight(gram):
    if gram > 2 or gram <= 0:
        return False
    else:
        return True

def meassurements(langd, bredd, thickness):
    if langd >= 14\
            and langd <= 60\
            and bredd >= 9 \
            and langd + bredd + thickness <= 90 \
            and langd + bredd + thickness > 0:
        return True
    else:
        return False

def weightpak(gram):
    if gram > 20 or gram <= 2.001:
        return False
    else:
        return True

def meassurementspak(langd, bredd, height):
    if langd <= 150 and bredd <= 70 and height <= 115:
        return True
    else:
        return False