import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)

Migrate(app,db)

################


class puppy(db.Model):

    # manual table name choice

    __tablename__ = 'puppies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    breed = db.Column(db.Text)
    #one to many
    #puppy to many toys
    toys = db.relationship('Toy',backref='puppy',lazy='dynamic')
    #one to one 
    # one owner --one puppy
    owner =db.relationship('Owner',backref='puppy',uselist=False)

    def __init__(self, name, age,breed):
        self.name = name
        self.age= age
        self.breed = breed


    def __repr__(self):
        if self.owner
            return f"puppy name is{self.name} and owner is {self.owner.name}"
        else:
            return f"pupy name is {self.name} and has no owner yet"

    def report_toys(self):
        print "here are my toys"
        for toy in self.toys:
            print( toy.item_name)


class Toy(db.Model):
    __tablename__='toys'

    id = db.Column(db.Integer,primary_key= True)
    item_name = db.Column (db.Text)
    puppy_id = db.Column(db.Integer,db.ForeignKey('puppies.id'))



class Owner(db.Model):
    pass
             

if __name__=="__main__":
    app.run(debug=True)
