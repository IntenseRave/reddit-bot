from flask import Flask,request,jsonify,render_template,url_for,redirect
import sys
import requests

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template("index.html",url="")
#Trained Model Object
 # model = pickle.load(open('pickle/model_v1.pk','rb'))
@app.route('/result',methods=["GET","POST"])
def result():
    try:
        if request.method =="POST":
            #url given by user
            url=request.form["query"]
            url="https://robohash.org/"+url

            print(url)
            #scraping data from url
            #data_frame=d
             # return data_frame.to_json(orient="records")
            return render_template("index.html",url=url)
        else:
            return ("NOT Working")
    except Exception as e:
        return(str(e))




if __name__ == "__main__":
    app.run()
