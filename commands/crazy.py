from command_system import user_command, Response


@user_command
class Crazy:
    keys = ['крейзи', 'крейзи пицца', 'удиви меня', 'необычное']

    @classmethod
    def process(cls, text):
        message = '\n Томатный соус, увеличенные порции цыпленка и пепперони, моцарелла, кисло-сладкий соус \nМаленькая стоит 425 рублей, Средняя - 605 рублей, Большая - 755 рублей.  \nОна и с мясом и с кислым соусом, очень необычное и классное сочетание. Будешь? Для заказа напиши, например, "Буду маленькую крейзи пиццу"'
        attachment = 'photo-148325456_456239017'
        return Response(message, attachment, '')
