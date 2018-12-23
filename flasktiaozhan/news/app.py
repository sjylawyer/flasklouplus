#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask,url_for,redirect,render_template,request
import json
import os

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    path = "/home/shiyanlou/files"
    s = []
    files = os.listdir(path)
    for file in files:
        print(file)
        if not os.path.isdir(file):
            with open(path+'/'+file,'w') as f:
                news_data=json.load(f)
                print(news_data)
if __name__=='__main__':
    app.run()
