FROM node:6.17.1-alpine

# Working environment
ENV \
    CNPMJS_ORG_VERSION="2.19.4" \
    CNPM_DIR="/var/app/cnpmjs.org" \
    CNPM_DATA_DIR="/var/data/cnpm_data"

RUN set x=1 && \
    apk update && \
    apk add --no-cache --virtual .tz tzdata && \
    rm -rf /tmp/* /var/cache/apk/*

RUN mkdir -p /var/app ${CNPM_DATA_DIR}

RUN \
  wget -P /tmp https://github.com/cnpm/cnpmjs.org/archive/${CNPMJS_ORG_VERSION}.tar.gz && \
  tar xvzf /tmp/${CNPMJS_ORG_VERSION}.tar.gz -C /var/app && \
  mv /var/app/cnpmjs.org-${CNPMJS_ORG_VERSION} ${CNPM_DIR}

WORKDIR ${CNPM_DIR}

RUN npm install

EXPOSE 7001/tcp 7002/tcp

VOLUME ["/var/data/cnpm_data"]

CMD ["node", "dispatch.js"]
