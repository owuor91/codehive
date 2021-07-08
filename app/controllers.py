from flask_restful import Resource

from app.base.controller import BaseController
from app.models import Student
from app.schemas import StudentSchema


class StudentController(Resource):
    def post(self):
        return BaseController().register(StudentSchema())


class StudentLogin(Resource):
    def post(self):
        return BaseController().login(Student)