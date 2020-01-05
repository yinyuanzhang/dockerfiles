FROM python:3.8

RUN apt-get update \
    && apt-get install -y ghostscript \
    && rm -rf /var/cache/apt

RUN pip install --no-cache-dir coverage tox poetry pipenv && \
	poetry config virtualenvs.create false
