from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date
import click
from flask.cli import with_appcontext
from flask_login import UserMixin

db = SQLAlchemy()

class Client(UserMixin, db.Model):
    __tablename__= "client"

    id = db.Column(db.Integer, primary_key=True) 
    email = db.Column(db.String(100), unique=True, nullable=False, index=True)
    password = db.Column(db.LargeBinary(100))
    username = db.Column(db.String(100))
    fname = db.Column(db.String(100))
    lname = db.Column(db.String(100))
    dob = db.Column(db.Date)
    created_on = db.Column(db.DateTime, default=datetime.now)
    updated_on = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return f'<Client {self.username}>'
    
    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password


class Product(db.Model):
    __tablename__= "product"

    id = db.Column(db.Integer, primary_key=True) 
    description = db.Column(db.String(100), nullable=False)
    sku = db.Column(db.String(25), index=True, nullable=False, unique=True)
    price = db.Column(db.Numeric(12,4))
    quantity = db.Column(db.Integer)
    created_on = db.Column(db.DateTime, default=datetime.now)
    updated_on = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    

    def __repr__(self):
        return f'<Product {self.description}>'
    
    # def __init__(self,ids, email, password):
    def __init__(self, description, sku, price):
        # self.id = ids
        self.description = description
        self.sku = sku
        self.price = price

@click.command('init-db')
@with_appcontext
def init_db_command():
    db.create_all()
    click.echo('Initialized the database')

def init_app(app):
    app.cli.add_command(init_db_command)