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
