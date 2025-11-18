from flask import render_template, session,url_for,jsonify,redirect, Blueprint,flash,request,g
from extentions import db
import re
from ..models.user_model import User
from ..models.sponsor import Sponsor
from ..models.student import Student
from ..models.talents import Talent
from ..utils.convert_url import convert_to_embed_url


talent_bp = Blueprint('talent',__name__, url_prefix='/talent')

@talent_bp.route('/addtalent', methods=['POST','GET']) #done
def add_talent():
    talentname = request.form.get('talentname')
    talentditails = request.form.get('details')
    talent_url = request.form.get('url')
    talentcategory = request.form.get('category')

    
   
    embeded_url = convert_to_embed_url(talent_url)

    talent = db.session.query(Talent).filter_by(talent_url=embeded_url).first()

    if talent:
        flash('talent already exists!','warning')
        db.session.rollback()
    try:
        newtalent = Talent(talentname=talentname,talentdetails=talentditails,talent_url=embeded_url,category=talentcategory)
        newtalent.userid = g.user_id
        db.session.add(newtalent)
        db.session.commit()
        flash('talent added successfully!!','success')
        return redirect(url_for('talent.mytalents'))
    except Exception as e:
        flash(f'unexpected error occured: {e}', 'danger')
        return redirect(url_for('talent.mytalents'))
    
@talent_bp.route('/delete/<int:id>',methods=['DELETE']) #done
def delete_talent(id):
    talent = db.session.query(Talent).filter(Talent.talentid==id).first()
    try:
        if talent:
            db.session.delete(talent)
            db.session.commit()
            flash('talent deleted successfully' 'success')
            return redirect(url_for('talent.mytalents'))
    except Exception as e:
        db.session.rollback()
        flash(f'unexpected error occured!!: {e}','danger')
@talent_bp.route('/edit/<int:id>', methods=['POST'])
def edit_talent(id):
    changes = request.form
    talent = db.session.query(Talent).filter_by(talentid=id).first()

    if not talent:
        flash('Talent not found', 'warning')
        return redirect(url_for('talent.mytalents'))

    if not changes:
        flash('No changes submitted', 'info')
        return redirect(url_for('talent.mytalents'))

    try:
        changes_made = False

        for k, v in changes.items():
            if not v:  # skip empty fields
                continue

            # map form field names to model attributes if different
            if k == 'url':
                embeded = convert_to_embed_url(v)
                setattr(talent, 'talent_url', embeded)
                changes_made = True
            elif k in talent.__table__.columns.keys():
                setattr(talent, k, v)
                changes_made = True
            else:
                flash(f'Unknown field: {k}', 'danger')

        if changes_made:
            db.session.commit()
            flash('Talent updated successfully!', 'success')
        else:
            flash('No valid changes detected', 'info')

    except Exception as e:
        db.session.rollback()
        flash(f'Unexpected error occurred: {e}', 'danger')

    return redirect(url_for('talent.mytalents'))

@talent_bp.route('/mytalents',methods=['GET'])
def mytalents():
    #all_talents = db.session.query(Talent).all()
    user_talent = db.session.query(Talent).filter(Talent.userid==g.user_id).all()
    #dict_talent = [talent.to_dict() for talent in all_talents]
    #dict= jsonify(dict_talent)
    if not user_talent:
        flash('NB:you need to add your talent to see them here!!', 'info')
    
    return render_template('my_talents.html',dict=user_talent)
@talent_bp.route('/displayall',methods=['GET'])
def display_all():
    all_talents = db.session.query(Talent).all()
    return render_template('all_tallents.html',dict=all_talents)
@talent_bp.route('/home',methods=['GET'])
def home():
    return render_template('home.html')





    
    
