WORKDIR /app/

ENV DJANGO_SETTINGS_MODULE='config.settings'

RUN pip install poetry==1.5.1

COPY poetry.lock .
COPY pyproject.toml .

RUN poetry install --without dev

COPY . .

CMD poetry run python manage.py runserver 0.0.0.0:8000