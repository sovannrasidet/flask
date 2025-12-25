
from main import app, db, User

with app.app_context():
    for u in User.query.all():
        print(f"({u.id}) Name: {u.username:20} Password: {u.password}" )




# import sqlite3  


# # modify for actual location of the database file
# file_location = "...{project_folder}\\instance\\data.db"  # location of the database file

# conn = sqlite3.connect(file_location)
# curs = conn.cursor()

# curs.execute("SELECT * FROM User")
# items = curs.fetchall()
# for item in items:
#     print(item) 

