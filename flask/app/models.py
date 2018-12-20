from app import db


class Note (db.Model):
    noteId = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), index=True)
    content = db.Column(db.String(250), index=True)
    status = db.Column(db.Boolean,default=False)
    date = db.Column(db.Date)
    def __repr__(self):
        return  self.content + ' ' + self.stauts + 
        		' ' + self.date+ ' ' + self.title

 