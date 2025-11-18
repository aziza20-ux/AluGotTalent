from extentions import db
from werkzeug.security import check_password_hash, generate_password_hash

class User(db.Model):
    __tablename__ = 'users'
    userid = db.Column(db.Integer, primary_key = True,autoincrement=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    phone = db.Column(db.Integer)
    password = db.Column(db.String(255))
    role = db.Column(db.String(50))

    student = db.relationship('Student', back_populates= 'user', uselist=False)
    #sponsor = db.relationship('Sponsor', back_populates= 'user')

    def set_hashpassword(self, password):
        self.password = generate_password_hash(password)
    def check_password(self, entered_password):
        return check_password_hash(self.password, entered_password)


