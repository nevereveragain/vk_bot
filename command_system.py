from collections import namedtuple

Response = namedtuple('Response', ['message', 'attachment', 'data'])

command_list = []
required_fields = {}


def user_command(cls):
    command_list.append(cls)
    if hasattr(cls, 'field') and hasattr(cls, 'required_msg'):
        required_fields[cls.field] = cls
    return cls
