FROM python:3.7-alpine
LABEL maintainer="Mathew Moon < mmoon@quinovas.com >"

RUN apk add bash && \
    pip install awscli lambda_setuptools

WORKDIR /root

CMD ["/bin/bash"]
