from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main
from flask_login import login_required



@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@main.route('/dicks', methods=['GET', 'POST'])
@login_required
def cheese():
    return render_template('index.html')

