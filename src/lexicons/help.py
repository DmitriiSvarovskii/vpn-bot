
def create_help_btn() -> dict[str, dict[str, str]]:
    return {
        'doesnt_work': {
            'text': '🚫 Не работает VPN',
            # 'callback_data': 'doesnt-work',
            'callback_data': 'in-development'
        },
        'exchange': {
            'text': '🔄 Поменять ключ',
            'callback_data': 'in-development'
            # 'callback_data': 'exchange-keys'
        },
        'rules': {
            'text': '📑 Правила и Оферты',
            'callback_data': 'in-development'
            # 'callback_data': 'rules'
        },
        'hesupport': {
            'text': '👨‍💻 Написать в поддержку',
            'url': 'https://t.me/fast_rabbit_vpn_support'
        },
        'back': {
            'text': '💠 Главное меню',
            'callback_data': 'start'
        },
    }


text_dict: dict[str, str] = {
    'text_help': (
        '📌 В этом разделе вы сможете:\n'
        '— Сообщить, если VPN не работает;\n'
        '— Поменять ключ доступа;\n'
        '— Ознакомиться с правилами и офертой;\n'
        '— Связаться с техподдержкой.\n\n'
        '❗️На данный момент работает только кнопка «✉️ Написать в поддержку».\n'  # noqa
        'Остальные функции находятся в разработке 👨‍💻'
    )
}
