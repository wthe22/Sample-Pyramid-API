import bcrypt

from src.api.models import User


def check_credentials(username, password):
    user = User.select().where(User.username == username)

    if not len(user) == 1:
        return

    user = user[0]
    expected_hash = user.password
    password = password.encode('utf8')
    expected_hash = expected_hash.encode('utf8')
    valid = bcrypt.checkpw(password, expected_hash)

    if valid:
        user_id = user.id
    else:
        user_id = None
    return user_id


def get_group(username, request):
    return []
