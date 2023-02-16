# -*- coding: utf-8 -*-
"""
on veut :
    - entrer le nombre de lettre
    - à chaque itération renseigner les lettres présentes / bien placées / absentes
    - tirer du dico les mots avec le bon nb de lettres
    - 

caractères spéciaux:

pour plus tard
 - Distance de Levenshtein
 
 
 premier test concluant 27/10 13:20
 primier SUTOM 27/10 13:33
 
 amélioration à faire :
     - pas de même position pour les présentes bien placées
     - pondération des lettres à tester
     - pondération des lettres + position
 

"""

import random as r
import sys
import os



def suppr_double(lst_mots):
    temp = ""
    for mot in lst_mots:
        if mot == temp:
            lst_mots.remove(mot)
        temp = mot
    return lst_mots
    

def nb_de_lettres():
    return input ("Combien de lettres dans le mot? ")


def lettres_absentes():
    absentes = input ("Listez les lettres absentes: (collées ex: addef)")
    output = []
    for i in range (len(absentes)):
        output.append(absentes[i])
    return output


def lettres_presente():
    output = []
    while True:
        presentes = input ("Listez les lettres mal placées et leur position: (ex:a1g7)")
        if len(presentes)%2==0 :
            break
        else:
            print("INPUT ERROR")
    
    for i in range (len(presentes)):
        output.append(presentes[i])
    return output


def lettres_bien_placees():
    output = []
    while(True):
        pbp = input ("Listez les lettres bien placées et leur position: (ex:a1g7)")
        if(len(pbp)%2==0) :
            break
        else:
            print("INPUT ERROR")
    
    for i in range (len(pbp)):
        output.append(pbp[i])
    return output



def suppr_la(lst_mots,lst_la):
    lst_suppr=[]
    
    #print(f"\nil y a {len(lst_mots)} mots")
    for lettre in lst_la:
        #[ x for x in l if "2" not in x ]
        
        lst_suppr += [mot for mot in lst_mots if lettre in mot]
    
        for mot_s in lst_suppr:
            if mot_s in lst_mots:
                lst_mots.remove(mot_s)

    #print(f"final : il y a {len(lst_mots)} mots\n")

    return lst_mots


def suppr_lp(lst_mots,lst_lp):
    if len(lst_lp)==0:
        return lst_mots
    
    lst_suppr=[]
    
    lst_l,lst_p=lettre_et_pos(lst_lp)
    
    #print(f"\nil y a {len(lst_mots)} mots")
    for lettre,pos in zip(lst_l,lst_p):
        #[ x for x in l if "2" not in x ]
        
        lst_suppr += [mot for mot in lst_mots if (mot[pos]==lettre) or lettre not in mot]
    
        for mot_s in lst_suppr:
            if mot_s in lst_mots:
                lst_mots.remove(mot_s)
                
    return lst_mots


def suppr_bp(lst_mots,lst_bp):
    lst_suppr=[]
    
    lst_l,lst_p=lettre_et_pos(lst_bp)
    
    #print(f"\nil y a {len(lst_mots)} mots")
    for lettre,pos in zip(lst_l,lst_p):
        #[ x for x in l if "2" not in x ]
        
        lst_suppr += [mot for mot in lst_mots if (mot[pos]!=lettre) or lettre not in mot]
    
        for mot_s in lst_suppr:
            if mot_s in lst_mots:
                lst_mots.remove(mot_s)
                
    return lst_mots


def lettre_et_pos(lst):
    lst_l=[]
    lst_p=[]
    pair=True
    for i in lst:
        if pair==True:
            lst_l.append(i)
            pair=False
        else:
            lst_p.append(int(i)-1)
            pair=True
    return lst_l,lst_p


def lettre_double(mot):
    for i in mot:
        if mot.count(i)>1:
            return True
    return False


def select_mot(lst):
        
    lstbis = [mot for mot in lst if not lettre_double(mot)]
    if len(lstbis):
        ind = r.randint(0,len(lstbis)-1)
        return lstbis[ind]
    else:
        ind = r.randint(0,len(lst)-1)
        return lst[ind] 


def freq_lettre(lst_m):
    #lst_l : lettre,occurence,lettre,occurance
    lst_l=[25]
    for mot in lst_m:
        mot=suppr_doublon(mot)
        for lettre in mot:
            lst_l[no_lettre(lettre)]+=1
    return lst_l

def no_lettre(lettre):
    if (lettre=='a'):return 0
    elif (lettre=='b'):return 1
    elif (lettre=='c'):return 2
    elif (lettre=='d'):return 3
    elif (lettre=='e'):return 4
    elif (lettre=='f'):return 5
    elif (lettre=='g'):return 6
    elif (lettre=='h'):return 7
    elif (lettre=='i'):return 8
    elif (lettre=='j'):return 9
    elif (lettre=='k'):return 10
    elif (lettre=='l'):return 11
    elif (lettre=='m'):return 12
    elif (lettre=='n'):return 13
    elif (lettre=='o'):return 14
    elif (lettre=='p'):return 15
    elif (lettre=='q'):return 16
    elif (lettre=='r'):return 17
    elif (lettre=='s'):return 18
    elif (lettre=='t'):return 19
    elif (lettre=='u'):return 20
    elif (lettre=='v'):return 21
    elif (lettre=='w'):return 22
    elif (lettre=='x'):return 23
    elif (lettre=='y'):return 24
    elif (lettre=='z'):return 25
    return -1


def suppr_doublon(mot):
    for lettre in mot:
        if mot.count(lettre)>1:
            mot.remove(lettre)
    return mot
    

def prop_mot(mot):
    print("Proposition de mot : "+mot)


def est_trouvee(lst):
    trouve = input ("Est-ce le bon mot? (Y/n/show) ")
    if (trouve=="show"):
        print("vous avez choisi de montrer la liste de mots:\n",lst)
        return est_trouvee(lst)
    if (trouve=="Y"): return True
    elif (trouve=="n"): return False
    else : 
        print("ERROR : Entrée non valide")

        return est_trouvee(lst)


def liste_mots(l_mot):
    #"C:\Users\777hd\Documents\pgrmRDM\motsFrancais.txt"
    path = os.path.dirname(__file__)

    entry = path +"\motsFrancais.txt"
    lst = []
    #print(int(l_mot))
    
    with open(entry, 'r', encoding="utf-8") as file:
        
        for i in file:
            if(len(i) == (int(l_mot)+1)):
               #print(i)
               mot=i[:int(l_mot)]
               lst.append(mot)
            
    
    return lst


def premiere_lettre(lst):
    lettre = input("première lettre : ")
    
    return [mot for mot in lst if mot[0]==lettre]


def type_jeu():
    jeu = int(input("SUTOM -> 0 ou WORDLE -> 1 : "))
    if jeu > 1:
        jeu=type_jeu()
    
    return jeu

    

def main():
    
    jeu = type_jeu()
    lst=[]
    
    if jeu:
        lst = liste_mots(5)
    else:    
        nb_l = nb_de_lettres()
        lst = liste_mots(nb_l)
        lst = premiere_lettre(lst)
    
    lst = suppr_double(lst)
    
    trouve = False
    
    print(f"-> {len(lst)} possibilité")
    
    if lst==[]:
        sys.exit("ERROR : select_mot -> lst entrée vide")

    mot = select_mot(lst)
    prop_mot(mot)
    trouve = est_trouvee(lst)
    if (not trouve):
        lst.remove(mot)
    
    while (not trouve):
        
        lst_la = lettres_absentes()
        lst_lp = lettres_presente()
        lst_bp = lettres_bien_placees()
        
        lst = suppr_la(lst,lst_la)
        lst = suppr_lp(lst,lst_lp)
        lst = suppr_bp(lst,lst_bp)
        
        """ 
        j'élimine de la liste tous les mots avec 1 ou plr lettre absentes
        j'élimine les mots sans la lettre bien placée
        j'affiche
        """
        
        print(lst)
        
        ind = r.randint(0,len(lst)-1)
        mot = lst[ind]
        prop_mot(mot)
        trouve = est_trouvee(lst)
        if (not trouve):
            lst.remove(mot)
    
    
    return 0


"""__________________Main________________"""


main()



"""______________________________________"""


