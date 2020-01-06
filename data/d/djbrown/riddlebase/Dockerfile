FROM python:3.7-stretch
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN pip install pipenv
COPY Pipfile .
COPY Pipfile.lock .
RUN pipenv install
COPY . .

RUN ["pipenv", "run", "python", "manage.py", "migrate"]

ENTRYPOINT ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000", "--settings", "riddlebase.settings_docker"]
EXPOSE 8000
