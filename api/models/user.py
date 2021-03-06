from api.config.database import db

class User(db.Document):
    name = db.StringField(required=True)
    email = db.StringField(required=True, unique=True)
    password = db.StringField(required= True, unique=True)

    def to_json():
        return {
                name: self.name,
                email: self.email
            }

