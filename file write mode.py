#checkpoint
stop = """ 
fifi = open("speech.txt", "w")
fifi.write("In short, I love to code!")
fifi.close()
new = open("porcupine.txt", "w")

#challenges never mind
fi = open("emial.txt", "w")
fi.write("Never mind")
fi.close()
"""
#challenges custom greeting cards
answer = input("what do you want to replace the text file with? ")

fil = open("report.txt", "w")
fil.write(answer)
fil.close()

fil = open("report.txt", "r")
print(fil.read())
