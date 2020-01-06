FROM rocker/r-apt:xenial

ARG GIT_BRANCH
ARG GIT_COMMIT

RUN apt-get update \
    && apt-get install -y build-essential libssl-dev libffi-dev python3-dev python3-pip \
    && pip3 install blobxfer==0.12.1

CMD ["R"]