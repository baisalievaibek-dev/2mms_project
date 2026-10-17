# API курсов

## Запуск

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Список и создание курсов: `http://127.0.0.1:8000/api/courses/`.

## Запросы

- `GET /api/courses/` — список курсов.
- `POST /api/courses/` — добавить курс.
- `GET /api/courses/1/` — получить курс по ID.
- `PUT` или `PATCH /api/courses/1/` — изменить курс.
- `DELETE /api/courses/1/` — удалить курс.
- `GET /api/courses/?price=120.00` — фильтр по цене.
- `GET /api/courses/?search=Python` — поиск по названию.

При создании нужно передать `title`, `description`, `price` и `duration`.
Название не может быть пустым, цена должна быть неотрицательной, а длительность
должна быть больше нуля. `created_at` заполняется автоматически.

Запуск тестов: `python manage.py test`.