from api.config.database import db

class Player(db.Document):
    firstname = db.StringField(required=True)
    lastname = db.StringField(required=True)
    email = db.StringField(required=True, unique=True)
    nickname = db.StringField(required= True, unique=True)
    fornite_nickname = db.StringField(required=True)
    clash_royal_player_tag = db.StringField(required=True)
    active = db.BooleanField(required=True, default=False)
    stats = db.ListField()

    def to_json():
        return {
                firstname: self.firstname,
                lastname: self.lastname,
                email: self.email,
                nickname: self.nickname,
                fornite_nickname: self.fornite_nickname,
                clash_royal_player_tag: self.clash_royal_player_tag,
                active: self.active,
                stats: self.stats
            }

