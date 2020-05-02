from app import create_app, db
import os
from flask_migrate import Migrate
from app.models import User,Role
import click

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

migrate = Migrate(app, db)


# cmd 启动示例
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User)

@app.cli.command()
def deploy():
    """Run deployment tasks."""
    # # migrate database to latest revision
    # upgrade()

    # create or update user roles
    Role.insert_roles()

    # ensure all users are following themselves
    User.add_self_follows()