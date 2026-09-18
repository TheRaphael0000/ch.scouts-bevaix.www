FROM python:3
EXPOSE 80

WORKDIR /app

COPY ./pyproject.toml .

RUN pip install .

COPY . .

RUN python manage.py migrate

CMD ["sh", "./start.sh"]