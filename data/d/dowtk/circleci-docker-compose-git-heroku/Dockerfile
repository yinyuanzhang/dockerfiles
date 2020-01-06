FROM docker:latest

LABEL name=dowtk/circleci-docker-compose-git-heroku
LABEL maintainer="rob.styles@dayoutwiththekids.co.uk"
LABEL description="git, docker, docker compose, heroku combined for running CI builds on Circle CI"

RUN apk add --no-cache py-pip curl wget bash openssh git nodejs yarn
RUN pip install docker-compose
RUN yarn global add heroku

RUN git --version && \
    heroku --version && \
    docker --version && \
    docker-compose --version

WORKDIR /

ENTRYPOINT bash
CMD bash
