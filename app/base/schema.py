from marshmallow import Schema, fields, pre_load, ValidationError, post_load


class BaseSchema(Schema):
    date_created = fields.DateTime()
    date_updated = fields.DateTime()
    created_by = fields.String()
    updated_by = fields.String()
    active = fields.Boolean()

    class Meta:
        ordered = True
        model = None

    @classmethod
    @pre_load
    def pre_load(cls, data):
        for k, v in data.items():
            if isinstance(v, str):
                data[k] = v.strip()
        return data

    @post_load
    def load(self, data, many=None):
        many = self.many if many is None else bool(many)
        if self.Meta.model is None:
            raise ValidationError(
                "Schema must define a model attribute under Meta"
            )
        if many:
            if not isinstance(data, list):
                raise ValidationError(
                    "data must be a list of objects if many=True"
                )

            return [self.Meta.model(**item_data) for item_data in data]
        return self.Meta.model(**data)
