from extentions import db
from .user_model import User

class Sponsor(db.Model):
    __tablename__ = 'sponsors'
    #userid = db.Column(db.Integer, db.ForeignKey('users.userid'))
    sponsorid=db.Column(db.Integer, primary_key=True, autoincrement=True)
    name=db.Column(db.String(50))
    sponsoredtalents = db.Column(db.String(500))
    address = db.Column(db.String)
    company_name = db.Column(db.String(100))
    linkedIn=db.Column(db.String(100))
    email_addres=db.Column(db.String(50))
    category=db.Column(db.String(255))
    companylogo=db.Column(db.String(300))
    
    #user = db.relationship('User', back_populates= 'sponsor')
    def __init__(self,**kwargs):
        super().__init__(**kwargs)