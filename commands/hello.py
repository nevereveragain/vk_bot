from command_system import user_command, Response


@user_command
class Hello:
    keys = ['привет', 'hello', 'дратути', 'здравствуй', 'здравствуйте', 'hi!']

    @classmethod
    def process(cls, text):
        message = 'Привет :)\nУ нас есть пицца) \n Напиши "Меню" для показа меню, либо "заказ", если уже знаешь, что хочешь (например, "заказать пепперони 25 см")\nЯ еще молод, поэтому, если со мной что-то пойдет не так, напиши, пожалуйста: или позвони в наш колл-центр по номеру: '
        return Response(message, '', '')
