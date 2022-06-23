from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class User (db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    favoritos = relationship('Favorito', backref='user', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "favoritos": self.favoritos
        }



class Characters (db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    gender = Column(String(50))
    eyesColor = Column(String(50))
    hairColor = Column(String(50))
    height = Column(Integer)
    skinColor = Column(String(50), nullable=False)
    favoritos = relationship('Favorito', backref='characters', lazy=True)

    def __repr__(self):
        return '<Characters %r>' % self.characters

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "favoritos": self.favoritos
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "eyesColor": self.eyesColor,
            "hairColor": self.hairColor,
            "height": self.height,
            "skinColor": self.skinColor,
            "favoritos": self.favoritos
        }


class Planets(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    population = Column(String(250))
    terrain = Column(String(250), nullable=False)
    climate = Column(Integer)
    orbitalPeriod = Column(Integer)
    rotationPeriod = Column(Integer)
    diameter = Column(Integer)
    favoritos = relationship('Favorito', backref='planets', lazy=True)

    def __repr__(self):
        return '<Planets %r>' % self.planets

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
            "terrain": self.terrain,
            "climate": self.climate,
            "orbitalPeriod": self.orbitalPeriod,
            "rotationPeriod": self.rotationPeriod,
            "diameter": self.diameter,
            "favoritos": self.favoritos
        }


class Favs(Base):
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('characters.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))


    def to_dict(self):
        return {}

    def __repr__(self):
        return '<Favs %r>' % self.favs

    def serialize(self):
        return {
            "id": self.id,
            "person_id": self.person_id,
            "character_id": self.character_id,
            "planets_id": self.planets_id
        }