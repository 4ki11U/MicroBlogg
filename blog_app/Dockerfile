# Выкачиваем из dockerhub образ с python версии 3.9
FROM python:3.10.5
# Устанавливаем рабочую директорию для проекта в контейнере
WORKDIR /blog_app
# Скачиваем/обновляем необходимые библиотеки для проекта
COPY requirements.txt /blog_app
RUN pip3 install --upgrade pip -r requirements.txt
# |ВАЖНЫЙ МОМЕНТ| копируем содержимое папки, где находится Dockerfile,
# в рабочую директорию контейнера
COPY . /blog_app
COPY . .
# Устанавливаем порт, который будет использоваться для сервера
EXPOSE 5000