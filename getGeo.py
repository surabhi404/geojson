import pandas as pd
import requests
import json
def read_file(a):
    df = pd.read_csv(a)
    print(df.head())
    pd.set_option('display.max_rows', None)
    return df
    file_processing(df)
def file_processing(df):
    for i, row in df.iterrows():
    apiAddress = str(df.at[i,'street'])+','+str(df.at[i,'zip'])+','+str(df.at[i,'city'])+','+str(df.at[i,'country'])
    
    parameters = {
        "key": "khAc51jPMyXgbgfITfvc7VuACPW9J2ij",
        "location": apiAddress
    }

    response = requests.get("http://www.mapquestapi.com/geocoding/v1/address", params=parameters)
    print(response)
    data = response.text
    dataJ = json.loads(data)['results']
    lat = (dataJ[0]['locations'][0]['latLng']['lat'])
    lng = (dataJ[0]['locations'][0]['latLng']['lng'])
    print(lat,lng)
    df.at[i,'lat'] = lat
    df.at[i,'lng'] = lng
    file_output(df)
def file_output(df):
    df.to_csv('restaurants_geo.csv')

read_file("restaurants.csv")
