# Проект пожертвований на благо кошечек
Проект пожертвований, написанный на FastApi

## Запуск проекта:


Клонировать репозиторий и перейти в него в командной строке:

```
git clone 
```

```
cd cat_charity_fund
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Использовать миграции:

```
alembic upgrade head
```

Запуск приложения:

```
uvicorn app.main:app
```

## Автор
- Макаров Пётр
