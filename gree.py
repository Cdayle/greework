from app import create_app,db
import os


app = create_app(os.getenv('FLASK_CONFIG') or 'default')

# migrate = Migrate(app,db)

# cmd 启动示例
# @app.shell_content_processor
# def make_shell_context():
# 	return dic(db=db, User=User,Role=Role)
