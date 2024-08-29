#checkpoint
stopper = """
vari = open("speech.txt", "a")

vari.write("I love programming!")
vari.close()
vari = open("speech.txt", "r")
print(vari.read())
vari.close()

#challenges pen pal
vari = open("letter.txt", "a")
vari.write("From your Pen Pal")
vari.close()

vari = open("letter.txt", "r")
print(vari.read())
vari.close()
"""
#challenges give credit
vari = open("report.txt", "a")
vari.write("Quote was said by Gandhi")
vari.close()

vari = open("report.txt", "r")
print(vari.read())
vari.close()
