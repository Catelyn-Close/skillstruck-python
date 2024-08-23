num = 758302648
def descending_order(num):
    rea = []
    gth = len(str(num))
    splitter1 = 0
    splitter2 = 1
    while gth != 0:
        putter = str(num)[splitter1:splitter2]
        rea.append(putter)
        splitter1 += 1
        splitter2 += 1
        gth -= 1
    rea.sort(reverse=True)
    return ("".join( rea))
    
print(descending_order(num))

