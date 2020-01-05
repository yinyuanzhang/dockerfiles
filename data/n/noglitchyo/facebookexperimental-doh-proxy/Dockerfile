FROM python:3.6.8-alpine3.9
WORKDIR /usr/src/app

COPY . .

RUN python3 setup.py develop && python3 setup.py build

ENTRYPOINT ["sh", "/usr/src/app/docker/entrypoint.sh"]
