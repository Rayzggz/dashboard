import numpy as np
import pandas


def readData():
    dorm = pandas.read_csv('src/data/dorm_buildings.csv', delimiter=',')
    non_dorm = pandas.read_csv('src/data/non-dorm_buildings.csv', delimiter=',')
    weather = pandas.read_csv('src/data/weather_data.csv', delimiter=',')
    print(dorm)
