FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV POETRY_HOME=/bin/poetry
ENV PATH="${POETRY_HOME}/bin/:${PATH}"

EXPOSE 9000

RUN apt-get -y update && apt-get -y upgrade && \
    apt-get -y install bash python3 python3-dev postgresql-client  && \
    rm -vrf /var/cache/apk/* && \
    curl -sSL https://install.python-poetry.org  | python - && \
    poetry config virtualenvs.create false --local
COPY poetry.lock .
COPY pyproject.toml .

RUN poetry install

RUN pip install redis
COPY . .

EXPOSE 8000

ENTRYPOINT python manage.py migrate & python3 manage.py runserver

#FROM python:3.11 as python-base
#
## https://python-poetry.org/docs#ci-recommendations
#ENV POETRY_VERSION=1.5.1
#ENV POETRY_HOME=/opt/poetry
#ENV POETRY_VENV=/opt/poetry-venv
#
## Tell Poetry where to place its cache and virtual environment
#ENV POETRY_CACHE_DIR=/opt/.cache
#
## Create stage for Poetry installation
#FROM python-base as poetry-base
#
## Creating a virtual environment just for poetry and install it with pip
#RUN python3 -m venv $POETRY_VENV \
#	&& $POETRY_VENV/bin/pip install -U pip setuptools \
#	&& $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}
#
## Create a new stage from the base python image
#FROM python-base as example-app
#
## Copy Poetry to app image
#COPY --from=poetry-base ${POETRY_VENV} ${POETRY_VENV}
#
## Add Poetry to PATH
#ENV PATH="${PATH}:${POETRY_VENV}/bin"
#
#WORKDIR /online_course_app
#
## Copy Dependencies
#COPY poetry.lock pyproject.toml ./
#
## [OPTIONAL] Validate the project is properly configured
#RUN poetry check
#
## Install Dependencies
#RUN poetry install --no-interaction --no-cache
#
## Copy Application
#COPY . /online_course_app
#
## Run Application
#EXPOSE 5000
#CMD ["python", "manage.py", "runserver"]


#
#FROM python:3
#
#WORKDIR /online_course_app
#
#COPY poetry.lock pyproject.toml ./
#
#RUN poetry install --no-interaction --no-cache
#
#COPY . .