# Обрезка ссылок с помощью Битли

Данный скрипт позволяет узнавать количиство кликов по той или иной ссылке, а также сокращать ссылки как таковые.

### Как установить

Для начала работы необходимо:
- Зарегистрироваться на сайте [сервиса Bitly](https://bitly.com)
- Затем, можно начать получать свой [первый ключ](https://bitly.com/a/sign_in?rd=/a/oauth_apps). Ключ выглядит, как длинная строчка, составленная из хаотичного расположения букв и цифр.
- После чего создайте файл `.env` и поместите в него ключ в виде `BITLY_API_TOKEN=ваш ключ`

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
Рекомендуется использовать [virtualenv/env](https://docs.python.org/3/library/venv.html) для изоляции проекта.

### Как запустить

Для запуска скрипта используйте команду `python3 main.py ВАША_ССЫЛКА`

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).