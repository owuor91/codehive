from flask_jwt_extended import jwt_required
from flask_restful import Resource

from app.base.controller import BaseController
from app.models import Student, Enrolment
from app.schemas import StudentSchema, CourseSchema, EnrolmentSchema
from app.base.db import db


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
    def get(self, student_id):
        session = db.session
        items = session.query(Enrolment).filter(
            Enrolment.student_id == student_id
        )
        return [EnrolmentSchema().dump(x) for x in items], 200

    @jwt_required()
    def delete(self, pk):
        return BaseController().delete(EnrolmentSchema(), pk)
