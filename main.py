'''
2.2 Feladat
A program számolja össze, hogy hány darab 'E' vagy 'e' betűt tartalmazó szó van a szavak listában. 
A képernyőre írja is ki a feltételnek megfelelő szavakat!
'''

szavak = ['Elemér', 'Emma', 'ajtó', 'róka', 'egér']
e_szavak = [szo for szo in szavak if "e" in szo or "E" in szo]
print(e_szavak)