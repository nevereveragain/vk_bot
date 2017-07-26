from command_system import user_command, Response


@user_command
class Ready:
    keys = ['оформить', 'все', 'закончил']

    @classmethod
    def process(cls, text):
        message = 'Заказ составлен. Так как я еще маленький - мне нужно около 3-5 минут, чтобы проверить данные заказы, потом я смогу его подтвердить, или задам вопросы :) Спасибо)'
        return Response(message, '', '')
