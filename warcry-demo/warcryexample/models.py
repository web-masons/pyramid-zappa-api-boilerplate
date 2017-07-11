from sqlalchemy import (
    Column,
    Boolean,
    DateTime,
    Integer,
    Text,
    Sequence,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension
from warcryexample.util.jsonhelpers import RenderSchema

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))


class Base(object):
    def __json__(self, request):
        json_exclude = getattr(self, '__json_exclude__', set())
        return {key: value for key, value in self.__dict__.items()
                # Do not serialize 'private' attributes
                # (SQLAlchemy-internal attributes are among those, too)
                if not key.startswith('_')
                and key not in json_exclude}

Base = declarative_base(cls=Base)

def get_nextautoincrement():
    cursor = DBSession.execute( "SELECT id from users ORDER BY id DESC LIMIT 1;" )
    row = cursor.fetchone()
    cursor.close()
    return row[0] + 1

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    #id = Column(Integer, nullable=False, unique=True, autoincrement=True)
    name = Column(Text)
    super_hero = Column(Boolean)
    created_at = Column(DateTime)
 
    def __init__(self, name, super_hero, created_at):
        self.id = get_nextautoincrement()
        self.name = name
        self.super_hero = super_hero
        self.created_at = created_at

class UserSchema(RenderSchema):
    class Meta:
        fields = ("id", "name", "super_hero", "created_at")
