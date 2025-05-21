#Saisie des moyennes
print("Calcul de moyenne\n")
math = float(input("Veuillez saisir la moyenne en math svp :"))
pc = float(input("Veuillez saisir la moyenne en pc svp :"))
fr = float(input("Veuillez saisir la moyenne en fr svp :"))
ang = float(input("Veuillez saisir la moyenne en anglais svp :"))
eps = float(input("Veuillez saisir la moyenne en eps svp :"))

#Saisie des coefficients
Cmath=math*5
Cpc=pc*4
Cfr=fr*3
Cang=ang*2
SC=15
#eps est coeff 1

#Calcul de la moyenne
Moy=(Cmath+Cpc+Cfr+Cang+eps)/SC
print(f"\nLa moyenne generale de l'etudiant est {Moy:.2f}")

#Mention
if Moy < 10 :
    print("\nla mention de l'etudiant est mediocre")
elif 10 <= Moy <12 :
    print("\nla mention de l'etudiant est passable")
elif 12<= Moy <14 :
    print("\nla mention de l'etudiant est assez bien")
elif 14<= Moy <16 :
    print("\nla mention de l'etudiant est bien")
else :
    print("\nla mention de l'etudiant est tres bien")