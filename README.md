# Вёрстка библиотеки ([tululu.org](http://tululu.org/))

С помощью этого кода вы сможете легко сверстать свою [библиотеку](https://maratdzhukaev09.github.io/verstka_library_devman/pages/index1.html) из [результатов парсинга](https://github.com/maratdzhukaev09/parse_devman) с сайта [tululu.org](http://tululu.org/).
Пример библиотеки вы можете посмотреть [здесь](https://maratdzhukaev09.github.io/verstka_library_devman/pages/index1.html).

## Запуск кода

Для запуска кода у вас уже должен быть установлен Python 3.

- Скачайте код.
- Установите зависимости с помощью `pip` (или `pip3`, есть есть конфликт с Python2) командами `pip install -r requirements.txt`
- Переместите [результаты парсинга](https://github.com/maratdzhukaev09/parse_devman) (json-файл, папки books и images) в папку static
- Запутите код командой `python on_reload.py`
- Перейдите на сайт по ссылке: [http://127.0.0.1:5500/pages/index1.html](http://127.0.0.1:5500/pages/index1.html)

Рекомендуется использовать [virtualenv/venv](https://docs.python.org/3/library/venv.html) для изоляции проекта.

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).