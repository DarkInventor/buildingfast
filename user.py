from firebase_admin import firestore
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id_, name, email, profile_pic, is_active=True):
        self.id = id_
        self.name = name
        self.email = email
        self.profile_pic = profile_pic
        self.is_active = is_active
        
    def get_id(self):
        return str(self.id)

    def is_active(self, value):
        self._is_active = value
        
    @staticmethod
    def get(user_id):
        db = firestore.client()
        user_ref = db.collection('users').document(user_id)
        user = user_ref.get()
        if user.exists:
            user_data = user.to_dict()
            return User(user_data['id'], user_data['name'], user_data['email'], user_data['profile_pic'])
        else:
            return None

    @staticmethod
    def create(id_, name, email, profile_pic):
        db = firestore.client()
        user_ref = db.collection('users').document(id_)
        user_ref.set({
            'id': id_,
            'name': name,
            'email': email,
            'profile_pic': profile_pic
        })
