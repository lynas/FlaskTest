from config.DBConfig import mongoDB
from schema.AppUser import AppUser
from bson.objectid import ObjectId


class AppUserService:
    @staticmethod
    def getAll():
        output = []
        for q in mongoDB.db.AppUser.find():
            data, errors = AppUser().load(q)
            data['_id'] = str(q['_id'])
            output.append(data)
        return output

    @staticmethod
    def getOneAppUserByName(name):
        q = mongoDB.db.AppUser.find_one_or_404({'firstName': name})
        data, errors = AppUser().load(q)
        data['_id'] = str(q['_id'])
        return data

    @staticmethod
    def createNewAppUser(appUser):
        app_user_id = mongoDB.db.AppUser.insert(appUser)
        q = mongoDB.db.AppUser.find_one_or_404({'_id': app_user_id})
        data, errors = AppUser().load(q)
        return data

    @staticmethod
    def updateAppUser(appUserId, updatedAppUser):
        mongoDB.db.AppUser.find_one_or_404({'_id': ObjectId(appUserId)})
        mongoDB.db.AppUser.update_one({'_id': ObjectId(appUserId)}, {"$set": updatedAppUser}, upsert=False)
        q_res = mongoDB.db.AppUser.find_one_or_404({'_id': ObjectId(appUserId)})
        data, errors = AppUser().load(q_res)
        return data

    @staticmethod
    def delete(appUserId):
        mongoDB.db.AppUser.find_one_or_404({'_id': ObjectId(appUserId)})
        mongoDB.db.AppUser.delete_one({'_id': ObjectId(appUserId)})
        return {"delete": "success"}
