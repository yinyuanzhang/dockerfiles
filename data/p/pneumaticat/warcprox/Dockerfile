FROM python:3.7-alpine

RUN apk add --update build-base libffi libffi-dev openssl openssl-dev && \
    pip install warcprox==2.4.b3 && \
    apk del build-base libffi-dev openssl-dev

EXPOSE 8888

VOLUME /warcs /db /ca

ENTRYPOINT ["warcprox", "--address", "0.0.0.0", "--port", "8888"]
