FROM python:3.6
ENV PYTHONUNBUFFERED 1

# Allows docker to cache installed dependencies between builds
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Adds our application code to the image
COPY . /restjournal/
WORKDIR /restjournal

# Migrates the database, and runs the production server
CMD ./manage.py migrate && \
    python manage.py createadmin && \
    gunicorn restjournal.wsgi -b 0.0.0.0:8000