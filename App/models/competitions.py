from extentions import db

class Comp(db.Model):
    __tablename__='comps'
    compid = db.Column(db.Integer,primary_key=True, autoincrement=True)
    category = db.Column(db.String(225))
    deadline = db.Column(db.DateTime)
    compdetails = db.Column(db.String(255))
    appylink=db.Column(db.String(255))
    title=db.Column(db.String(255))