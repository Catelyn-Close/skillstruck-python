stopper = """
#checkpoint
this_list = ['panda', 'lion', 'giraffe', 'tiger', 'elephant', 'monkey', 'fish', 'snake', 'bearded dragon', 'koala']

def feeding(this_list):
    if len(this_list) == 1:
        print("The " + this_list[0] + " has been fed.")
    else:
        mid = len(this_list) // 2
        first_half = this_list[mid:]
        second_half = this_list[:mid]
        
        feeding(first_half)
        feeding(second_half)

feeding(this_list)
#books and sequels
books = [int(n) for n in input("Input a list of numbers").split()]
lister = []
def pages(books):
    
    if len(books) == 2:
        one = books[0]
        two = books[1]
        three = one + two
        lister.append(three)
    else:
        mid = len(books) // 2
        first = books[mid:]
        second = books[:mid]

        pages(first)
        pages(second)
    rev = list(reversed(lister))
    return rev
print(pages(books))
"""
#pollinating Bees
flowers = [int(n) for n in input("How many blossoms are on each tree?").split()]
listing = []
def orchard(flowers):
    if len(flowers) == 1:
        blossom = flowers[0] * 3
        listing.append(blossom)
    else:
        mid = len(flowers) // 2
        first = flowers[mid:]
        second = flowers[:mid]

        orchard(first)
        orchard(second)
    rev = list(reversed(listing))
    return rev
print(orchard(flowers))