from flask_restx import fields
from .extension import api

client_model = api.model("ClientModel", {
    "id": fields.Integer,
    "uci": fields.String,
    "email": fields.String,
    "password": fields.String,
    "username": fields.String,
    "fname": fields.String,
    "lname": fields.String,
    "dob": fields.Date,
    "created_on": fields.DateTime,
    "updated_on": fields.DateTime,
    # "products": fields.List(fields.Nested(product_model))
})

client_input_model = api.model("ClientInputModel", {
    "uci": fields.String,
    "email": fields.String,
    "password": fields.String,
    "username": fields.String,
    "fname": fields.String,
    "lname": fields.String,
    "dob": fields.Date,
})

product_model = api.model("ProductModel", {
    "id": fields.Integer,
    "sku": fields.String,
    "description": fields.String,
    "price": fields.Integer,
    "quantity": fields.Integer,
    "created_on": fields.DateTime,
    "updated_on": fields.DateTime,
    #relationship
    "client": fields.Nested(client_model)
})

product_input_model = api.model("ProductInputModel", {
    "sku": fields.String,
    "description": fields.String,
    "price": fields.Integer,
    "quantity": fields.Integer,
    #relationship
    "client_id": fields.Integer,
})