FROM python:alpine

ARG PROJECT=djangoparty
ARG PROJECT_DIR=/var/www/${PROJECT}

RUN mkdir -p $PROJECT_DIR
WORKDIR $PROJECT_DIR
COPY Pipfile.lock Pipfile ./
RUN pip install -U pipenv
RUN pipenv install --system

COPY . ./

EXPOSE 8000
STOPSIGNAL SIGINT
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
