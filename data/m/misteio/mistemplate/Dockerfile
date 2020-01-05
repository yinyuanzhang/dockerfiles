FROM python:3.6
ENV PYTHONUNBUFFERED 1

# Allows docker to cache installed dependencies between builds
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Adds our application code to the image
COPY . /website/
WORKDIR /website/website

# Migrates the database, and runs the production server
CMD python manage.py createcachetable && \
    python manage.py migrate && \
    python manage.py createadmin && \
    python manage.py collectstatic --noinput && \
    gunicorn website.wsgi -b 0.0.0.0:8000 -w 4
