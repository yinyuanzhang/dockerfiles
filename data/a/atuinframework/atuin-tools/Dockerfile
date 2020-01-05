FROM node:10-slim

MAINTAINER Paolo Casciello <paolo.casciello@scalebox.it>

RUN apt-get update -y && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends python && \
    curl https://bootstrap.pypa.io/get-pip.py | python  && \
    pip install --upgrade flask flask_babel && \
    apt-get -y autoremove && \
    apt-get -y clean && \
    rm -rf /var/lib/apt/lists/* /var/cache/* /tmp/* /var/tmp/*

COPY ./gulpfile.js /workspace/
COPY ./gulp /workspace/gulp
COPY ./package.json /workspace/

WORKDIR /workspace

RUN npm update

ENV PATH=/workspace/node_modules/.bin:$PATH

CMD ["gulp", "monitor"]
