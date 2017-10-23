
convert = True
while convert:
    x_km = float(raw_input((" Vnesi razdaljo vb km: ")))
    p = 1.609

    x_mil = x_km / p

    print("{0} km je {1} mil".format(x_km, x_mil))

    answer = raw_input(("Vtipkaj 'da' za novo pretvorbo ali 'ne' za konec: "))

    if answer == 'da':
        continue
    elif answer == 'ne':
        convert = False
    else:
        raise ValueError('Go fuck yourself you sick bastard!!!')