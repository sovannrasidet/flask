
# run once time

from main import app, db, User

with app.app_context():
    db.create_all()
    user1 = User(username = "Example_abcdefg", password="Example_12345")
    db.session.add(user1)
    db.session.commit()
    for u in User.query.all():
        print(f"Name: {u.username} Password: {u.password}" )

