FROM "node:10"

LABEL com.indiestore.crowdwatch.version="1.1.1"
LABEL com.indiestore.crowdwatch.author="Dean Vaessen"
LABEL com.indiestore.crowdwatch.description="Crowdwatch moderation tool"
LABEL maintainer="claude.juif@gmail.com"

RUN set -ex \
  mkdir /usr/src; \
  mkdir /config; \
  mkdir /usr/logs; \
  apt update -y; \
  DEBIAN_FRONTEND=noninteractive apt upgrade -q -y; \
  DEBIAN_FRONTEND=noninteractive apt install -y \
    python-dev \
    python-pip; \
  rm -rf /var/lib/apt/lists/*; \
  pip install envtpl

ADD sources/moderation /usr/src/moderation
ADD sources/webpack /usr/src/webpack
ADD aws.json.tpl /config
ADD prod.json.tpl /config
ADD entrypoint.sh /

RUN set -ex; \
  cd /usr/src/webpack \
  && npm install \
  && npm run build \
  && cd /usr/src/moderation \
  && npm install \
  && ln -s /usr/src/webpack/build public

EXPOSE 4001/tcp

ENTRYPOINT ["/entrypoint.sh"]

CMD ["npm", "run", "prod"]
