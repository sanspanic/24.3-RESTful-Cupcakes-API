"""Models for Cupcake app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app): 
    db.app = app
    db.init_app(app)

class Cupcake(db.Model): 
    """cupcake model"""

    __tablename__ = 'cupcakes'

    def __repr__(self): 
        c = self
        return f"<cupcake_id = {c.id}, flavour = {c.flavour}, size = {c.size}, rating={c.rating}, image={c.image}"

    id = db.Column(db.Integer, 
                    primary_key = True, 
                    autoincrement = True)

    flavour = db.Column(db.String, 
                        nullable = False)

    size = db.Column(db.String, 
                        nullable = False)
    
    rating = db.Column(db.Float, 
                        nullable = False)

    image = db.Column(db.String, 
                        nullable = True,
                        default='https://tinyurl.com/demo-cupcake')

    @property
    def full_name(self): 
        """returns string of full name"""
        full_name = f'{self.flavour} Cupcake'
        return full_name.capitalize()

    def serialize(self):
        """Serialize a SQLAlchemy obj to dictionary."""

        return {
            "id": self.id,
            "flavour": self.flavour,
            "size": self.size,
            "rating": self.rating, 
            "image": self.image
        }


        



