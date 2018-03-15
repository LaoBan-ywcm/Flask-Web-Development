# -*- coding: utf-8 -*-
'''
    Author: LaoBan-ywcm
    Date:   2018-03-13 22:14:43
    Last Modified by:   LaoBan-ywcm
    Last Modified time: 2018-03-15 21:29:24
'''
from datetime import datetime


from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return render_template('index.html',
        current_time=datetime.utcnow())

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)