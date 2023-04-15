import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import extractData
import json

if __name__ == '__main__':

    dataFrameWeather = extractData.extractDataToDataFrame('data/weather.json')
    print(dataFrameWeather.head())


