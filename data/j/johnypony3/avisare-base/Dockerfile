FROM node:6

RUN apt-get -y upgrade \
    && apt-get update \
    && apt-get -y install \
      gettext-base \
      mysql-client \
      python \
      python-dev \
      python-pip \
      python-setuptools \
      groff \
      less \
    && apt-get clean \
    && pip install --upgrade awscli \
    && aws --version \
    && npm install -g \
      mysql2 \
      bower \
      gulp-cli \
      sequelize-cli \
      swagger \
      jasmine
