#def abbreviate(letter):
#    letter = " "
#    sp = letter.split(" ")
#    return letter

#print(abbreviate("Joker"))
#print(abbreviate("Rap monster"))
#print(abbreviate("jin young park"))
def abbreviate(name):
    abb =""
    name = name.upper()
    for word in name.split(" "):
        abb += word[0]
    abb = ".".join(abb)
    return abb

print(abbreviate("Joker"))
print(abbreviate("Rap monster"))
print(abbreviate("jin young park"))
