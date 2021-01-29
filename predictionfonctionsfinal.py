import numpy as np
import pandas as pd 

def outil(data,modele) :
    df=data[['Marque','TAILLE','État','couleur','pays','genre',"Prix","Vus","likes"]]
    y = df['Prix']
    X= df.drop('Prix', axis=1)
    pred = pd.DataFrame.from_dict({'predicted' : modele.predict(X), 'true': y})
    pred.true=pd.to_numeric(pred['true'])
    pred['difference']= pred.predicted - pred.true
    plusvalue=[]
    i=0
    for i in range(len(pred)):
        plusv=round(((pred.predicted.iloc[i]/pred.true.iloc[i])*100)-100)
        plusvalue.append(plusv)
        i=i+1
        
    pred['plusvalue']=plusvalue        
    return pred


def dataplusvaluepredicted(s):
    if s.plusvalue > 75:
        return ['background-color: limegreen']*10
    elif s.plusvalue > 0:
        return ['background-color: gold']*10
    else:
        return ['background-color: indianred']*10