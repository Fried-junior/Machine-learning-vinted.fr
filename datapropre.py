import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import seaborn as sns 


def nettoyage(data):
    data.pop("Unnamed: 0")
    data.pop("ajout")
    data.pop("Modepaiement")
    data = data.rename(columns = {'Nombre de vus': 'Vus','interet':'likes'})
    
    
    #Prix : le format est de type X,00 €, on choisi donc de ne garder la première partie pour suppimer la virgule et le €.
    
    pr =[]
    for i in range(len(data.prix)):
        try : 
            head, sep, tail = data.prix.iloc[i].partition(',')
            carac= head
            pr.append(carac)
        except : 
            return 
    
    data['Prix']=pr
    data['Prix']=data['Prix'].str.replace(' ','')
    data.likes=data.likes.replace(np.nan,0)
    data.Vus=data.Vus.replace(np.nan,0)
    data.pop("prix")
    data=data.dropna()
    
    #Likes : le format est de type X UTILISATEURS, on remplace utilisateur par " ".
    
    try:
        data['likes']=data['likes'].str.replace('UTILISATEURS','')
    except:
        return

    try:
        data['likes']=data['likes'].str.replace('UTILISATEUR','')
    except:
        return
    
    # Couleur : il peut il y avoir plusieurs couleur, on décide de ne grader que la première couleur mentionné.
    
    premier =[]
    for i in range(len(data.Couleur)):
        try : 
            head, sep, tail = data.Couleur.iloc[i].partition(',')
            carac= head
            premier.append(carac)
        except : 
            print()

    data['couleur']=premier
    data['couleur']=data['couleur'].str.replace(" ","") 
    data.pop("Couleur")
    
    # Emplacement : le format est de type VILLE,PAYS ; On choisit de ne garder que le pays.
    
    pays =[]
    for i in range(len(data.Emplacement)):
        try : 
            head, sep, tail = data.Emplacement.iloc[i].partition(',')
            if tail=="":
                carac= head
            else: 
                carac= tail
            pays.append(carac)
        except : 
            vide=0
        
    data['pays']=pays
    data['pays']=data['pays'].str.replace("/ BELGIË","")
    data['pays']=data['pays'].str.replace("L',","")
    data['pays']=data['pays'].str.replace(" ","")
    data['pays']=data['pays'].str.replace("O","")
    data['pays']=data['pays'].str.replace(",","")

    paysoff=[]
    for i in range(len(data.pays)):
        if data.pays.iloc[i]=="(CASCURBAN)ESPAÑA":
            data.pays.iloc[i]="ESPAÑA"      
        elif data.pays.iloc[i]=="A(SANTANDRE)ESPAÑA": 
            data.pays.iloc[i]="ESPAÑA" 
        elif data.pays.iloc[i]=="LES)ESPAÑA": 
            data.pays.iloc[i]="ESPAÑA" 
        else : 
            vide=0
            
    data.pop("Emplacement")

    
    # Taille : on transforme la taille en float et on supprime toutes les valeurs qui ne sont pas convertibles et donc qui ne correspondent pas à des chaussures. Notre analyse sur les données manquantes nous a permis de déterminer que les NA correspondent à des articles qui ne sont pas des chaussures, on peut donc les supprimer.
    
    data=data.dropna()
    liste=[]
    for i in range(len(data.Taille)):
        try:
            t=float(data.Taille.iloc[i])
        except:
            t=data.Taille.iloc[i]
        liste.append(t)

    data['TAILLE']=liste

    Liste=[]
    for i in range(len(data.TAILLE)):
        if isinstance(data.TAILLE.iloc[i], (int, float))==False:
            carac=i
            Liste.append(carac)

    data.pop("Taille")
    data.drop(data.index[Liste], inplace=True)
    

    return  data