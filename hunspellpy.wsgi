activate_this = '/var/www/hunspellpy_venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

import sys
sys.path.append('/var/www/hunspellpy_venv/hunspellpy')

from hunspellpyrest import app as application

sys.stdout = sys.stderr
