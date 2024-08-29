stopper = """
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





thing = ([1,2,3,4,5,6,7,8,9,11])
def last(thing):
    real = thing
    counter = len(real)
    counter2 = counter - 1
    other = thing[counter2:counter]
    return thing[-1] or return other


print(*last(thing))


sentence = "is2 Thi1s T4est 3a"
def order(sentence):
    first = sentence.split()
    gth = len(first)
    real = []
    for i in first: 
        if first[i] == "1":
            real.append(word1)
            return real

print(order(sentence))
"""
#vowel count
stopperr = """
sentence = "aeiou"

def get_count(sentence):
    vowels = ("a", "e", "i", "o", "u")
    counter = 0
    length = len(sentence)
    counter1 = 0
    counter2 = 1
    while length != 0:
        splitter = sentence[counter1:counter2]
        counter1 += 1
        counter2 += 1
        if splitter in vowels:
            counter += 1
        length -= 1
    return counter

print(get_count(sentence))
"""

legs_number = 34
heads_number = 11
horns_number = 6


def get_animals_count(legs_number, heads_number, horns_number):
    leggies = legs_number
    head = heads_number
    horn = horns_number
    diction = {
        "rabbit" : 0,
        "chicken" : 0,
        "cow" : 0
    }
    while leggies != 0:
        hmc = int(horn / 2)
        diction["cow"] = hmc
        head -= 1 * hmc
        leggies -= 4 * hmc
        return leggies
    while leggies != 0:
    return head
    return horn
    return diction




print(get_animals_count(legs_number, heads_number, horns_number))

