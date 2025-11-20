from extentions import db
from .user_model import User

class Student(User):
    __tablename__='students'
    userid = db.Column(db.Integer, db.ForeignKey('users.userid'),primary_key=True)
    dateofbirth = db.Column(db.DateTime)
    gradelevel = db.Column(db.Integer)
    school = db.Column(db.String(50))
    #talentid = db.Column(db.Integer, db.ForeignKey('talents.talentid'),primary_key=True)

    user = db.relationship('User', back_populates= 'student')
    talents = db.relationship(
        'Talent', 
        # The FK is in the Talent table, linking back to the Student's userid
        back_populates='student', 
        lazy=True,
        # The 'primaryjoin' might be necessary here for joined inheritance, but 
        # let's try 'backref' first for simplicity.
    )



