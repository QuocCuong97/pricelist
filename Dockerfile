FROM hub.paas.vn/public/python:3.9.2

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ARG HOST_IP

RUN echo $(hostname -i) > ${HOST_IP}

ENV ALLOWED_HOSTS ${HOST_IP}

EXPOSE 80