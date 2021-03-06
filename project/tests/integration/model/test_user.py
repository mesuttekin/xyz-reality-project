import unittest

from project.main import db
from project.main.model.user import User
from project.tests.integration.base import BaseTestCase


class TestUserModel(BaseTestCase):

    def test_givenUser_whenUserAdded_thenGetTheUser(self):
        """Add and get a user to DB """
        expected_user = User(
            email='test@test.com',
            name='Mesut',
            surname='Tekin',
            password='test'
        )
        db.session.add(expected_user)
        db.session.commit()
        actual_user = User.query.filter_by(email='test@test.com').first()

        self.assertEqual(expected_user.email, actual_user.email)
        self.assertEqual(expected_user.name, actual_user.name)
        self.assertEqual(expected_user.surname, actual_user.surname)

    def test_givenUserWithPass_whenAddDB_thenEncodeAuthToken(self):
        """User model encode auth token test """
        user = User(
            email='test@test.com',
            password='test'
        )
        db.session.add(user)
        db.session.commit()
        auth_token = user.encode_auth_token(user.id, user.email)
        self.assertTrue(isinstance(auth_token, bytes))

    def test_givenUserWithPass_whenAddDB_thenDecodeAuthToken(self):
        """User model decode auth token test """
        user = User(
            email='test@test.com',
            password='test'
        )
        db.session.add(user)
        db.session.commit()
        auth_token = user.encode_auth_token(user.id, user.email)
        self.assertTrue(isinstance(auth_token, bytes))
        payload = User.decode_auth_token(auth_token.decode("utf-8"))
        self.assertEqual('test@test.com', payload['user_email'])


if __name__ == '__main__':
    unittest.main()
