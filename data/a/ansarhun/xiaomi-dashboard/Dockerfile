FROM python:3.7-stretch

ADD . /opt/xiaomi
WORKDIR /opt/xiaomi

RUN pip install pipenv && \
    pipenv install

CMD pipenv run python -m reporter
