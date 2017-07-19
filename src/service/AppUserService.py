from schema.AppUser import AppUser
from bson.objectid import ObjectId


class AppUserService:
    @staticmethod
    def getAll():
        from main import dbCon
        output = []
        for q in dbCon.db.AppUser.find():
            data, errors = AppUser().load(q)
            data['_id'] = str(q['_id'])
            output.append(data)
        return output

    @staticmethod
    def getOneAppUserByName(name):
        from main import dbCon
        q = dbCon.db.AppUser.find_one_or_404({'firstName': name})
        data, errors = AppUser().load(q)
        data['_id'] = str(q['_id'])
        return data

    @staticmethod
    def createNewAppUser(appUser):
        from main import dbCon
        app_user_id = dbCon.db.AppUser.insert(appUser)
        q = dbCon.db.AppUser.find_one_or_404({'_id': app_user_id})
        data, errors = AppUser().load(q)
        return data

    @staticmethod
    def updateAppUser(appUserId, updatedAppUser):
        from main import dbCon
        dbCon.db.AppUser.find_one_or_404({'_id': ObjectId(appUserId)})
        dbCon.db.AppUser.update_one({'_id': ObjectId(appUserId)}, {"$set": updatedAppUser}, upsert=False)
        q_res = dbCon.db.AppUser.find_one_or_404({'_id': ObjectId(appUserId)})
        data, errors = AppUser().load(q_res)
        return data

    @staticmethod
    def delete(appUserId):
        from main import dbCon
        dbCon.db.AppUser.find_one_or_404({'_id': ObjectId(appUserId)})
        dbCon.db.AppUser.delete_one({'_id': ObjectId(appUserId)})
        return {"delete": "success"}
