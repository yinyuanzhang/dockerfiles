FROM python:3.7-alpine

MAINTAINER Artemix <ivan@artemix.org>

RUN apk add --no-cache build-base
RUN mkdir /app
WORKDIR /app
RUN pip install sinking
RUN apk del build-base

EXPOSE 8080

CMD ["python", "-m", "sinking"]
