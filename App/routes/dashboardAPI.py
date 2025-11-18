from flask import render_template, session,url_for,jsonify,redirect, Blueprint,flash,request,g
from extentions import db
import re
from ..models.user_model import User
from ..models.sponsor import Sponsor
from ..models.student import Student
from ..models.talents import Talent


dash_bp=Blueprint('dash',__name__,url_prefix='/dash')
@dash_bp.route('/competitions',methods=['GET'])
def competitions():
    return redirect(url_for('compe.display_all_comp'))
@dash_bp.route('/sponsors',methods=['GET'])
def sponsors():
    return redirect(url_for('sponsor.displayall'))
@dash_bp.route('/success',methods=['GET'])
def success():
    return render_template('admin/success.html')
@dash_bp.route('/dashboard',methods=['GET'])
def dashboard():
    return render_template('admin/dashboardhome.html')