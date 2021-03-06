import time
import jwt
import os
import logging

secret_key = 'FLASK_SECRET_KEY'
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="/tmp/flsk.log", level=logging.DEBUG, format=LOG_FORMAT)
logger = logging.getLogger()


def current_milli_time():
    return int(round(time.time() * 1000))


def two_day_after_milli_time():
    # 2days = 172800000 ms
    logger.debug("2 days from now")
    return current_milli_time() + 172800000


def encode_auth_token():
    env_secret = os.getenv(secret_key, '1234')
    if env_secret == '':
        return False, "Server error env_secret"
    encoded = jwt.encode(
        {
            'exp': two_day_after_milli_time()
        },
        env_secret, algorithm='HS256')
    return True, encoded.decode('utf8')


def decode_auth_token(auth_token):
    from service.TokenBlackListService import TokenBlackListService
    """
    Validates the auth token
    :param auth_token:
    :return: integer|string
    """
    env_secret = os.getenv(secret_key, '1234')
    if env_secret == '':
        return False, "Server Error, env_secret"
    try:
        payload = jwt.decode(auth_token, env_secret)
        is_blacklisted_token = TokenBlackListService.isBlackListed(auth_token)
        if is_blacklisted_token:
            return False, 'Token blacklisted. Please log in again.'
        else:
            return True, payload['exp']
    except jwt.ExpiredSignatureError:
        return False, 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return False, 'Invalid token. Please log in again.'
