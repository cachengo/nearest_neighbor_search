from app import db


class Vector(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vector = db.Column(db.PickleType())

    def __repr__(self):
        return '<Vector {}>'.format(self.id)
