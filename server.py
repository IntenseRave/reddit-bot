
from data_crawler import *
from model import *
import json
import requests


def url_to_data(url):
	df=scrape(url)
	return df


def data_to_prediction(df):
	responses=predict(df)
	return responses

df_test=url_to_data(url)####Takes url and gives dataframe to be tested
header = {'Content-Type': 'application/json', \
                  'Accept': 'application/json'}


"""Converting Pandas Dataframe to json
"""
data_test = df_test.to_json(orient='records')####converting test data to json
data= requests.post("http://0.0.0.0:8000/predict", \
                    data = json.dumps(data_test),\
                    headers= header)#####sending test data to api call in reddit_app
resp=data_to_prediction(data)

print(resp.status_code)
print(resp.json())
