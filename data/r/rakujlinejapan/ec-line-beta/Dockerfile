from node:8.11-alpine

# python
RUN apk add --update \
    python \
    python-dev \
    py-pip \
    build-base \
  && pip install virtualenv \
  && rm -rf /var/cache/apk/*

# the name of an archived meteor app
ARG METEOR_APP="ec-line-beta"

ADD ${METEOR_APP}.tar.gz /

RUN cd / \
  tar -zxf ${METEOR_APP}.tar.gz \
  && cd bundle/programs/server \
  && npm i

ENV MONGO_URL="mongodb://mongo_instance:27017/meteor"
ENV ROOT_URL="https://127.0.0.1"
ENV PORT="3000"

EXPOSE 3000

ENTRYPOINT ["node", "/bundle/main.js"]
