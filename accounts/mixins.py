from django.core.exceptions import ValidationError
import re


def contact_number_validator(value):
    rule = re.compile(r'(^([+]{1}[8]{2}|0088)?(01){1}[3-9]{1}\d{8})$')
    if not rule.search(value):
        raise ValidationError('Invalid contact number. Enter a valid contact number.')
