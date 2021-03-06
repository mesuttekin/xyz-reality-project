import os
import unittest

from flask import current_app
from flask_testing import TestCase

from manage import app
from project.main.config import basedir


class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object('project.main.config.DevelopmentConfig')
        return app

    def test_givenDevelopAppConfig_whenFromObject_thenAppIsDevelop(self):
        """Test if app is development """
        self.assertFalse(app.config['SECRET_KEY'] == 'my_secret_key')
        self.assertTrue(app.config['DEBUG'] == True)
        self.assertFalse(current_app is None)
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///' + os.path.join(basedir, 'xyz_reality_main.db')
        )


class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object('project.main.config.TestingConfig')
        return app

    def test_givenTestinfAppConfig_whenFromObject_thenAppIsTesting(self):
        """Test if app is testing """
        self.assertFalse(app.config['SECRET_KEY'] == 'my_secret_key')
        self.assertTrue(app.config['DEBUG'])
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///' + os.path.join(basedir, 'xyz_reality_test.db')
        )


class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object('project.main.config.ProductionConfig')
        return app

    def test_givenProdAppConfig_whenFromObject_thenAppIsProduction(self):
        """Test if app is production """
        self.assertTrue(app.config['DEBUG'] is False)


if __name__ == '__main__':
    unittest.main()
