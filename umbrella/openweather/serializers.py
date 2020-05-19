from datetime import datetime

from marshmallow import fields, Schema, EXCLUDE


class UnixTimestamp(fields.Field):

    def _deserialize(self, value, attr, obj, **kwargs):
        return datetime.fromtimestamp(value) if value else None


class ForecastSchema(Schema):

    dt = UnixTimestamp()
    humidity = fields.Int()

    class Meta:
        unknown = EXCLUDE
