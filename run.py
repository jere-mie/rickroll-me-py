from website import app, db
import os
import sys
import json

# getting config details
with open('config.json') as f:
    data = json.load(f)

if not os.path.exists('website/site.db'):
    db.create_all()

# running site
if __name__=='__main__':
    # run this command with any additional arg to run in production
    if len(sys.argv) > 1:
        print('<< PROD >>')
        os.system(f"gunicorn -b '127.0.0.1:{data['port']}' website:app")
    # or just run without an additional arg to run in debug
    else:
        print('<< DEBUG >>')
        app.run(debug=True)