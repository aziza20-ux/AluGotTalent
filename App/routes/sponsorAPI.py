from flask import render_template, session, current_app, url_for,jsonify,redirect, Blueprint,flash,request,g
from extentions import db
import re
from werkzeug.utils import secure_filename
import os 
from ..models.user_model import User
from ..models.sponsor import Sponsor
from ..models.student import Student
from ..models.talents import Talent
#from ..utils.convert_url import convert_to_embed_url


sponsor_bp = Blueprint('sponsor',__name__, url_prefix='/sponsor')

@sponsor_bp.route('/addsponsor', methods=['POST','GET']) #done
def add_sponsor():
    name = request.form.get('name')
    companyname=request.form.get('company_name')
    sponsoredtalents=request.form.get('sponsoredtalents')
    address=request.form.get('address')
    linkedin=request.form.get('linkedIn')
    email=request.form.get('email_addres')
    category=request.form.get('category')
    companylogo=request.files['file']
    path_of_picture = None

    sponsor = db.session.query(Sponsor).filter_by(email_addres=email).first()

    if sponsor:
        flash('sponsor already exists!','warning')
        db.session.rollback()
        return redirect(url_for('sponsor.displayall'))
        
    if companylogo and companylogo.filename != '':
        
        # 1. Define the name of the folder inside 'static'
        UPLOADS_DIR_NAME = 'uploads'
        
        # 2. Get the ABSOLUTE path: /path/to/project/static/uploads
        full_uploads_path = os.path.join(current_app.static_folder, UPLOADS_DIR_NAME)
        
        # 3. Create the directory if it doesn't exist
        os.makedirs(full_uploads_path, exist_ok=True)
        
        safefilename = secure_filename(companylogo.filename)
        
        # 4. Save the file using the FULL absolute path
        companylogo.save(os.path.join(full_uploads_path, safefilename))
        
        # 5. Store the path RELATIVE to the 'static' folder (for the database)
        # Ensure forward slashes for web compatibility
        path_of_picture = os.path.join(UPLOADS_DIR_NAME, safefilename).replace(os.path.sep, '/')

    else:
        flash('profile picture is recommended','warning')
        
    try:
        newsponsor = Sponsor(name=name,company_name=companyname,address=address,email_addres=email,sponsoredtalents=sponsoredtalents,linkedIn=linkedin,
                             companylogo=path_of_picture,category=category)
        db.session.add(newsponsor)
        db.session.commit()
        flash('sponsor added successfully!!','success')
        return redirect(url_for('sponsor.displayall'))
    except Exception as e:
        flash(f'unexpected error occured: {e}', 'danger')
        db.session.rollback() # Important to rollback on failure
        return redirect(url_for('sponsor.displayall'))
    
@sponsor_bp.route('/delete/<int:id>',methods=['DELETE']) #done
def delete_sponsor(id):
    sponsor = db.session.query(Sponsor).filter(Sponsor.sponsorid==id).first()
    try:
        if sponsor:
            db.session.delete(sponsor)
            db.session.commit()
            flash('sponsor deleted successfully' 'success')
            return redirect(url_for('sponsor.displayall'))
    except Exception as e:
        db.session.rollback()
        flash(f'unexpected error occured!!: {e}','danger')
        return redirect(url_for('sponsor.displayall'))
@sponsor_bp.route('/edit/<int:id>', methods=['POST'])
def edit_sponsor(id):
    changes = request.form
    sponsor = db.session.query(Sponsor).filter_by(sponsorid=id).first()

    if not sponsor:
        flash('sponsor not found', 'warning')
        return redirect(url_for('sponsor.displayall'))

    if not changes:
        flash('No changes submitted', 'info')
        return redirect(url_for('sponsor.displayall'))

    try:
        changes_made = False

        for k, v in changes.items():
            if not v:  # skip empty fields
                continue

            # map form field names to model attributes if different

            elif k in sponsor.__table__.columns.keys():
                setattr(sponsor, k, v)
                changes_made = True
            else:
                flash(f'Unknown field: {k}', 'danger')

        if changes_made:
            db.session.commit()
            flash('sponsor updated successfully!', 'success')
            return redirect(url_for('sponsor.displayall'))
        else:
            flash('No valid changes detected', 'info')
            return redirect(url_for('sponsor.displayall'))

    except Exception as e:
        db.session.rollback()
        flash(f'Unexpected error occurred: {e}', 'danger')
        return redirect(url_for('sponsor.displayall'))

@sponsor_bp.route('/displayall',methods=['GET'])
def displayall():
    all_sponsor = db.session.query(Sponsor).all()
    return render_template('admin/sponsors.html',all_sponsor=all_sponsor)




    
    
