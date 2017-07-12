from config.DBConfig import mongoDB


def getAppUserList():
    output = []
    for q in mongoDB.db.AppUser.find():
        output.append({'firstName': q['firstName'], 'lastName': q['lastName']})
    return output


def getOneAppUserByName(name):
    q = mongoDB.db.AppUser.find_one_or_404({'firstName': name})
    output = {'firstName': q['firstName'], 'lastName': q['lastName']}
    return output


def createNewAppUser(appUser):
    app_user_id = mongoDB.db.AppUser.insert(appUser)
    q = mongoDB.db.AppUser.find_one_or_404({'_id': app_user_id})
    output = {'firstName': q['firstName'], 'lastName': q['lastName']}
    return output
