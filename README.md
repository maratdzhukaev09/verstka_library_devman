# Вёрстка библиотеки ([tululu.org](http://tululu.org/))

Вёрстка библиотеки с книгами в жанре "Научная фантастика" с сайта [tululu.org](http://tululu.org/). Также с помощью этого кода вы сможете легко сверстать свою [библиотеку](https://maratdzhukaev09.github.io/verstka_library_devman/pages/index1.html) из [результатов парсинга](https://github.com/maratdzhukaev09/parse_devman) с сайта [tululu.org](http://tululu.org/).

Пример библиотеки вы можете посмотреть [здесь](https://maratdzhukaev09.github.io/verstka_library_devman/pages/index1.html).

## Подготовка к запуску

Для запуска кода у вас уже должен быть установлен Python 3.

### Установка кода

[Скачайте репозиторий.](https://github.com/maratdzhukaev09/verstka_library_devman/archive/master.zip)

(Если у вас есть [результаты парсинга](https://github.com/maratdzhukaev09/parse_devman) переместите их (json-файл, папки books и images) в папку static.)

### Использование [virtualenv/venv](https://docs.python.org/3/library/venv.html)

Создайте virtualenv/venv консольной командой:
```bash
$ virtualenv путь\к\репозиторию\venv
```
Перейдите в репозиторий командой:
```bash
$ cd путь\к\репозиторию
```
Активируйте virtualenv/venv командой:
```bash
$ venv\Scripts\activate
```

### Установка зависимостей

Установите зависимости с помощью `pip` (или `pip3`, есть есть конфликт с Python2) командой:
```bash
$ pip install -r requirements.txt
```

## Запуск кода
Запустите код командой:
```bash
$ python render_website.py
```

Сайт будет доступен по ссылке: [http://127.0.0.1:5500/pages/index1.html](http://127.0.0.1:5500/pages/index1.html)

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).