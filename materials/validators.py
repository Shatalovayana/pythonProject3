import re

from rest_framework.exceptions import ValidationError


class LinkValidator:
    class Meta:
        fields = ['link']

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if not re.match(r'^https://www\.youtube\.com/', value):
            raise ValidationError('Необходимо указывать Youtube-ссылку на ресурс!')
