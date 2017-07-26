from command_system import user_command, Response


@user_command
class Address:
    keys = ['адрес', 'мой адрес', 'я живу']
    field = 'Адрес'
    required_msg = 'Пожалуйста, введи свой полный адрес доставки, написав, например "я живу на улице Космонавтов, дом 3, квартира 4, подъезд 2, домофон 1"'

    @classmethod
    def process(cls, text):
        message = 'Спасибо, я записал адрес. Напиши "меню" для вывода меню, либо "оформить", если готов оформить заказ'
        data = text.strip()
        return Response(message, '', data)
