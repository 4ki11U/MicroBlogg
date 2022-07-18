FROM python:3.10.5

WORKDIR /blog_app

COPY requirements.txt /blog_app
RUN pip install --upgrade pip -r requirements.txt

COPY . /blog_app
COPY . .

EXPOSE 5000

