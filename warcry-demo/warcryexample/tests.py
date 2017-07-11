import datetime
import unittest
import transaction

from pyramid import testing

from .models import DBSession


class TestMyViewSuccessCondition(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        from sqlalchemy import create_engine
        engine = create_engine('sqlite://')
        from .models import (
            Base,
            User,
            )
        DBSession.configure(bind=engine)
        Base.metadata.create_all(engine)
        with transaction.manager:
            model = User(name='Bruce Wayne', super_hero=True,
                         created_at=datetime.datetime.now())
            DBSession.add(model)

    def tearDown(self):
        DBSession.remove()
        testing.tearDown()

    def test_passing_view(self):
        from .views import get_user_sqlalchemy_simple
        request = testing.DummyRequest()
        user = get_user_sqlalchemy_simple(request)
        self.assertEqual(user.name, 'Bruce Wayne')
