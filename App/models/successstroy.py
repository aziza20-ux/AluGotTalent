from extentions import db

class Story(db.Model):
    __tablename__='stories'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title=db.Column(db.String(255))
    description = db.Column(db.String(255))
    media_url = db.Column(db.String(255))
