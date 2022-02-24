import math
import joblib
import pandas as pd

# import the trained model
model = joblib.load('D:/downloads/PassagePredict/DT_Mav_Model.pkl')

# Set the data structure of the model
data_structure = {'DECISION_ID': [2], 'WEEKDAY_0': [0], 'WEEKDAY_1': [0], 'WEEKDAY_2': [0], 'WEEKDAY_3': [0],
                  'WEEKDAY_4': [0], 'WEEKDAY_5': [0], 'WEEKDAY_6': [0], 'HOUR_0': [0], 'HOUR_1': [0],
                  'HOUR_2': [0], 'HOUR_3': [0], 'HOUR_4': [0], 'HOUR_5': [0], 'HOUR_6': [0], 'HOUR_7': [0],
                  'HOUR_8': [0], 'HOUR_9': [0], 'HOUR_10': [0], 'HOUR_11': [0], 'HOUR_12': [0], 'HOUR_13': [0],
                  'HOUR_14': [0], 'HOUR_15': [0], 'HOUR_16': [0], 'HOUR_17': [0], 'HOUR_18': [0], 'HOUR_19': [0],
                  'HOUR_20': [0], 'HOUR_21': [0], 'HOUR_22': [0], 'HOUR_23': [0], 'SITE_ID_200': [0],
                  'SITE_ID_287': [0], 'SITE_ID_540': [0], 'SITE_ID_550': [0], 'SITE_ID_650': [0],
                  'SITE_ID_709': [0], 'SITE_ID_710': [0], 'SITE_ID_720': [0], 'SITE_ID_740': [0], 'SITE_ID_750': [0],
                  'SITE_ID_760': [0], 'SITE_ID_770': [0], 'SITE_ID_790': [0]}


def predict(variables):
    data = data_structure.copy()
    data[variables['weekday']] = [1]
    data[variables['site']] = [1]
    data[variables['hour']] = [1]

    df = pd.DataFrame(data=data)
    y = model.predict(df)

    return math.floor(y[0])
