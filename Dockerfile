FROM hub.paas.vn/public/python:3.9.2

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENV ALLOWED_HOSTS localhost 127.0.0.1

EXPOSE 80

