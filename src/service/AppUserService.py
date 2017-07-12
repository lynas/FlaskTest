from config.DBConfig import mongoDB
from schema.AppUser import AppUser


def getAppUserList():
    output = []
    for q in mongoDB.db.AppUser.find():
        data, errors = AppUser().load(q)
        data['_id'] = str(q['_id'])
        output.append(data)
    return output


def getOneAppUserByName(name):
    q = mongoDB.db.AppUser.find_one_or_404({'firstName': name})
    data, errors = AppUser().load(q)
    data['_id'] = str(q['_id'])
    return data


def createNewAppUser(appUser):
    app_user_id = mongoDB.db.AppUser.insert(appUser)
    q = mongoDB.db.AppUser.find_one_or_404({'_id': app_user_id})
    data, errors = AppUser().load(q)
    return data
