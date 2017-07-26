from command_system import user_command, Response


@user_command
class Order:
    keys = ['мой заказ', 'заказ', 'хочу заказать']
    field = 'Заказ'
    required_msg = 'Пожалуйста, выбери пиццу для заказа'
    multiple = True

    @classmethod
    def process(cls, text):
        # Наши пиццы бывают маленькими (25см), средними (30 см) и большими (см)
        message = 'Спасибо, пицца добавлена в заказ'
        data = text.strip()
        return Response(message, '', data)
