import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from project import blueprint
from project.main import create_app, db

# values for env are "dev, test, prod"
app = create_app(os.getenv('PROJECT_ENV') or 'dev')
app.register_blueprint(blueprint)
# Disable the mask field, by default X-Fields
app.config['RESTPLUS_MASK_SWAGGER'] = False

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run(debug=True, host='0.0.0.0')


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
