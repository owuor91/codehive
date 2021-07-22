from flask_jwt_extended import jwt_required
from flask_restful import Resource

from app.base.controller import BaseController
from app.models import Student
from app.schemas import StudentSchema, CourseSchema


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
        return BaseController().get(CourseSchema(),pk)

    @jwt_required()
    def put(self, pk):
        return BaseController().update(CourseSchema(), pk)

    @jwt_required()
    def delete(self, pk):
        return BaseController().delete(CourseSchema(), pk)
