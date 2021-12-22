uinput = 'x'
oioi = []

def phraseProcessor(phrase):
    capitalised = phrase.capitalize()
    if (phrase.startswith(("how","what","why"))):
        return '{}?'.format(capitalised)
    else:
        return '{}.'.format(capitalised)    

while uinput != '/end':
    uinput = input("Say something: ")
    if(uinput != '/end'):
        oioi.append(phraseProcessor(uinput))

concatstring = " ".join(oioi)

print (concatstring)    

