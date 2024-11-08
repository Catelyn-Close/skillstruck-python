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
stop = """
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


dna = 'GACCGCCGCC'
def dna_to_rna(dna):
    lister = []
    counter1 = 0
    counter2 = 1
    length = len(dna)
    while length != 0:
        splitter = dna[counter1:counter2]
        counter1 += 1
        counter2 += 1
        length -= 1
        if splitter == "T":
            splitter = "U"
        lister.append(splitter)
    full = ''.join(lister)
    return full

print(dna_to_rna(dna))



st = "Hello there."
def reverse(st):
    words = st.split()
    length = len(words)
    lengther = len(words) -1
    lister = []
    lister.extend(reversed(words))
    full = " ".join(lister)
    return full


print(reverse(st))

string_ = "fafefifofgu"
def disemvowel(string_):
    lister = []
    for char in string_:
        if char in "aeiouAEIOU":
            new = string_.replace(char, "")
            string_ = new       
    return new
print(disemvowel(string_))
length = 100
speed = 1
inc = 2
def can_snail_reach_end(length, speed, inc): 
    minute = 0
    Full_len = length
    while minute != 525600:
        Full_len += inc
        minute += 1
        Full_len -= speed
        if minute == 525600 and Full_len > 0:
            return False
        elif Full_len <= 0:
            return True
print(can_snail_reach_end(length, speed, inc))
num = 9119
def square_digits(num):
    fixer = str(num)
    string1 = ""
    for number in fixer:
        new = int(number) ** 2
        string1 += str(new)
    return int(string1)
      


print(square_digits(num))


group = "DFK"
def trilingual_democracy(group):
    e = "D", "F", "K", "I"
    f = 0
    if group[0] == group[1] or group[1] == group[2] or group[0] == group[2]:
        f += 2
    sect1 = 0
    sect2 = 0
    sect3 = 0
    if group[0] == group[1]:
        sect1 += 1
    elif group[1] == group[2]:
        sect2 += 1
    elif group[0] == group[2]:
        sect3 += 1
    if sect1 == 1 and sect2 ==0:
        g = group[2]
        return g
    elif sect2 == 1 and sect3 ==0:
        h = group[0]
        return h
    elif sect3 == 1 and sect1 ==0:
        i = group[1]
        return i
    for char in e:
        if char not in group and f == 0:
            d = char
            return d
    a, b, c = group
    if group == a + b + c:
        return a
print(trilingual_democracy(group))

#add all numbers except highest and lowest
arr = [None]
#[1,2,6,8,10]
def sum_array(arr):
    list1 = arr
    list1.sort()
    maths = arr[1:-1]
    ans = sum(maths)
    if ans == None:
        return None
    return ans



print(sum_array(arr))

#The office 11 - boredom score
staff = 
def boredom(staff):
    mydict = {
    "accounts" : 1,
    "finance" : 2,
    "canteen" : 10,
    "regulation" : 3,
    "trading" : 6,
    "change" : 6,
    "IS" : 8,
    "retail" : 5,
    "cleaning" : 4,
    "pissing about" : 25
    }
    for role in staff:
        if role in mydict:
            number += mydict[role]
            
    if number > 100:
        return "party time!!"
    elif number <= 80:
        return "kill me now"
    elif number < 100 and number > 80:
        return "I can handle this"

print(boredom(staff))

args = ([1,2,3,4,5,6,7,8,9,10])


#Last
def last(*args):
    return args[0]

print(last(*args))


    try:
        return args[-1]
    except:
        a = len(args)
        return args[a]

print(last(args))

ranger = (range(0,6))
mather = 43
while mather not in range(0,6):
    mather -= 6
    print(mather)
    if mather in ranger:
        break

ranger = (range(0,6))
"""
quantity = 6
price = 3
counter = quantity
counting = counter / 3
if counting == 0:
    quantity -= 1
else:
    while quantity >= 3:
        quantity -= counting
     

        