from flask_restx import Resource, Namespace
from .model import Client, Product
from .api_model import client_model, product_model, client_input_model, product_input_model
from .extension import db
import bcrypt

ns = Namespace("api")

@ns.route("/client")
class ClientList(Resource):
    @ns.marshal_list_with(client_model)
    def get(self):
        return Client.query.all()

    @ns.expect(client_input_model)
    @ns.marshal_with(client_model)
    def post(self):
        client = Client(uci = ns.payload["uci"],
                        email = ns.payload["email"],
                        password = ns.payload["password"],
                        username = ns.payload["username"],
                        fname = ns.payload["fname"],
                        lname = ns.payload["lname"],
                        dob = ns.payload["dob"]
                        )
        db.session.add(client)
        db.session.commit()
        return client, 201
    
@ns.route("/client/<int:id>")
class ClientAPI(Resource):
    @ns.marshal_with(client_model)
    def get(self, id):
        # client = db.session.query(Client).query.get(id)
        client = Client.query.get(id)
        if client:
            return client
        else:
            ns.abort(404, f"client id {id} not found")
    
@ns.route("/product")
class ProductList(Resource):
    @ns.marshal_list_with(product_model)
    def get(self):
        return Product.query.all()

    @ns.expect(product_input_model)
    @ns.marshal_with(product_model)
    def post(self):
        product = Product(sku=ns.payload["sku"],
                          description=ns.payload["description"],
                          price=ns.payload["price"],
                          quantity= ns.payload["quantity"] or None,
                          client_id=ns.payload["client_id"])
        db.session.add(product)
        db.session.commit()
        return product, 201

@ns.route("/product/<int:id>")
class ProductAPI(Resource):
    @ns.marshal_with(product_model)
    def get(self, id):
        product = Product.query.get(id)
        if product:
            return product    
        else:
            ns.abort(404, f"product with id {id} not found")

    @ns.expect(product_input_model)
    @ns.marshal_with(product_model)
    def put(self, id):
        product = Product.query.get(id)
        if product:
            product.sku = ns.payload["sku"],
            product.description = ns.payload["description"],
            product.price = ns.payload["price"],
            product.quantity = ns.payload["quantity"],
            product.client_id = ns.payload["client_id"]
            db.session.commit()
            return product
        else:
            ns.abort(404, f"product with id {id} not found")
