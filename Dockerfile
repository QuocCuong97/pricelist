FROM hub.paas.vn/public/python:3.9.2

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

RUN echo "ALLOW_HOSTS=$(hostname -i) localhost 127.0.0.1" >> ./.env

EXPOSE 80