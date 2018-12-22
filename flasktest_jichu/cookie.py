#!/usr/bin/env python3

from flask import Flask,render_template,request,make_response

app= Flask(__name__)

@app.route('/')
def index():
    return render_template('cookie_index.html')

@app.route('/setcookie',methods=['POST','GET'])
def setcookie(name):
    if request.method=='POST':
        user = request.form['name']
    resp = make_response(render_template('readcookie.html',name=name))
    resp.set_cookie('userID',user)
@app.route('/getcookie')
def getcookie():
    request.cookies.get('userID')
    return '<h1>welcome,'+name+'</h1>'


if __name__=='__main__':
    app.run()

