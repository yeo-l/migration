FROM python:3.9-slim

ENV DATABASE_TYPE = "mysql"
ENV DATABASE_NAME = "db"
ENV DATABASE_USER = "root"
ENV DATABASE_PASS = ""
ENV DATABASE_HOST = "localhost"
ENV DATABASE_PORT = "3306"

COPY ./src /app/src

COPY ./requirements.txt /app

WORKDIR app

RUN pip3 install -r requirements.txt

EXPOSE 8080

CMD ["uvicorn", "src.main:app", "--host=0.0.0.0", "--reload"]