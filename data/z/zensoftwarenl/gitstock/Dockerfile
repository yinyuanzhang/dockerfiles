FROM python:3-alpine

MAINTAINER Arjan Franzen

COPY gitstock/requirements.txt ./

RUN apk add --virtual build-dependencies \
      build-base --no-cache \
      && pip install -qq -r requirements.txt \
      && rm -rf .cache/pip \
      && apk del build-dependencies

RUN apk add git --no-cache

RUN mkdir /gitstock

COPY gitstock/src/ /gitstock

RUN chmod +x /gitstock/gitstock.py

WORKDIR /gitstock

ENTRYPOINT ["/gitstock/gitstock.py"]
#CMD ["sleep", "300" ]
