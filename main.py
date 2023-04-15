import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import extractData
import removeInconsistanteData

import removeInconsistanteData
import json

if __name__ == '__main__':
    #on recup les données et on les mets dans un dataFrame
    dataFrameWeather = extractData.extractDataToDataFrame('data/weather.json')
    #on le type
    dataFrameWeather['temp'] = dataFrameWeather['temp'].astype('float')
    dataFrameWeather['humidity'] = dataFrameWeather['humidity'].astype('float')
    dataFrameWeather['pressure'] = dataFrameWeather['pressure'].astype('int')
    dataFrameWeather['report_date'] = pd.to_datetime(dataFrameWeather['report_date'])

    removeInconsistanteData.RemoveInconsistanteData(dataFrameWeather)

