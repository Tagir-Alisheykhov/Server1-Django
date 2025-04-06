# Интернет магазин

В этом проекте реализовывается основной функционал для интернет-магазина с использованием 
фреймворка Django.

## Структура проекта
- `catalog/`: Приложение
  - `migrations/`: Миграции 
  - `templates/`: HTML-страницы веб-приложения
  - `admin.py`: Модуль для работы с административной панелью
  - `apps.py`: Приложения
  - `models.py`: Модели для работы с БД
  - `tests.py`: Модуль для тестирования функционала
  - `urls.py`: Маршрутизатор для страниц веб-приложения
  - `views.py`: Контроллер
- `config/`: 
  - `asgi.py`: 
  - `settings.py`: 
  - `urls.py`: Маршрутизатор проекта
  - `wsgi.py`: 
- `static/`: Статические данные
  - `css/`: Стили CSS
  - `js/`: Скрипты JavaScript
- `.gitignore`: Игнорируемые файлы
- `catalog_fixture.json`: Файл с тестовыми данными для загрузки в БД.
- `manage.py`: Менеджер для работы с проектом


## Запуск проекта
Для запуска проекта нужно запустить сервер, с помощью следующей команды:
```bash
python manage.py runserver
```

## Основные зависимости проекта
- `asgiref`  3.8.1  ASGI specs, helper code, and adapters
- `django`   5.1.7  A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- `sqlparse` 0.5.3  A non-validating SQL parser.
- `tzdata`   2025.2 Provider of IANA time zone data
