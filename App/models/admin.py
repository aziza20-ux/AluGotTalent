from extentions import db
from werkzeug.security import check_password_hash, generate_password_hash

class Admin(db.Model):
    __tablename__ = 'admin'
    adminid = db.Column(db.Integer, primary_key = True,autoincrement=True)
    email = db.Column(db.String(50))
    password = db.Column(db.String(255))
    secretkey = db.Column(db.String(50))

   
    #sponsor = db.relationship('Sponsor', back_populates= 'user')

    def set_hashpassword(self, password):
        self.password = generate_password_hash(password)
    def check_password(self, entered_password):
        return check_password_hash(self.password, entered_password)