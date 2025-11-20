from extentions import db

class Talent(db.Model):
    __tablename__='talents'
    userid = db.Column(db.Integer, db.ForeignKey('users.userid'))
    talentid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    talentname = db.Column(db.String(255))
    talentdetails = db.Column(db.String(500))
    talent_url = db.Column(db.String(255))
    category = db.Column(db.String(255))
    email=db.Column(db.String(255))
    phone=db.Column(db.String(255))
    tiktok=db.Column(db.String(300))
    inst=db.Column(db.String(300))
    facebook=db.Column(db.String(300))

    student = db.relationship('Student', back_populates='talents', lazy=True)
   

    def to_dict(self):

        return {
            'talentname':self.talentname,
            'talentdetails':self.talentdetails,
            'talent_url':self.talent_url,
            'category':self.category
        }



