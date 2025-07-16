
def create_start_btn() -> dict[str, dict[str, str]]:
    return {
        'current_week': {
            'text': '💰 Приобрести / Продлить',
            'callback_data': 'dont-sale',
            # 'callback_data': 'presale',
        },
        'demo_key': {
            'text': '🆓 Получить демо-ключ',
            'callback_data': 'demo-key',
            # 'callback_data': 'presale',
        },
        'next_week': {
            'text': '🔑 Мои ключи',
            'callback_data': 'my-keys'
        },
        # 'del_acc': {
        #     'text': 'Удаление ключа',
        #     'callback_data': 'del-key',
        #     # 'callback_data': 'my-keys'
        # },
        'education': {
            'text': '📚 Инструкция по подключению',
            'callback_data': 'education'
        },
        # 'education_ios': {
        #     'text': '📱 Инструкция по подключению (IOS)',
        #     'url': 'https://telegra.ph/Instrukciya-po-podklyucheniyu-VPN-iOS-07-16'  # noqa
        #     # 'callback_data': 'education'
        # },
        # 'education_android': {
        #     'text': '🤖 Инструкция по подключению (Android)',
        #     'url': 'https://telegra.ph/Instrukciya-po-podklyucheniyu-VPN-Android-07-16'  # noqa
        # },
        'help': {
            'text': '🛟 Помощь',
            'callback_data': 'help'
        },
    }


text_dict: dict[str, str] = {
    'text_welcome': (
        '👋 Добро пожаловать в Fast Rabbit VPN!\n\n'
        'Сервис позволяет получить быстрый и безопасный доступ к заблокированным сайтам и приложениям.\n\n'
        '🔑 Сейчас доступен демо-тариф — вы можете начать пользоваться VPN бесплатно.\n\n'
        '👉 Нажмите «🆓 Получить демо-ключ» и далее следуйте разделу «Инструкция по подключению» на главной странице.'
    ),
    'text_repeat': 'Вы в главном меню — выберите нужный пункт ниже, чтобы получить демо-ключ, просмотреть инструкции или связаться с поддержкой.'

}
