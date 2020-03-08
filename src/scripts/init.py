
import os
from pathlib import Path

import bcrypt

from src.api.models import (
    db,
    User,
    Course,
    Score,
)


def hash_pw(pw):
    pw_hash = bcrypt.hashpw(pw.encode('utf8'), bcrypt.gensalt())
    return pw_hash


def init_db(db_file):
    db_dir = os.path.dirname(db_file)
    if not os.path.exists(db_dir):
        Path(db_dir).mkdir(parents=True, exist_ok=True)

    db.init(db_file)
    db.connect()
    db.create_tables([User, Course, Score])

    user = list(User.select())
    if not user:
        user = User.create(username='student', password=hash_pw('student'))
        course = Course.create(name='Java')
        score = Score.create(user_id=user.id, course_id=course.id, value=100)
