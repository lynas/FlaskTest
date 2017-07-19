from config.DBConfig import dbCon


class TokenBlackListService:
    @staticmethod
    def isBlackListed(token):
        q = dbCon.db.TokenBlackList.find_one({'token': token})
        if q is None:
            return False
        else:
            return True

    @staticmethod
    def addToTokenBlackList(token):
        dbCon.db.TokenBlackList.insert({"token": token})
