import os
import pandas as pd
from sklearn.externals import joblib
from flask import Flask, jsonify, request
from fastai.learner import *


from fastai.imports import *
from fastai.structured import *

from pandas_summary import DataFrameSummary
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from IPython.display import display

from sklearn import metrics

app = Flask(__name__)
PATH = "/home/iiitd/Desktop/Shivam2/Paperspace/"
@app.route('/predict', methods=['POST'])
def apicall():###takes json test data and returns test dataframe in pandas format
    
    try:
        test_json = request.get_json()
        test_df = pd.read_json(test_json, orient='records')


    except Exception as e:
        raise e
    
    return test_df

def predict(test_df):
    load_ids=test['ids']

    clf = 'model_v1.pk'

    if test.empty:
        return(bad_request())
    else:
        #Load the saved model
        print("Loading the model...")
        loaded_model = None
        with open(PATH+clf,'rb') as f:
            loaded_model = pickle.load(f)

        print("The model has been loaded...doing predictions now...")
        predictions = loaded_model.predict(test)
        print(predictions)
        """Add the predictions as Series to a new pandas dataframe
                                OR
           Depending on the use-case, the entire test data appended with the new files
        """
        prediction_series = list(pd.Series(predictions))

        final_predictions = pd.DataFrame(list(zip(loan_ids, prediction_series)))

        """We can be as creative in sending the responses.
           But we need to send the response codes as well.
        """
        responses = jsonify(predictions=final_predictions.to_json(orient="records"))
        responses.status_code = 200

     return (responses)

                                                                                                                                      