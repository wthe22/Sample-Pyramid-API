
from peewee import *


db = SqliteDatabase(None)


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    id = AutoField(primary_key=True)
    username = CharField(unique=True)
    password = CharField()


class Course(BaseModel):
    id = AutoField(primary_key=True)
    name = CharField(unique=True)


class Score(BaseModel):
    user = ForeignKeyField(User, on_delete='CASCADE')
    course = ForeignKeyField(Course, on_delete='CASCADE')
    value = IntegerField()

    class Meta:
        primary_key = CompositeKey('user', 'course')
