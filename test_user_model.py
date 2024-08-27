"""User model tests."""

import os
from unittest import TestCase

from app import app
from models import db, dbx, User

# To run the tests, you must provide a "test database", since these tests
# delete & recreate the tables & data. In your shell:
#
# Do this only once:
#   $ createdb warbler_test
#
# To run the tests using that test data:
#   $ DATABASE_URL=postgresql:///warbler_test python3 -m unittest

if not app.config['SQLALCHEMY_DATABASE_URI'].endswith("_test"):
    raise Exception(
        "\n\nMust set DATABASE_URL env var to db ending with _test")

# NOW WE KNOW WE'RE IN THE RIGHT DATABASE, SO WE CAN CONTINUE
app.app_context().push()
db.drop_all()
db.create_all()


class UserModelTestCase(TestCase):
    def setUp(self):
        dbx(db.delete(User))
        db.session.commit()

        u1 = User.signup("u1", "u1@email.com", "password", None)
        u2 = User.signup("u2", "u2@email.com", "password", None)

        db.session.commit()
        self.u1_id = u1.id
        self.u2_id = u2.id

    def tearDown(self):
        db.session.rollback()

    def test_user_model(self):
        u1 = db.session.get(User, self.u1_id)

        # User should have no messages & no followers
        self.assertEqual(len(u1.messages), 0)
        self.assertEqual(len(u1.followers), 0)


# Does is_following successfully detect when user1 is following user2?


# Does is_following successfully detect when user1 is not following user2?

# Does is_followed_by successfully detect when user1 is followed by user2?

# Does is_followed_by successfully detect when user1 is not followed by user2?

# Does User.signup successfully create a new user given valid credentials?

# Does User.signup fail to create a new user if any of the validations (eg uniqueness, non-nullable fields) fail?

# Does User.authenticate successfully return a user when given a valid username and password?

# Does User.authenticate fail to return a user when the username is invalid?

# Does User.authenticate fail to return a user when the password is invalid?
