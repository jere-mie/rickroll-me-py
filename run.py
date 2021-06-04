from website import app, db
import os
if not os.path.exists('website/site.db'):
    db.create_all()

if __name__=='__main__':
    app.run(debug=True)