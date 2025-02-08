FROM python:3.12-slim

ARG PIP_ROOT_USER_ACTION='ignore'

ARG POETRY_VIRTUALENVS_CREATE='false'

COPY pyproject.toml poetry.lock ./

RUN pip install -U pip
RUN pip install poetry

RUN poetry install --no-root

RUN mkdir -p /usr/src/app && chown www-data:www-data /usr/src/app

USER www-data

WORKDIR /usr/src/app
