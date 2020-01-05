ARG PYTHON_VERSION=3.7.0-alpine3.8

FROM python:${PYTHON_VERSION} as builder

ENV PYTHONUNBUFFERED=1

WORKDIR /wheels

COPY ./requirements.txt /wheels/requirements.txt
RUN pip install -U pip \
    && pip wheel -r /wheels/requirements.txt

FROM python:${PYTHON_VERSION}
ENV PYTHONUNBUFFERED=1

ENV FLASK_ENV=production
ENV FLASK_DEBUG=false

COPY --from=builder /wheels /wheels

RUN pip install -U pip \
    && pip install -r /wheels/requirements.txt \
    && rm -rf /wheels \
    && rm -rf /root/.cache/pip/*

COPY ./entrypoint.sh /

WORKDIR /code
COPY ./wsgi.py /code
COPY ./cert_checks/ /code/cert_checks
EXPOSE 5000

ENTRYPOINT [ "/entrypoint.sh" ]