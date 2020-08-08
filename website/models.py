from website import db

class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return f"Post: {self.title}, Posted By: {self.author}"