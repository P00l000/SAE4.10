import splitDataFromDate
import datetime
import pandas as pd

def createDataFrameMinMaxMoy(fct,typeDecoupage,df, parametre):
    firstDataDate = df['report_date'].min()
    lastDataDate = df['report_date'].max()
    saisons = ['p','e','a','h']
    donnees = {typeDecoupage :[],
               parametre: [],}

    if typeDecoupage == 'annee':
        annee = int(firstDataDate.year)
        derniereAnnee = int(lastDataDate.year)
        while annee <= derniereAnnee :
            dataFrameSplited = splitDataFromDate.SplitDataFromDate(df,'a',annee)
            valeurfct = ExecuteFct(dataFrameSplited,fct,parametre)
            donnees[typeDecoupage] += [annee]
            donnees[parametre] += [valeurfct]
            annee+=1

    if typeDecoupage == 'mois':
        annee = int(firstDataDate.year)
        mois = int(firstDataDate.month)
        derniereAnnee = int(lastDataDate.year)
        while annee <= derniereAnnee :
            while mois <= 12 :
                dataFrameSplited = splitDataFromDate.SplitDataFromDate(df,'m',str(mois)+'/'+str(annee))
                valeurfct = ExecuteFct(dataFrameSplited,fct,parametre)
                donnees[typeDecoupage] += [str(mois)+'/'+str(annee)]
                donnees[parametre] += [valeurfct]
                mois+=1
            mois=1
            annee+=1

    if typeDecoupage == 'saison':
        annee = int(firstDataDate.year)
        derniereAnnee = int(lastDataDate.year)
        saison= 0
        while annee <= derniereAnnee:
            while saison <4 :
                dataFrameSplited = splitDataFromDate.SplitDataFromDate(df, 's', saisons[saison] + '-' + str(annee))
                valeurfct = ExecuteFct(dataFrameSplited, fct, parametre)
                donnees[typeDecoupage] += [saisons[saison] + '-' + str(annee)]
                donnees[parametre] += [valeurfct]
                saison += 1
            saison = 1
            annee += 1
    return pd.DataFrame.from_dict(donnees)


def ExecuteFct (df,fct,parametre ):
    if fct =='min':
        return df[parametre].min()
    if fct =='max':
        return df[parametre].max()
    if fct =='moy':
        return df[parametre].mean()








