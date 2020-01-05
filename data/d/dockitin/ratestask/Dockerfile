FROM jenkins/jenkins:2.82-alpine

USER root

RUN apk add --update  python \
            python-dev \
            py-pip \
            build-base \
 &&  pip install --upgrade pip \
                   awscli --upgrade \
                  requests
USER jenkins
