import re


def validate_color(color):
    if re.match(r'^(?:[0-9a-fA-F]{3}){1,2}$', color):
        return True
    return False


assert validate_color('FFFFFF') == True
assert validate_color('234234') == True
assert validate_color('aa88bb') == True

assert validate_color('FFFFF') == False
assert validate_color('ZFFFFF') == False
assert validate_color('AAAAA') == False