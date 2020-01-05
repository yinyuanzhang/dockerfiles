FROM docker:18.09-git
# To build docker image in circle ci, you'll need to have docker and git installed
# reference: https://circleci.com/blog/how-to-build-a-docker-image-on-circleci-2-0/#docker-executor

RUN apk add --no-cache py2-pip=18.1-r0 \
      && pip install awscli==1.16.140
