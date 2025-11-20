from flask import render_template, session,url_for,jsonify,redirect, Blueprint,flash,request,g
from extentions import db
from datetime import datetime
from ..models.competitions import Comp
from ..models.sponsor import Sponsor
from ..models.successstroy import Story
from ..models.student import Student
from ..models.user_model import User
from middleware import login_required

userview_bp=Blueprint('userview',__name__,url_prefix='/userview')

@userview_bp.route('/compdisplayall',methods=['GET'])
@login_required
def compdisplayall():
    data = db.session.query(Comp).all()
    return render_template('competitions.html',data=data)
@userview_bp.route('/sponsordisplayall',methods=['GET'])
@login_required
def sponsordisplayall():
    data = db.session.query(Sponsor).all()
    return render_template('sponsors.html',data=data)
@userview_bp.route('/successdisplayall',methods=['GET'])
def successdisplayall():
    data = db.session.query(Story).all()
    return render_template('home.html',data=data)
