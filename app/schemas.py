from marshmallow import fields, Schema
from marshmallow_enum import EnumField

from app.base.schema import BaseSchema
from app.enums import Nationality
from app.models import Student, Course, Enrolment, Photo


class StudentSchema(BaseSchema):
    student_id = fields.UUID(dump_only=True)
    name = fields.String(required=True)
    email = fields.Email(required=True)
    phone_number = fields.String(required=True)
    date_of_birth = fields.Date(required=True)
    nationality = EnumField(Nationality, required=True)
    password = fields.String(required=True, load_only=True)

    class Meta(BaseSchema.Meta):
        model = Student


class CourseSchema(BaseSchema):
    course_id = fields.UUID(dump_only=True)
    course_name = fields.String(required=True)
    course_code = fields.String(required=True)
    description = fields.String(required=True)
    instructor = fields.String(required=True)

    class Meta(BaseSchema.Meta):
        model = Course


class EnrolmentSchema(BaseSchema):
    enrolment_id = fields.UUID(dump_only=True)
    course_id = fields.UUID(required=True)
    student_id = fields.UUID(required=True)

    class Meta(BaseSchema.Meta):
        model = Enrolment


class PhotoSchema(BaseSchema):
    date_created = fields.DateTime(load_only=True)
    date_updated = fields.DateTime(load_only=True)
    created_by = fields.String(load_only=True)
    updated_by = fields.String(load_only=True)
    active = fields.Boolean(load_only=True)
    id = fields.UUID(dump_only=True)
    image_url = fields.String(required=True)
    caption = fields.String(required=True)

    class Meta(BaseSchema.Meta):
        model = Photo


class CalculatorSchema(Schema):
    number_one = fields.Number(required=True)
    number_two = fields.Number(required=True)
