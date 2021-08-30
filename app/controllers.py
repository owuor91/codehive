from flask_jwt_extended import jwt_required
from flask_restful import Resource, request

from app.base.controller import BaseController
from app.models import Student, Enrolment
from app.schemas import (
    StudentSchema,
    CourseSchema,
    EnrolmentSchema,
    PhotoSchema,
    CalculatorSchema,
)
from app.base.db import db
import json


class StudentController(Resource):
    def post(self):
        return BaseController().register(StudentSchema())


class StudentLogin(Resource):
    def post(self):
        return BaseController().login(Student)


class CourseController(Resource):
    @jwt_required()
    def post(self):
        return BaseController().create(CourseSchema())

    @jwt_required()
    def get(self, pk=None):
        return BaseController().get(CourseSchema(), pk)

    @jwt_required()
    def put(self, pk):
        return BaseController().update(CourseSchema(), pk)

    @jwt_required()
    def delete(self, pk):
        return BaseController().delete(CourseSchema(), pk)


class EnrolmentController(Resource):
    @jwt_required()
    def post(self):
        return BaseController().create(EnrolmentSchema())

    @jwt_required()
    def get(self):
        student_id = request.args.get("student_id")
        if student_id is not None:
            session = db.session
            items = session.query(Enrolment).filter(
                Enrolment.student_id == student_id
            )
            return [EnrolmentSchema().dump(x) for x in items], 200
        return {"error": "student_id required"}, 400

    @jwt_required()
    def delete(self, pk):
        return BaseController().delete(EnrolmentSchema(), pk)


class PhotosController(Resource):
    @jwt_required()
    def post(self):
        return BaseController().create(PhotoSchema())

    def get(self, pk=None):
        return BaseController().get(PhotoSchema(), pk)

    @jwt_required()
    def put(self, pk):
        return BaseController().update(PhotoSchema(), pk)

    @jwt_required()
    def delete(self, pk):
        return BaseController().delete(PhotoSchema(), pk)


class Arithmetic:
    def calculate(self, operation):
        data = json.loads(request.data)
        errors = CalculatorSchema().validate(data)
        if errors:
            return {"errors": str(errors)}, 400

        number_one = data["number_one"]
        number_two = data["number_two"]

        if operation == "+":
            result = number_one + number_two
        elif operation == "-":
            result = number_one - number_two
        elif operation == "*":
            result = number_one * number_two
        elif operation == "/":
            result = number_one / number_two
        else:
            result = 0
        return {"result": result}, 200


class AdditionController(Resource):
    def post(self):
        return Arithmetic().calculate("+")


class SubtractionController(Resource):
    def post(self):
        return Arithmetic().calculate("-")


class MultiplicationController(Resource):
    def post(self):
        return Arithmetic().calculate("*")


class DivisionController(Resource):
    def post(self):
        return Arithmetic().calculate("/")
