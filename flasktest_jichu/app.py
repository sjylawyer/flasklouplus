#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask,url_for,redirect,render_template,request
import requests

app = Flask(__name__)


@app.route('/')
def index():
    name = resquest.cookies.get('name')
    return 'hello{}'.format(name)

@app.route('/courses/<coursename>')
def user_index(coursename):
    return render_template('courses.html',coursename=coursename)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post {}'.format(post_id)


@app.route('/test')
def test():
    print(url_for('user_index',name='java',_external=True))
    return 'test'

@app.route('/courses/<name>')
def name():
    if name=='java':
        return redirect(url_for('index'))

@app.route('/httptest',methods=['GET','POST'])
def httptest():
    if request.method=='GET':
        print('t:',request.args.get('t'))
        print('q:',request.args.get('q'))
        return 'It is a get request!'
    else:
        print('Q:',request.args.get('Q'))
        return 'It is a post request!'
if  __name__=='__main__':
    app.run()
