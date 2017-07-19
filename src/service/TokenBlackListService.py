

class TokenBlackListService:
    @staticmethod
    def isBlackListed(token):
        from main import dbCon
        q = dbCon.db.TokenBlackList.find_one({'token': token})
        if q is None:
            return False
        else:
            return True

    @staticmethod
    def addToTokenBlackList(token):
        from main import dbCon
        dbCon.db.TokenBlackList.insert({"token": token})
