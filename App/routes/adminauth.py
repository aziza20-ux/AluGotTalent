from flask import render_template, session,url_for,redirect, Blueprint,flash,request,g
from werkzeug.utils import secure_filename
from datetime   import datetime
import os
from extentions import db
from sqlalchemy.exc import IntegrityError
from ..models.user_model import User
from ..models.sponsor import Sponsor
from ..models.student import Student
from ..models.admin import Admin


admin_bp = Blueprint('admin',__name__,url_prefix='/admin')
@admin_bp.route('/register', methods=['POST','GET'])
def register():
    key='admin@123'
    if request.method == 'POST':     
        email = request.form.get('email')
        password = request.form.get('password')
        secretkey = request.form.get('secretkey')

        if not password and not email:
            flash('you need to provide atleast email and password!', 'danger')
        user = db.session.query(Admin).first()
        if user:
            flash('admin account is already there and one account is allowed please login instead','warning')
            return redirect(url_for('admin.login'))

        if secretkey !=key:
            flash('you must provide right secret key','danger')
            return render_template('admin/formadmin.html')
        try:
            newuser = Admin(emaile=email,password=password,secretkey=secretkey)
            newuser.set_hashpassword(password)
            db.session.add(newuser)
            db.session.commit()
            flash('register in successfully as admin','success')
            return redirect(url_for('admin.login'))
        except IntegrityError:
            db.session.rollback()
            flash('user already exist please login!!', 'warning')
            return redirect(url_for('admin.login'))
        except Exception as e:
            db.session.rollback()
            flash(f'unexpected error occured : {e}','danger')
            return render_template('admin/formadmin.html')
        
    return render_template('admin/formadmin.html')



@admin_bp.route('/login',methods=['POST','GET'])
def login():
    key='admin@123'
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        secretkey = request.form.get('secretkey')

        if secretkey != key:
            flash('you must put admin secret key','danger')
            return render_template('admin/formadmin.html')
        

        if not email and not password:
            flash('please provide your email and password before proceeding!!','info')
            return render_template('admin/formadmin.html')
        user = db.session.query(Admin).filter_by(emaile=email).first()
        if user and user.check_password(password):
            session['user_id'] = user.adminid
            session['email']=user.emaile
            flash(f'logged in successfully as admin', 'success')
            return redirect(url_for('dash.dashboard'))
        flash('invalid email or password!! please check and try again!!','danger')
        return render_template('admin/formadmin.html')
    return render_template('admin/login.html')
@admin_bp.route('/logout')
def logout():
    session.pop('user_id',None)
    session.pop('email',None)
    flash('you have been logout successfully, you might want to login again','success')
    return redirect(url_for('userview.successdisplayall'))
