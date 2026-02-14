# PlaceRemember(В разработке)
Сервис для сохранения и управления любимыми местами

## Описание
PlaceRemember — это веб-приложение для сохранения, поиска и управления любимыми местами. Основные возможности проекта:

- Добавление мест с указанием названия, описания, категории и географических координат
- Фильтрация и поиск мест по категориям, названию или расположению
- Личный кабинет пользователя с избранными местами
- Просмотр мест на интерактивной карте
- Доступ к функционалу через REST API для интеграции в сторонние приложения

## Примеры запросов к API

# Технологии
- Python
- Django
- Django REST Framework
- SQLite

## Как запустить проект PlaceRemember:

Клонировать репозиторий и перейти в него в командной строке:

```bash
git clone https://github.com/hurtt111/PlaceRemember

cd PlaceRemember
```

Cоздать и активировать виртуальное окружение:

```bash
python -m venv venv
```

* Если у вас Linux/macOS

    ```bash
    source venv/bin/activate
    ```

* Если у вас windows

    ```bash
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```bash
python3 -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

Создать в директории проекта файл .env:

```
SECRET_KEY=your_secret_key
```

Создать и применить миграции:

```bash
python manage.py makemigrations

python manage.py migrate
```

Запустить проект:

```bash
python manage.py runserver 
```
Приложение будет доступно по адресу: http://127.0.0.1:8000

### Автор
[Егор Поляков](https://github.com/hurtt111)

[Telegram](https://t.me/Hurt1112)