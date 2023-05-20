# from flask_sqlalchemy import SQLAlchemy
from .extension import db
from datetime import datetime, date
import click
from flask.cli import with_appcontext
from flask_login import UserMixin
import bcrypt

# db = SQLAlchemy()

# class Client(UserMixin, db.Model):
class Client(db.Model):
    __tablename__= "client"

    id = db.Column(db.Integer, primary_key=True) 
    # ssn = db.Column(db.String(50), unique=True, nullable=False, index=True)
    #unique client identifier
    uci = db.Column(db.String(50), unique=True, nullable=False, index=True)
    email = db.Column(db.String(100), unique=True, nullable=False, index=True)
    username = db.Column(db.String(100))
    # password = db.Column(db.LargeBinary(100))
    password = db.Column(db.String(100))
    fname = db.Column(db.String(100))
    lname = db.Column(db.String(100))
    dob = db.Column(db.Date)
    created_on = db.Column(db.DateTime, default=datetime.now)
    updated_on = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    products = db.relationship("Product", back_populates="client")

    def __repr__(self):
        return f'''<Client\n{self.id}\n{self.uci}\n{self.email}\n{self.username}\n
        {self.password}\n{self.fname}\n{self.lname}\n{self.dob}\n
        {self.created_on}\n{self.updated_on}>'''
    
    def __init__(self, uci, email, username, password, fname="", lname="", dob=None):
        self.uci = uci
        self.email = email
        self.username = username
        #str to byte
        bpasswd = password.encode('utf-8')
        passwd_hash = bcrypt.hashpw(bpasswd, bcrypt.gensalt())
        self.password = passwd_hash
        self.fname = fname
        self.lname = lname
        self.dob = dob


class Product(db.Model):
    __tablename__= "product"

    id = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String(25), index=True, nullable=False, unique=True)
    description = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Numeric(12,4))
    quantity = db.Column(db.Integer)
    created_on = db.Column(db.DateTime, default=datetime.now)
    updated_on = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    
    client_id = db.Column(db.ForeignKey("client.id"))
    client = db.relationship("Client", back_populates="products")

    def __repr__(self):
        #literal string interpolation '''
        return f'''<Product\n{self.id}\n{self.sku}\n{self.description}\n
            {self.price}\n{self.quantity}\n{self.client_id}>'''
    
    def __init__(self, sku, description, client_id, price=0, quantity=0):
        self.sku = sku
        self.description = description
        self.client_id = client_id
        self.price = price
        # self.quantity = 1 if quantity is None else quantity
        self.quantity = quantity


@click.command('init-db')
@with_appcontext
def init_db_command():
    db.create_all()
    click.echo('Initialized the database')

def init_app(app):
    app.cli.add_command(init_db_command)