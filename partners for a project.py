def partenners():
    names = input("input names for group. ").split()
    names.sort()
    partner1 = names[0], names[7]
    partner2 = names[1], names[6]
    partner3 = names[2], names[5]
    partner4 = names[3], names[4]
    partnersall = [partner1, partner2, partner3, partner4]
    return partnersall

print(partenners())


