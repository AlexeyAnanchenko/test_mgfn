import psycopg2
import time
import logging

from datetime import datetime
from faker import Faker


# значения для подключения к БД
DB_NAME = 'postgres_db'
DB_USER = 'postgres'
DB_PASS = 'postgres'
DB_HOST = 'db'  # название приложения БД в docker-compose
DB_PORT = '5432'

faker = Faker()

# получаем объект логгера с именем модуля
logger = logging.getLogger(__name__)
# записывать будем в файл app_log.log
fileHandler = logging.FileHandler(filename='app_log.log', encoding='utf-8')
# установка настроек логирования
logging.basicConfig(
    format='%(asctime)s (%(name)s) [%(levelname)s] - %(message)s',
    handlers=[fileHandler],
    level=logging.INFO
)


def get_conn():
    """Подключение к БД"""

    try:
        connection = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
        )
        cursor = connection.cursor()
        logger.info('Приложение успешно подключено к базе данных')
        return connection, cursor
    except Exception as error:
        massage = f'Не удалось подключиться к базе данных, ошибка: {error}'
        logger.error(massage)
        raise Exception(massage)


def generate_data():
    """Генерация данных для таблицы"""

    try:
        # ID инкремент, поэтому формируется на стороне БД
        text = faker.text()
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        logger.info('Данные успешно сгенерированы!')
        return text, current_time
    except Exception as error:
        message = f'Ошибка при попытке генерации данных: {error}'
        logger.error(message)
        raise Exception(error)


def check_rows(cursor):
    """Проверка количества строк в таблице"""

    try:
        cursor.execute("SELECT COUNT(1) FROM public.t_test;")
        rows_cnt = cursor.fetchone()[0]
        logger.info(f'Количество строк в таблице - {rows_cnt}')

        if rows_cnt >= 30:
            return True
        return False
    except Exception as error:
        message = f'Ошибка получения данных о количестве строк: {error}'
        logger.error(message)
        raise Exception(message)


def clear_table(connection, cursor):
    """Очистка таблицы"""

    try:
        # очистка таблицы со сбросом счетчика инкремента через Truncate
        cursor.execute("TRUNCATE TABLE public.t_test;")
        connection.commit()
        logger.info('Таблица успешно очищена!')
        return
    except Exception as error:
        # откат транзакции
        connection.rollback()

        message = f'Не удалось очистить таблицу, ошибка: {error}'
        logger.error(message)
        raise Exception(message)


def main():
    # подключаемся к БД
    connection, cursor = get_conn()

    # получаем данные для вставки строки
    text, current_time = generate_data()

    # если 30 и больше строк, то сначала очистим таблицу
    if check_rows(cursor):
        clear_table(connection, cursor)

    try:
        cursor.execute(
            '''
            INSERT INTO public.t_test (DATA, DATE) VALUES (%s, %s)
            ''',
            (text, current_time)
        )
        connection.commit()
        logger.info('Новая строка успешно вставлена в таблицу!')
        return
    except Exception as error:
        # откат транзакции
        connection.rollback()

        message = f'Не удалось вставить новую строку в таблицу: {error}'
        logger.error(message)
        raise Exception(message)


if __name__ == '__main__':
    logger.info('>>> Программа запущена')

    while True:
        main()
        logger.info('Ожидание 1 минута')
        time.sleep(60)  # вставка новых данных с интервалом в минуту
