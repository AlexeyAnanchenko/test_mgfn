# TEST_MGFN
Тестовое задание (Разработчик по автоматизации облачной инфраструктуры)

<details>
<summary>Условие задания</summary>

*Стек: Python, Docker.*
*Создать git проект, в котором должно быть 2 docker контейнера:*
+ *скрипт python;*
+ *БД (postgreSQL).*

*Алгоритм взаимодействия.*
*Скрипт каждую минуту отправляет данные в БД cо сгенерированными данными.*
*Пример данных:*
+ *"id": id записи (инкремент);*
+ *"data": сгенерированная строка данных;*
+ *"date": текущая дата и время.*

*Скрипт логирует свои действия.*
*При достижении в таблице БД 30 строк, таблица должна очищаться и вновь пришедшие данные должны быть записаны 1й строчкой. (Можно реализовать на уровне БД или на уровне скрипта)*
*Проект разворачивается с помощью docker compose.*

</details>

## Содержание репозитория:

- Скрипт создания таблицы при инициализации контейнера с БД: <code>[./db_data/DDL_init.sql/](https://github.com/AlexeyAnanchenko/test_mgfn/blob/main/db_data/DDL_init.sql)</code>.
- Dockerfile для сбора контейнера с python-приложением: <code>[./python_app/Dockerfile](https://github.com/AlexeyAnanchenko/test_mgfn/blob/main/python_app/Dockerfile)</code>.
- Python-скрипт: <code>[./python_app/app.py](https://github.com/AlexeyAnanchenko/test_mgfn/blob/main/python_app/app.py)</code>.
- Docker-compose файл для разворачивания БД и Python-приложения: <code>[./docker-compose.yml](https://github.com/AlexeyAnanchenko/test_mgfn/blob/main/docker-compose.yml)</code>.

## Для запуска:

1. Скопировать репозиторий
```sh
git clone git@github.com:AlexeyAnanchenko/test_mgfn.git
```

2. Развернуть контейнеры:

```sh
docker-compose up -d
```

Логи из контейнера можно будет просматривать в папке python_app/logs/.

