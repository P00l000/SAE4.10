import json
import pandas as pd

def extractDataToDataFrame (file):
    # Charger le fichier JSON
    with open(file, 'r') as f:
        data = json.load(f)

    # Extraire la partie spécifique du JSON en tant que dictionnaire
    dataDict = data['data']

    # Créer un DataFrame à partir du dictionnaire
    dataFrameFile = pd.DataFrame.from_dict(dataDict)

    return dataFrameFile
