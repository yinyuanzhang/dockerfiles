# python:alpine is 3.{latest}
FROM python:alpine 

COPY src/requirements.txt /src/

RUN apk add --virtual .install_dependencies_paramiko \
    gcc \
    musl-dev \
    python-dev \
    libffi-dev \
    openssl-dev \
    build-base \
    py-pip \
    libssl1.0 \
&&  pip install -r /src/requirements.txt \
&&  apk del .install_dependencies_paramiko


COPY src/app.py /src/

EXPOSE 5000

ENTRYPOINT ["python", "/src/app.py"]
