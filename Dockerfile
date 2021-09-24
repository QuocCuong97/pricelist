FROM hub.paas.vn/public/python:3.9.2

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 80

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:80"]