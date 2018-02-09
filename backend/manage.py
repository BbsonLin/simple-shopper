import os

from flask_script import Manager, Server
from flask_migrate import MigrateCommand

from app import create_app, init_db
from config import config

extra_dirs = config[os.environ.get('FLASK_CONFIG', 'development')].EXTRA_DIRS
print('extra_dirs', extra_dirs)
extra_files = extra_dirs[:]
for extra_dir in extra_dirs:
    for dirname, dirs, files in os.walk(extra_dir):
        for filename in files:
            filename = os.path.join(dirname, filename)
            if os.path.isfile(filename):
                extra_files.append(filename)

app = create_app(os.environ.get('FLASK_CONFIG', 'development'))
manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command("runserver",
                    Server(host='0.0.0.0', use_debugger=True,
                           use_reloader=True, extra_files=extra_files))


@manager.command
def init_all():
    init_db()


if __name__ == '__main__':
    manager.run()
