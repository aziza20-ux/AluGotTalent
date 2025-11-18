from flask import render_template, session,url_for,jsonify,redirect, Blueprint,flash,request,g
from extentions import db
from datetime import datetime
from ..models.competitions import Comp

comp_bp = Blueprint('compe',__name__, url_prefix='/comp')

@comp_bp.route('/addcomp',methods=['POST','GET'])
def add_comp():
    if request.method == 'POST':
        title=request.form.get('title')
        details = request.form.get('details')
        category = request.form.get('category')
        deadline= request.form.get('deadline')
        try:
            parse_date = datetime.strptime(deadline, '%Y-%m-%d').date()
        except ValueError:
            flash('invalid format!!','danger')
            return redirect(url_for('compe.display_all_comp'))
        try:       
            newcomp = Comp(compdetails=details,deadline=parse_date,category=category,title=title)
            db.session.add(newcomp)
            db.session.commit()
            flash('competitions added successfully','success')
            return redirect(url_for('compe.display_all_comp'))
        except Exception as e:
            flash(f'unexpected error occured: {e}')
            db.session.rollback()
    return render_template('competitions.html')
@comp_bp.route('/editcomp/<int:id>',methods=['POST'])
def edit_comp(id):
    changes = request.form
    comp = db.session.query(Comp).filter_by(compid=id).first()

    if not comp:
        flash('competition not found', 'warning')
        return redirect(url_for('compe.display_all_comp')) #the redirect for route which display all competitions

    if not changes:
        flash('No changes submitted', 'info')
        return redirect(url_for('compe.display_all_comp'))#the redirect for route which display all competitions

    try:
        changes_made = False

        for k, v in changes.items():
            if not v:  # skip empty fields
                continue

            
            elif k in comp.__table__.columns.keys():
                setattr(comp, k, v)
                changes_made = True
            else:
                flash(f'Unknown field: {k}', 'danger')

        if changes_made:
            db.session.commit()
            flash('competition updated successfully!', 'success')
            return redirect(url_for('compe.display_all_comp'))
        else:
            flash('No valid changes detected', 'info')
            return redirect(url_for('compe.display_all_comp'))


    except Exception as e:
        db.session.rollback()
        flash(f'Unexpected error occurred: {e}', 'danger')

        return redirect(url_for('compe.display_all_comp'))#the redirect for route which display all competitions
@comp_bp.route('/deletecomp/<int:id>',methods=['DELETE'])
def delete_comp(id):
    comp = db.session.query(Comp).filter_by(compid=id).first()

    if not comp:
        flash('this competition no longer exists, refresh the page if this issue persists','danger')
        return redirect(url_for('compe.display_all_comp'))#the redirect for route which display all competitions
    try:
        db.session.delete(comp)
        db.session.commit()
        return redirect(url_for('compe.display_all_comp'))
    except Exception as e:
        db.session.rollback()
        flash(f'unexpected error occured: {e}')
        return redirect(url_for('compe.display_all_comp'))
        
@comp_bp.route('/displayallcomp',methods=['GET'])
def display_all_comp():
    all_comp = db.session.query(Comp).all()
    total=len(all_comp)
    return render_template('admin/competitions.html',all_comp=all_comp,total=total)



