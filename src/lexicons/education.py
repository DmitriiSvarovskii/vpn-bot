
def create_education_btn() -> dict[str, dict[str, str]]:
    return {
        'education_ios': {
            'text': '📱 Инструкция IOS',
            'url': 'https://telegra.ph/Instrukciya-po-podklyucheniyu-VPN-iOS-07-16'  # noqa
            # 'callback_data': 'education'
        },
        'education_android': {
            'text': '🤖 Android',
            'url': 'https://telegra.ph/Instrukciya-po-podklyucheniyu-VPN-Android-07-16'  # noqa
        },
        'back': {
            'text': '💠 Главное меню',
            'callback_data': 'start'
        },
    }


text_dict: dict[str, str] = {
    'text_instructions': (
        '📖 В этом разделе вы найдёте инструкции по подключению к VPN-сервису.\n\n'
        'Выберите вашу платформу:\n'
        '— 📱 iOS\n'
        '— 🤖 Android\n\n'
        'Нажмите на соответствующую кнопку ниже, чтобы открыть подробную инструкцию.\n\n'
        '💻 Инструкции для macOS и Windows — в разработке.'
    )
}
