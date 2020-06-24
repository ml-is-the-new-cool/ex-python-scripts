pierres_max = 30

somme = 0
hauteur = 0

while True:
    # pour ajouter un étage on ajoute sa hauteur au carré
    somme_temp = somme + (hauteur + 1) ** 2
    
    # si on a dépassé le total de pierres, on ne peut pas ajouter un étage
    if somme_temp > pierres_max:
        break
    
    # sinon, on peut ajouter un étage
    else:
        hauteur += 1
        somme = somme_temp
    

print(somme)
print(hauteur)
