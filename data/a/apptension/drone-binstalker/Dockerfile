FROM python:3.6.6-alpine

ENV PYTHONPATH /usr/src/app
ENV APP_PATH /usr/src/app/drone-binstalker-client
WORKDIR ${APP_PATH}

RUN pip install --upgrade --no-cache-dir Jinja2==2.10 requests==2.9.1 && \
    mkdir -p ${APP_PATH}

COPY . ${APP_PATH}
CMD python ${APP_PATH}/run.py
