
import bson
import os

import pymongo
import dotenv


dotenv.load_dotenv()
#
client = pymongo.MongoClient(os.getenv('DATABASE_URL'),os.getenv('27017'))
db = client.api

class User:


    def __repr__(self):
        return f'Olá, me chamo {self.name}'

    @staticmethod
    def get_all_users():
        return [User(**u) for u in db.users.find()]
    

    @staticmethod
    def find_by_email(email):
        u = db.users.find_one({'email':email})
        return User(**u) if u else None
    
    @staticmethod
    def find_by_id(userid):
        u = db.users.find_one({'_id':bson.ObjectId(userid)})       
        return User(**u) if u else None
    
    @staticmethod
    def remove(userid):
        db.users.remove({"_id":bson.ObjectId(userid)})



    def __init__(self,*args, **kwargs):
        self._id = kwargs.get('_id')
        self.name = kwargs.get('name')
        self.email = kwargs.get('email')
        self.password = kwargs.get('password')


    def to_json(self):
        return {  
            'id':str(self._id),      
            'name':self.name,
            'email':self.email,
        }
    

    def save(self):
        query = {'email':self.email}
        if self._id:
            query = {'_id':self._id}

        db.users.update(query, {
            'name':self.name,
            'email':self.email,
            'password':self.password
        }, upsert=True)




if __name__ == '__main__':
    users = User.get_all_users() 
    print(users)
    users = [u.to_json() for u in users]
    print(users)
    users.find_by_email()
