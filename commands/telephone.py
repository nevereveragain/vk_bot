from command_system import user_command, Response


@user_command
class Telephone:
    keys = ['телефон', 'мой телефон']
    field = 'Телефон'
    required_msg = 'Пожалуйста, введи телефон для связи, написав, например, "мой телефон 8 800 333 00 60"'

    @classmethod
    def process(cls, text):
        message = 'Спасибо, я записал номер'
        data = text.strip()
        return Response(message, '', data)
