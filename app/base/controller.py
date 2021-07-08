import datetime
import json

from flask import request
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token, get_jwt_identity

from app.base.db import db


class BaseController:
    def register(self, schema):
        data = json.loads(request.data)
        data.update({"created_by": "Unknown", "updated_by": "Unknown"})
        errors = schema.validate(data)
        if errors:
            return {"errors": str(errors)}, 400

        item = schema.load(data)
        item.password = Bcrypt().generate_password_hash(item.password).decode()
        try:
            response = item.save()
            if isinstance(response, schema.Meta.model):
                return schema.dump(response), 201
            return {"error": str(response.args)}, 400
        except Exception as e:
            return {"error": e.args}, 500

    @staticmethod
    def password_is_valid(item, password):
        return Bcrypt().check_password_hash(item.password, password)

    @staticmethod
    def find_by_phone(model, phone):
        session = db.session
        return session.query(model).filter(model.phone_number == phone).first()

    @staticmethod
    def find_by_email(model, email):
        session = db.session
        return session.query(model).filter(model.email == email).first()

    def login(self, model):
        data = json.loads(request.data)
        phone = data.get("phone_number")
        password = data.get("password")
        email = data.get("email")
        item = None
        if phone is not None:
            item = BaseController.find_by_phone(model, phone)
        elif email is not None:
            item = BaseController.find_by_email(model, email)
        if item and BaseController.password_is_valid(item, password):
            pk_name = model.__table__.primary_key.columns.values()[0].name
            access_token = create_access_token(
                item.__dict__.get(pk_name),
                expires_delta=datetime.timedelta(seconds=86400),
            )
            if access_token:
                response = {
                    "message": "login successful",
                    "access_token": access_token,
                    pk_name: str(item.__dict__.get(pk_name)),
                }
                return response, 200
        else:
            return {"error": "invalid credentials"}, 401

    def create(self, schema):
        data = json.loads(request.data)
        user_id = get_jwt_identity()
        data.update({"created_by": user_id, "updated_by": user_id})
        errors = schema.validate(data)
        if errors:
            return {"errors": str(errors)}, 400
        item = schema.load(data)
        try:
            response = item.save()
            if isinstance(response, schema.Meta.model):
                return schema.dump(response), 201
            return {"error": str(response.args)}, 400
        except Exception as e:
            return {"error": e.args}, 500

    def get(self, schema, pk=None):
        model = schema.Meta.model
        session = db.session
        if pk:
            item = session.query(model).get(pk)
            return schema.dump(item), 200
        else:
            items = session.query(model).all()
            return [schema.dump(x) for x in items], 200

    def update(self, schema, pk):
        data = json.loads(request.data)
        user_id = get_jwt_identity()
        data["updated_by"] = user_id
        item = db.session.query(schema.Meta.model).get(pk)
        item.set_model_dict(data)
        response = item.save()
        return schema.dump(response), 200

    def delete(self, schema, pk):
        session = db.session
        item = session.query(schema.Meta.model).get(pk)
        response = item.delete(get_jwt_identity())
        return schema.dump(response), 200
