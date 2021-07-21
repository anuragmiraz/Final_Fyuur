from app import db

class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
# My change starts
    genres = db.Column(db.String(120))
    website_link = db.Column(db.String(500))
    seeking_talent = db.Column(db.String(), nullable = False, default = 'N')
    seeking_description  = db.Column(db.String(500))
    venue_id = db.relationship('Shows', backref='Venue', lazy=True)
# My change ends

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
# My change starts
    website_link = db.Column(db.String(500))
    seeking_venue = db.Column(db.String(), nullable = False, default = 'N')
    seeking_description  = db.Column(db.String(500))
    artist_id = db.relationship('Shows', backref='Artist', lazy=True)
# My change ends

# My change starts
class Shows(db.Model):
    __tablename__ = 'Shows'

    id = db.Column(db.Integer, primary_key=True)
    venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'), nullable=False)
#    venue_name = db.Column(db.String)
    artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'), nullable=False)
#    artist_name = db.Column(db.String)
    start_time = db.Column(db.DateTime(), nullable=False)
# My change ends

