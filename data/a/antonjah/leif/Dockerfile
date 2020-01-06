FROM python:2.7-alpine AS base

FROM base AS build

RUN apk add --no-cache g++ gcc libxslt-dev \
    && rm -rf /var/cache/apk/*

COPY requirements.txt /

RUN pip install --install-option="--prefix=/install" -r /requirements.txt

FROM base

RUN apk add --no-cache libxslt-dev \
  && rm -rf /var/cache/apk/*

COPY --from=build /install /usr/local

COPY ./*.py /app/

WORKDIR /app

CMD ["sh", "-c", "python ./leif.py"]
