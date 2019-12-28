FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1
ARG ENVIRONMENT=local

RUN apk update \
  # psycopg2 dependencies
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add postgresql-dev \
  # pillow dependencies
  && apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev \
  # translations dependencies
  && apk add gettext

# Requirements are installed here to ensure they will be cached.
COPY ./requirements /requirements
RUN if [ "$ENVIRONMENT" = "local" ] ; then pip install -r /requirements/local.txt; else pip install -r /requirements/production.txt; fi

COPY ./docker/django/entrypoint /entrypoint
RUN sed -i 's/\r//' /entrypoint
RUN chmod +x /entrypoint

COPY ./docker/django/start_local /start_local
RUN sed -i 's/\r//' /start_local
RUN chmod +x /start_local

COPY ./docker/django/start /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start

WORKDIR /app

ENTRYPOINT ["/entrypoint"]
