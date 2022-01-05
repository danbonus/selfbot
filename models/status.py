from tortoise.models import Model
from tortoise import fields


class Status(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField(required=True)
    text = fields.TextField()
    description = fields.TextField()

    class Meta:
        model = "Status"
        fields = ('name', 'text', 'description')

    def __str__(self):
        return self.name
