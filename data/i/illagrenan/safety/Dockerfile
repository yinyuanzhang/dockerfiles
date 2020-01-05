FROM python:3-alpine

LABEL authors="Vašek Dohnal <vaclav.dohnal@gmail.com>"
ARG SAFETY_VERSION=1.8.4

RUN pip install --ignore-installed --isolated --no-input --compile --exists-action=a --disable-pip-version-check --no-cache-dir \
      safety==${SAFETY_VERSION}

CMD ["safety", "check"]
