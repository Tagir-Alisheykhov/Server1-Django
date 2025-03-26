# Интернет магазин

В этом проекте реализовывается основной функционал для интернет-магазина с использованием 
фреймворка Django.

## Структура проекта
- `catalog/`: 
  - `migrations/`: 
  - `templates/`: 
  - `admin.py`: 
  - `apps.py`:
  - `models.py`:
  - `tests.py`:
  - `urls.py`:
  - `views.py`:
- `config/`: 
  - `asgi.py`: 
  - `settings.py`: 
  - `urls.py`: 
  - `wsgi.py`:
- `static/`: 
  - `css/`: 
  - `js/`: 
- `.gitignore`: 
- `manage.py`: 


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
