
def create_presale_btn() -> dict[str, dict[str, str]]:
    return {
        'one_month': {
            'text': '🟡 1 мес - 150₽',
            'callback_data': 'dont-sale'
            # 'callback_data': 'one-month',
        },
        'tree_month': {
            'text': '🟢 3 мес - 350₽',
            'callback_data': 'dont-sale'
            # 'callback_data': 'tree-month'
        },
        'six_month': {
            'text': '🔵 6 мес - 600₽',
            'callback_data': 'dont-sale'
            # 'callback_data': 'six-month'
        },
        'one_year': {
            'text': '🟣 12 мес - 1000₽',
            'callback_data': 'dont-sale'
            # 'callback_data': 'one-year'
        },
        'back': {
            'text': '💠 Главное меню',
            'callback_data': 'start'
        },
    }


text_dict: dict[str, str] = {
    'main_text': "1️⃣ Выбери нужный тариф ниже👇🏻\n"
    "2️⃣ Произведи оплату\n"
    "3️⃣ Установи VPN на свое устройство\n\n"
    "❗️После оплаты выдадим приложение, которое доступно для установки "
    "на Iphone, Android, ПК, macOS\n\n",
    # "💡Доступ выдается на телефон, компьютер, планшет и телевизор AndroidTV",
    'text_demo_key': '🔑 Ваш демо-ключ для подключения VPN (действует до старта продаж платных тарифов):\n\n',  # noqa
    'text_instructions': '\n\n📌 Скопируйте ключ и следуйте инструкции по подключению.',  # noqa
    'text_double_key': 'У вас уже есть демо-ключ, вы можете его скопировать в разделе "🔑 Мои ключи"',  # noqa
}
