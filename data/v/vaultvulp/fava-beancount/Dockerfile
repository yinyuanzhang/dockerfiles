FROM python:3.6

WORKDIR /opt/app

RUN pip install -U pipenv

COPY ./Pipfile  ./Pipfile
COPY ./Pipfile.lock ./Pipfile.lock

RUN pipenv install --deploy

COPY ./main.bean ./data/main.bean

ENTRYPOINT ["pipenv"]
CMD ["run", "app"]