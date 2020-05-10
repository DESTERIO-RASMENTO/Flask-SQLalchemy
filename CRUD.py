from app import db, puppy

# create

my_puppy = puppy('rufus',3)
db.session.add(my_puppy)
db.session.commit()

# read

all_puppies = puppy.query.all() # returns a list of puppies
print(all_puppies)
# read by id

puppy_one = puppy.query.get(1)
print(puppy_one.name)

# read by filters
puppy_frank = puppy.query.filter_by(name="frankie")
print(puppy_frank.all())

##########update
myfirstpuppy= puppy.query.get(1)
myfirstpuppy.age = 13
db.session.add(myfirstpuppy)
db.session.commit()

###delete
sec_puppy = puppy.query.get(2)
db.session.delete(sec_puppy)
db.session.commit()


all_puppies = puppy.query.all()
print(all_puppies)
