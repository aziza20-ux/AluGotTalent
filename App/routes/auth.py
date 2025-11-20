from flask import render_template, session,url_for,redirect, Blueprint,flash,request,g
from werkzeug.utils import secure_filename
from datetime   import datetime
import os
from extentions import db
from sqlalchemy.exc import IntegrityError
from ..models.user_model import User
from ..models.sponsor import Sponsor
from ..models.student import Student

auth_bp = Blueprint('auth',__name__,url_prefix='/auth')
@auth_bp.route('/register', methods=['POST','GET'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        emaile = request.form.get('email')
        phone = request.form.get('phone')
        password = request.form.get('password')
        role = request.form.get('role')

        if not password and not emaile:
            flash('you need to provide atleast email and password!', 'danger')
            return redirect(url_for('auth.login'))
        """
        user = db.session.query(User).filter_by(email=emaile)
        if user:
            flash('user already exist please login','warning')
            return redirect(url_for('auth.login'))
            """


        try:
            newuser = User(name=name,emaile=emaile,phone=phone,role=role)
            newuser.set_hashpassword(password)
            db.session.add(newuser)
            db.session.commit()

            flash('you have registered successfully please login!!','success')
            return redirect(url_for('auth.login'))
        except IntegrityError:
            db.session.rollback()
            flash('user already exist please login!!', 'warning')
            return redirect(url_for('auth.login'))
        except Exception as e:
            flash(f'unexpected error occured: {e}','danger')
            return redirect(url_for('auth.login'))
    return render_template('register.html')

@auth_bp.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if not email and not password:
            flash('please provide your email and password before proceeding!!','info')
            return render_template('login.html')
        user = db.session.query(User).filter_by(emaile=email).first()
        if user and user.check_password(password):
            session['user_id'] = user.userid
            session['email']=user.emaile
            flash(f'logged in successfully as {user.emaile}', 'success')
            return redirect(url_for('talent.display_all'))
        flash('invalid email or password!! please check and try again!!','danger')
        return render_template('login.html')
    return render_template('login.html')
@auth_bp.route('/logout')
def logout():
    session.pop('user_id',None)
    session.pop('email',None)
    flash('you have been logout successfully, you might want to login again','success')
    return redirect(url_for('userview.successdisplayall'))
