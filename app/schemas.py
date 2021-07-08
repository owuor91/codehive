from marshmallow import fields
from marshmallow_enum import EnumField

from app.base.schema import BaseSchema
from app.enums import Nationality
from app.models import Student


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

