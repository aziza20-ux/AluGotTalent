from flask import render_template, current_app, session,url_for,jsonify,redirect, Blueprint,flash,request,g
from extentions import db
from werkzeug.utils import secure_filename
import re
import os
from ..models.user_model import User
from ..models.sponsor import Sponsor
from ..models.student import Student
from ..models.talents import Talent
from ..models.successstroy import Story
from ..utils.convert_url import convert_to_embed_url


success_bp = Blueprint('success',__name__, url_prefix='/success')

@success_bp.route('/addsuccess', methods=['POST','GET']) #done
def add_success():
    title = request.form.get('title')
    successditails = request.form.get('details')
    media_url_file = request.form.get('file') # Renamed to avoid confusion with the attribute later
    
    # 1. Initialize the path variable with a default value (e.g., None)
    path_of_picture = None 

    # Look up existing story using the file data/URL provided
    # Note: If the file input is not a file object, this check might be problematic. 
    # Assuming 'media_url' is the unique identifier.
    talent = db.session.query(Story).filter_by(media_url=media_url_file).first()

    if talent:
        db.session.rollback()
        flash('success story already exists!','warning')
        return redirect(url_for('success.displayall'))
        
    # Check if the input is a file (using request.files if it's an actual file upload)
    # If the form input 'file' is intended for a URL, this logic needs adjustment. 
    # Assuming 'file' is a file upload field:
    if 'file' in request.files and request.files['file'].filename != '':
        media_url_file = request.files['file'] # Get the actual FileStorage object

        # 1. Define the name of the folder inside 'static'
        UPLOADS_DIR_NAME = 'videos'
        
        # 2. Get the ABSOLUTE path: /path/to/project/static/videos
        full_uploads_path = os.path.join(current_app.static_folder, UPLOADS_DIR_NAME)
        
        # 3. Create the directory if it doesn't exist
        os.makedirs(full_uploads_path, exist_ok=True)
        
        safefilename = secure_filename(media_url_file.filename)
        
        # 4. Save the file using the FULL absolute path
        media_url_file.save(os.path.join(full_uploads_path, safefilename))
        
        # 5. Store the path RELATIVE to the 'static' folder (for the database)
        path_of_picture = os.path.join(UPLOADS_DIR_NAME, safefilename).replace(os.path.sep, '/')
    
    # If it's not a file upload, use the direct URL from the form (if provided)
    elif media_url_file:
         path_of_picture = media_url_file # This assumes a raw URL (like a YouTube link) was input

    try:
        # Use the variable path_of_picture, which is now guaranteed to exist
        newsuccess = Story(title=title, description=successditails, media_url=path_of_picture)
        #newsuccess.userid = g.user_id
        db.session.add(newsuccess)
        db.session.commit()
        flash('success story added successfully!!','success')
        return redirect(url_for('success.displayall'))
    except Exception as e:
        flash(f'unexpected error occured: {e}', 'danger')
        return redirect(url_for('success.displayall'))
@success_bp.route('/delete/<int:id>',methods=['DELETE']) #done
def delete_talent(id):
    talent = db.session.query(Story).filter(Story.id==id).first()
    try:
        if talent:
            db.session.delete(talent)
            db.session.commit()
            flash('success deleted successfully' 'success')
            return redirect(url_for('success.displayall'))
    except Exception as e:
        db.session.rollback()
        flash(f'unexpected error occured!!: {e}','danger')
        return redirect(url_for('success.displayall'))
@success_bp.route('/displayall',methods=['GET'])
def displayall():
    all_sponso = db.session.query(Story).all()
    return render_template('admin/success.html',all_sponso=all_sponso)
    