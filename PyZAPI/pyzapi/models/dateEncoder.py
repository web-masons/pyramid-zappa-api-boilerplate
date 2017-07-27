from sqlalchemy import (
    Column,
    Boolean,
    DateTime,
    Integer,
    Text,
    Sequence,
    )

from ..util.jsonhelpers import RenderSchema
from .meta import Base
from .meta import DBSession

def get_nextautoincrement():
   try:
    cursor = DBSession.execute( "SELECT id from users ORDER BY id DESC LIMIT 1;" )
    row = cursor.fetchone()
    cursor.close()
    return row[0] + 1
   except:
    return 1

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(Text)
    last_name = Column(Text)
    created_at = Column(DateTime)

    def __init__(self, first_name, last_name, created_at):
        self.id = get_nextautoincrement()
        self.first_name = first_name
        self.last_name = last_name
        self.created_at = created_at

class UserSchema(RenderSchema):
    class Meta:
        fields = ("id", "first_name", "last_name", "created_at")