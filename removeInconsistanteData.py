import  splitDataFromDate as split
import pandas as pd
def RemoveInconsistanteData(dataFrame):
    #on regarde si il ya  des valeurs null (non)
    #print(dataFrame.isnull().values.any())

    # on défini les données incohérente
    # on regarde le min/max de chaque colonne pour voir si certaine donnée sont incohérante:


    # On trouve des données incohérante avec l'humidité:
    #dataFrameShorted = dataFrame.sort_values(by='humidity')
    # dataFrameShorted= dataFrame.sort_values(by='humidity',ascending=False)
    # print(dataFrameShorted[['temp','report_date','humidity','pressure']].head(n=400))
    #donc on définit un max cohérant et on enleve le reste
    maxHumidity=100;

    #idem avec les pression
    minPressure=90000;
    maxPressure=104000;

    #On enleve les données incohérantes
    removeCondition = (dataFrame['humidity'] <= maxHumidity)
    dataFrameFiltred = dataFrame.loc[removeCondition]


    removeCondition = (dataFrameFiltred['pressure'] >= minPressure)
    dataFrameFiltred = dataFrameFiltred.loc[removeCondition]

    removeCondition = (dataFrameFiltred['pressure'] <= maxPressure)
    dataFrameFiltred = dataFrameFiltred.loc[removeCondition]

    ##on regarde si les températures sont cohérantes par saisons
    #dataFrameH2020 = split.SplitDataFromDate(dataFrameFiltred,'s','p-2020')
    #print(dataFrameH2020.sort_values(by='temp', ascending=False))


    return dataFrameFiltred





