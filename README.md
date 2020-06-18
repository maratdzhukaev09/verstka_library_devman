# Вёрстка библиотеки ([tululu.org](http://tululu.org/))

Вёрстка библиотеки с книгами в жанре "Научная фантастика" с сайта [tululu.org](http://tululu.org/). Также с помощью этого кода вы сможете легко сверстать свою библиотеку из [результатов парсинга](https://github.com/maratdzhukaev09/parse_devman) с сайта [tululu.org](http://tululu.org/).

Пример сайта библиотеки вы можете посмотреть [здесь](https://maratdzhukaev09.github.io/verstka_library_devman/pages/index1.html). 

## Установка кода
(Пример на Windows; на Mac и Linux используйте `/`, вместо `\`)

Установите код консольной командой:
```bash
$ git clone https://github.com/maratdzhukaev09/verstka_library_devman.git
```
Или скачайте [архив с кодом.](https://github.com/maratdzhukaev09/verstka_library_devman/archive/master.zip)

Библиотека будет доступна по ссылке вида: file///полный/путь/к/репозиторию/pages/index1.html.
В адресе используйте только `/`, вместо `\`.

## Подготовка к запуску

Для запуска кода у вас уже должен быть установлен Python 3.

Перейдите в репозиторий командой:
```bash
$ cd путь\к\репозиторию
```

### Если у вас есть [результаты парсинга](https://github.com/maratdzhukaev09/parse_devman):

Если у вас есть свои результаты парсинга переместите(замените на свои) их (файл library.json, папки books и images) в папку static.

### Использование [virtualenv/venv](https://docs.python.org/3/library/venv.html)

Создайте virtualenv/venv консольной командой:
```bash
$ virtualenv название_virtualenv_venv
```
Активируйте virtualenv/venv командой:
```bash
$ название_virtualenv_venv\Scripts\activate
```

### Установка зависимостей

Установите зависимости с помощью `pip` (или `pip3`, если есть конфликт с Python2) командой:
```bash
$ pip install -r requirements.txt
```

## Запуск кода
Запустите код командой:
```bash
$ python render_website.py
# Используйте python3, если есть конфликт с Python2
```

Сайт будет доступен по ссылке: [http://127.0.0.1:5500/pages/index1.html](http://127.0.0.1:5500/pages/index1.html)

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).