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
        email = request.form.get('email')
        phone = request.form.get('phone')
        password = request.form.get('password')
        role = request.form.get('role')

        if not password and not email:
            flash('you need to provide atleast email and password!', 'danger')

        if not role:
            flash('you need to provide a role','danger')
            return render_template('register.html')
        try:
            newuser = User(name=name,email=email,phone=phone,role=role)
            newuser.set_hashpassword(password)
            db.session.add(newuser)
            db.session.commit()
            if role == 'student':
                return render_template('additional_details.html')
            if role == 'sponsor':

                flash('you have registered successfully please login!!','success')
                return redirect(url_for('auth.login'))
        except IntegrityError:
            db.session.rollback()
            flash('user already exist please login!!', 'warning')
        except Exception as e:
            flash(f'unexpected error occured: {e}','danger')
    return render_template('register.html')
@auth_bp.route('/additional_details', methods=['POST','GET'])
def additional_details():
    if request.method == 'POST':
        school = request.form.get('school')
        gradelevel = request.form.get('gradelevel')
        date = request.form.get('date')
        picture = request.files['file']
        path_of_picture = None
        try:
            parse_date = datetime.strptime(date, '%Y-%m-%d').date()
        except ValueError:
            flash('invalid format!!','danger')
            return redirect(url_for('auth.additional_details'))
        if picture and picture.filename != '':
            UPLOADS_FOLDER = 'uploads'
            os.makedirs(UPLOADS_FOLDER,exist_ok=True)
            safefilename = secure_filename(picture.filename)
            picture.save(os.path.join(UPLOADS_FOLDER, safefilename))
            path_of_picture = os.path.join(UPLOADS_FOLDER, safefilename)
       
        else:

            flash('profile picture is recommended','warning')

        newprofile = Student(school=school,gradelevel=gradelevel,dateofbirth=parse_date,picture=path_of_picture)

        newprofile.userid = g.user_id

        db.session.add(newprofile)
        db.session.commit()
        flash('additional details added. login to access application', 'info')
        return redirect(url_for('auth.login'))
    return render_template('additional_details.html')

@auth_bp.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if not email and not password:
            flash('please provide your email and password before proceeding!!','info')
            return render_template('login.html')
        user = db.session.query(User).filter_by(email=email).first()
        if user and user.check_password(password):
            session['user_id'] = user.userid
            session['email']=user.email
            flash(f'logged in successfully as {user.email}', 'success')
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
