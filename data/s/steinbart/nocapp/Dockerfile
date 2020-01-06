# TODO: Upgrade this to >3.7 as soon as Celery fixes #4849
FROM python:3.6
COPY . /app
WORKDIR /app
# Install required dependencies
RUN pip install pipenv
RUN pipenv install --system
RUN pip3 install uwsgi
