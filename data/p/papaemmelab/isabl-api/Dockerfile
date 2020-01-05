FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1

RUN apk update \
    # psycopg2 dependencies
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    # Pillow dependencies
    && apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev \
    # CFFI dependencies
    && apk add libffi-dev py-cffi \
    # https://docs.djangoproject.com/en/dev/ref/django-admin/#dbshell
    && apk add postgresql-client

# install some of API dependencies - this will need to be updated manually
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
