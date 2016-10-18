#Broji koliko ima slova a u unesenoj frazi
while True:
    pip=input('Insert the phrase')
    if pip=='q':
        break
    print(pip.capitalize())
    print("Ima " + str(pip.count('a'))+" slova a")
