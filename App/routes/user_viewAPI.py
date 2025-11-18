from flask import render_template, session,url_for,jsonify,redirect, Blueprint,flash,request,g
from extentions import db
from datetime import datetime
from ..models.competitions import Comp
from ..models.sponsor import Sponsor
from ..models.successstroy import Story

userview_bp=Blueprint('userview',__name__,url_prefix='/userview')

@userview_bp.route('/compdisplayall',methods=['GET'])
def compdisplayall():
    data = db.session.query(Comp).all()
    return render_template('competitions.html',data=data)
@userview_bp.route('/sponsordisplayall',methods=['GET'])
def sponsordisplayall():
    data = db.session.query(Sponsor).all()
    return render_template('sponsors.html',data=data)
@userview_bp.route('/successdisplayall',methods=['GET'])
def successdisplayall():
    data = db.session.query(Story).all()
    return render_template('home.html',data=data)