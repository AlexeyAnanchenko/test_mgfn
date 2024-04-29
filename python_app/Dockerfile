FROM python:3.11
# строка ниже копирует файл requirements.txt в папку /opt/app/ контейнера
COPY requirements.txt /opt/app/
# установка зависимостей внутри контейнера
RUN pip3 install -r /opt/app/requirements.txt
COPY app.py /opt/app/
WORKDIR /opt/app/
# закуск приложения из директории /opt/app/
CMD ["python", "app.py"]