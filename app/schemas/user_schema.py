from app.extensions import ma
from app.models.user import User
from marshmallow import fields, validate
from marshmallow_sqlalchemy import auto_field

class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    id = ma.auto_field(dump_only=True)
    nome = ma.auto_field(required=True)
    email = fields.Email(required=True)
    senha = fields.String(
        required=True,
        load_only=True,
        validate=validate.Length(min=6)
    )
    admin = ma.auto_field()