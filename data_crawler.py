
import praw
import pandas as pd
import datetime as dt
from psaw import PushshiftAPI
from fastai.learner import *
import os
import pandas as pd
from sklearn.externals import joblib
from flask import Flask, jsonify, request


from fastai.imports import *
from fastai.structured import *

from pandas_summary import DataFrameSummary
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from IPython.display import display

from sklearn import metrics
PATH = "/home/iiitd/Desktop/Shivam2/Paperspace/"

reddit = praw.Reddit(client_id='ZuvcrQvOJn0EGA', \
                     client_secret='2FjD3cEdhxlCIZKfjrzkr2DaYJw', \
                     user_agent='parser', \
                     username='chandhokshivam', \
                     password='silkworm3')






def get_date(created):
    return dt.datetime.fromtimestamp(created)

g=lambda x:get_date(x)













def scrape(url):
	api = PushshiftAPI(reddit)
	a=list(api.search_submissions(url=m[0].url,subreddit='india'))
	topics_dict = { "title":[], "id":[], "url":[], "comms_num": [],  "created": [],  "text":[],"flair":[],"self_text":[],"domain":[],"subreddit":[],"ups":[],"author":[],"over_18":[],"thumbnail":[],"clicked":[],"contest_mode":[],"can_gild":[],"wls":[],"whitelist_status":[],"visited":[],"upvote_ratio":[],"stickied":[],"spoiler":[],"send_replies":[],"is_self":[],"locked":[],"saved":[],"gilded":[]}
    for i,submission in enumerate(d):
    	topics_dict["title"].append(submission.title)
    	topics_dict["ups"].append(submission.ups)
    	topics_dict["id"].append(submission.id)
    	topics_dict["url"].append(submission.url)
    	topics_dict["comms_num"].append(submission.num_comments)
    	topics_dict["created"].append(g(submission.created))
    
    	topics_dict["flair"].append(submission.link_flair_text)
    	topics_dict["domain"].append(submission.domain)
    
    	topics_dict["author"].append(submission.author)
	    topics_dict["is_self"].append(submission.is_self)
	    topics_dict["self_text"].append(submission.selftext)
    	topics_dict["clicked"].append(submission.clicked)
    #topics_dict["comment_sort"].append(submission.comment_sort)
    
    	topics_dict["over_18"].append(submission.over_18)
    	topics_dict["thumbnail"].append(submission.thumbnail)
    
	    topics_dict["wls"].append(submission.wls)
	    
	    topics_dict["visited"].append(submission.visited)
	    #topics_dict["upvote_ratio"].append(submission.upvote_ratio)
	    topics_dict["stickied"].append(submission.stickied)

	    
	    #topics_dict["quarantine"].append(submission.quarantine)
	    topics_dict["saved"].append(submission.saved)
	    topics_dict["gilded"].append(submission.gilded)
        
        c=[]
        for comment in submission.comments:
           
            try:
                print(comment.body)
                c.append( comment.body)
                   
            except Exception: 
                        pass      
            topics_dict['comments'].append(c)
            topics_data=pd.DataFrame(topics_dict)

     return topics_data




        
    