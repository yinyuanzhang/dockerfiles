# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# FROM python:3.6-jessie
FROM amancevice/superset
USER root
# RUN useradd --user-group --create-home --no-log-init --shell /bin/bash superset

# Configure environment
ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8

RUN apt-get update -y && DEBIAN_FRONTEND=noninteractive \
    && apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv C2518248EEA14886

# Install dependencies to fix `curl https support error` and `elaying package configuration warning`
RUN apt-get install -y apt-transport-https apt-utils software-properties-common \
    && apt-get update -y && apt-get install software-properties-common \
    && add-apt-repository "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main"

# Install superset dependencies
# https://superset.incubator.apache.org/installation.html#os-dependencies
RUN apt-get update -y  && apt-get install -y build-essential libssl-dev libffi-dev python3-dev libsasl2-dev \
    libldap2-dev libxi-dev libxi-dev libsasl2-modules libgtk-3-0 xvfb firefox-esr libglib2.0-0  libnss3 libgconf-2-4 \
    libfontconfig1 vim less postgresql-client redis-tools chromium nodejs default-jdk

WORKDIR /home/superset

# COPY requirements.txt .
COPY requirements-dev.txt .
COPY requirements-extra.txt .

RUN pip install --upgrade setuptools pip \
    && pip install -r requirements-dev.txt -r requirements-extra.txt \
    && rm -rf /root/.cache/pip


RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz \
    && tar -x geckodriver -zf geckodriver-v0.26.0-linux64.tar.gz -O > /usr/bin/geckodriver \
    && chmod +x /usr/bin/geckodriver \
    && rm geckodriver-v0.26.0-linux64.tar.gz

RUN wget -q "https://chromedriver.storage.googleapis.com/80.0.3987.16/chromedriver_linux64.zip" -O /tmp/chromedriver.zip \
    && unzip /tmp/chromedriver.zip -d /usr/bin/ \
    && ls \
    && rm /tmp/chromedriver.zip

USER superset

RUN export USE_TZ=True && export TZ="Etc/UTC" && export CELERY_ENABLE_UTC=True \
    && export CELERY_TIMEZONE='Etc/UTC'

RUN Xvfb :10 -ac &
RUN export DISPLAY=:10

COPY --chown=superset:superset superset_config.py /home/superset/superset_config.py
COPY --chown=superset:superset docker-entrypoint.sh /home/superset/entrypoint.sh


ENTRYPOINT ["./entrypoint.sh"]

HEALTHCHECK CMD ["curl", "-f", "http://localhost:8088/health"]

EXPOSE 8088
