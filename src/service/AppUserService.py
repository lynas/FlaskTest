from config.DBConfig import mongoDB


def getAppUserList():
    output = []
    for q in mongoDB.db.AppUser.find():
        output.append({'firstName': q['firstName'], 'lastName': q['lastName']})
    return output
