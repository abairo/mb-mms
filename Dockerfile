FROM python:3.9.7-alpine3.14

ARG DJANGO_ENV

ENV DJANGO_ENV=${DJANGO_ENV} \
  # python:
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  # pip:
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  # poetry:
  POETRY_VERSION=1.1.8 \
  POETRY_VIRTUALENVS_CREATE=false \
  TZ=America/Sao_Paulo

RUN date

# System deps:
RUN apk --no-cache add \
    rust \
    cargo \
    gcc \
    libffi-dev \
    openssl-dev \
    postgresql-dev \
    bash \
  && pip install "poetry==$POETRY_VERSION" 

COPY pyproject.toml poetry.lock /app/
WORKDIR /app
RUN poetry install $(test "$DJANGO_ENV" == production && echo "--no-dev") --no-interaction --no-ansi

COPY . /app
