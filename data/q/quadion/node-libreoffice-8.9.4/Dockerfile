FROM node:8.9.4-slim
RUN apt-get update \
&& apt-get install -y \
 zip \
 apt-transport-https \
 build-essential \
 libcairo2-dev \
 libpango1.0-dev \
 libjpeg-dev libgif-dev \
 librsvg2-dev \
 software-properties-common \
 python-software-properties \
 python-pip \
 python-yaml \
 openssh-client \
&& pip install -U setuptools \
&& pip install awscli \
&& add-apt-repository "deb https://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main" \
&& apt-get update \
&& apt-get install -y --force-yes \
 libreoffice \
 postgresql-client-9.6 \
 git
