FROM python:3.6.4-alpine3.7

ENV PYTHONUNBUFFERED 1
ENV PYTHON_CMD python3
#ENV PYTHONPATH /usr/local/lib/python3.6/site-packages:/usr/lib/python3.6/site-packages

RUN apk add --no-cache --virtual .fetch-deps \
        tar \
        git \
        curl \
        ca-certificates \
        openssl \
    \
    && apk add --no-cache --virtual .build-deps \
        g++ \
        gcc \
        musl-dev \
        postgresql-dev \
        python3-dev \
        make \
    && curl -LO https://configs-devops-mobydigital.netlify.com/django/requirements.txt \
    && pip install -r requirements.txt \
    && curl https://configs-devops-mobydigital.netlify.com/django/start.sh > /start.sh \
    && chmod +x /start.sh \
    && apk del --no-cache .fetch-deps .build-deps \
    && rm -fr /root/.cache

RUN apk add --no-cache --virtual .postgresql-rundeps \
      postgresql-dev \
      uwsgi-python3 \
    && mkdir -p /app \
    && rm -fr /root/.cache
WORKDIR /app
CMD ["/start.sh"]
