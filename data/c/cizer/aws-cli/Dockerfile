FROM ubuntu:trusty
LABEL maintainer="richie.mackay@gmail.com"

RUN apt-get -y update && \
    apt-get install -y -q \
    unzip \
    curl \
    git \
    python3

RUN curl -kL https://bootstrap.pypa.io/get-pip.py | python3
RUN pip install awscli --upgrade

ENV HOME=/home
COPY .aws* /home/.aws

ENTRYPOINT ["aws"]
CMD ["--version"]