#!/usr/bin/env python3
# -*- coding:utf-8-*-
from flask import Flask,render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    course = {
             'python': 'lou+ python',
            'java': 'java base',
            'bigdata': 'spark sql',
            'teacher': 'shixiaolou',
            'is_unique': False,
            'has_tag': True,
            'tags': ['c', 'c++', 'docker']
            }
    return render_template('index.html',course=course)

@app.route('/courses/<username>')
def user_index(username):
    return 'Course:{}'.format(username)
