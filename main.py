import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import extractData
import json

if __name__ == '__main__':


    dataFrameWeather = extractData.extractDataToDataFrame('data/weather.json')
    dataFrameWeather['temp'] = dataFrameWeather['temp'].astype('float')
    dataFrameWeather['humidity'] = dataFrameWeather['humidity'].astype('float')
    dataFrameWeather['pressure'] = dataFrameWeather['pressure'].astype('int')
    dataFrameWeather['report_date'] = pandas.to_datetime(dataFrameWeather['report_date'])
    print(dataFrameWeather.head())


