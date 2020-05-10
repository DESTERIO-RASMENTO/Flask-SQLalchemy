from app import db, puppy

# creates all tables

db.create_all()

sam = puppy('sammy',10)
frank = puppy('frankie',5)

db.session.add_all([sam,frank])

db.session.commit()

print(sam.id)
print(frank.id)