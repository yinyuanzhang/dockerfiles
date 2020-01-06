FROM python:3.7

WORKDIR /web
ADD Pipfile Pipfile
ADD Pipfile.lock Pipfile.lock

RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile
ADD docker-entrypoint.sh /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
