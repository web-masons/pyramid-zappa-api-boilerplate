from pyramid.httpexceptions import HTTPOk
import transaction
import datetime
import random
import json
from json import JSONDecoder
from json import JSONEncoder
from datetime import datetime
from sqlalchemy import func
from sqlalchemy import desc
from pyramid.response import Response

from pyramid.view import view_config

from warcry_proj.models.mymodel import (
    DBSession,
    User,
    UserSchema,
    )

class DateTimeDecoder(json.JSONDecoder):
    def __init__(self, *args, **kargs):
        JSONDecoder.__init__(self, object_hook=self.dict_to_object,*args, **kargs)

    def dict_to_object(self, d):
        if '__type__' not in d:
            return d

        type = d.pop('__type__')
        try:
            dateobj = datetime(**d)
            return dateobj
        except:
            d['__type__'] = type
            return d

class DateTimeEncoder(JSONEncoder):
    """ Instead of letting the default encoder convert datetime to string,
        convert datetime objects into a dict, which can be decoded by the
        DateTimeDecoder
    """

    def default(self, obj):
        if isinstance(obj, datetime):
            return {
                '__type__' : 'datetime',
                'year' : obj.year,
                'month' : obj.month,
                'day' : obj.day,
                'hour' : obj.hour,
                'minute' : obj.minute,
                'second' : obj.second,
                'microsecond' : obj.microsecond,
            }
        else:
            return JSONEncoder.default(self, obj)

#Get a list of all Users in Database
@view_config(route_name='all_users', request_method='GET', renderer='json')
def get_all_users(_):
    schema = UserSchema(many=True)
    return schema.dumps(DBSession.query(User).all(), cls=DateTimeEncoder)

#Get a single user by specifying the user ID
@view_config(route_name='single_user', request_method='GET', renderer='json')
def get_single_user(request):
    user_id = request.matchdict.get('user_id')
    if user_id == '__first__':
        user_id = UserSchema().dumps(DBSession.query(User).get(1), cls=DateTimeEncoder)
        user_id = UserSchema().dumps(DBSession.query(User).get(1)).id

    user = UserSchema().dumps(DBSession.query(User).get(user_id), cls=DateTimeEncoder)
    if not user:
        msg = "The User with id '{}' was not found.".format(user_id)
        return Response(status=404, json_body={'error': msg})

    return user

#Create / Insert a User
@view_config(route_name='create_new_user', request_method='POST', renderer='json')
def create_user(request):
     data = request.json_body
     schema = UserSchema()
     json_dict = schema.load(data).data
     entered_name = json_dict["name"]
     #Super Hero
     superHero = json_dict["super_hero"] if json_dict.get("super_hero") else False
     #Created At
     createdAt = json_dict["created_at"] if json_dict.get("created_at") else datetime.now()
     #super_hero = int(json_dict["super_hero"])
     #createdAt = json_dict["created_at"]
     #Get Record With Max Record ID in Database
     #current_user_from_db = DBSession().query(User).order_by(User.id.desc()).first()
     #user = User(name='Bruce Wayne1', super_hero=True, created_at=datetime.now())
     #user = User(name=entered_name, super_hero=superHero, created_at=createdAt)
     #DBSession.add(user)
     # Flush to get the post.id from the database
     #DBSession.flush()
     #DBSession.commit()
     with transaction.manager:
        user = User(name=entered_name, super_hero=superHero, created_at=createdAt)
        DBSession.add(user)
        DBSession.flush()

     return "User Created Successfully"

#Update User
@view_config(route_name='update_user', request_method='PUT', renderer='json')
def update_user(request):
    user_id = request.matchdict.get('user_id')
    data = request.json_body #request.POST
    schema = UserSchema()
    json_dict = schema.load(data).data
    #Get Current Record in Database
    current_user_from_db = DBSession().query(User).filter_by(id=user_id).first()
    #Name
    new_name = json_dict["name"] if json_dict.get("name") else current_user_from_db.name
    #Super Hero
    superHero = json_dict["super_hero"] if json_dict.get("super_hero") else current_user_from_db.super_hero
    #Created At
    createdAt = json_dict["created_at"] if json_dict.get("created_at") else current_user_from_db.created_at

    with transaction.manager:  
       DBSession.query(User).filter_by(id=user_id).update({"name": new_name,"super_hero": superHero, "created_at":createdAt})
    return "User Updated Successfully"

#DELETE user
@view_config(route_name='delete_user', request_method='DELETE', renderer='json')
def delete_user(request):
    user_id = request.matchdict.get('user_id')
    user = DBSession.query(User).filter_by(id=user_id).first()
    if not user:
        msg = "The User with id '{}' was not found.".format(user_id)
        return Response(status=404, json_body={'error': msg})
    else :
        with transaction.manager:
          DBSession.delete(user)
          return HTTPOk()

