from rest_framework.serializers import ValidationError


def validate_link(value):
    if "youtube.com" not in value and value is not None:
        raise ValidationError("Ссылка может быть только на YouTube")