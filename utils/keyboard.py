from vkbottle import KeyboardButtonColor, Text, Keyboard


MENU_KEYBOARD = (
    Keyboard()
    .add(Text("Установить статус", {"cmd": "set_status"}))
    .row()
    .add(Text("Просмотреть статусы", {"cmd": "view_statuses"}))
    .row()
    .add(Text("Удалить статус", {"cmd": "remove_status"}))
    .add(Text("Удалить статус из БД", {"cmd": "delete_status"}))
    .row()
    .add(Text("Показать статус", {"cmd": "show_status"}))
    .row()
    .add(Text("Создать статус", {"cmd": "create_status"}))
).get_json()

BACK_TO_MENU = Keyboard()
BACK_TO_MENU.add(Text("Вернуться в меню", {"cmd": "back"}))
BACK_TO_MENU = BACK_TO_MENU.get_json()
