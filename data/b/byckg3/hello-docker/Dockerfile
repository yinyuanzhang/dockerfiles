# https://github.com/SeleniumHQ/docker-selenium

FROM selenium/standalone-chrome-debug:3.141.59

USER root

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN apt-get -y update \
    && apt-get -y install \
        python3 \
        python3-pip \
    && pip3 install --no-cache-dir -r requirements.txt \
    && apt-get -qqy autoremove \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get -qqy clean

CMD [ "robot", "--version" ]