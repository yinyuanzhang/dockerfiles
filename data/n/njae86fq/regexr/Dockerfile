FROM node:8.16.1-buster-slim

COPY npm-shrinkwrap.json .

RUN set -ex \
 && regexr_version=3.6.1 \
 && regexr_file="${regexr_version}.tar.gz" \
 && cd /tmp \
 && curl -L -O "https://github.com/gskinner/regexr/archive/${regexr_file}" \
 && tar xf "${regexr_file}" \
 && mv "regexr-${regexr_version}" /regexr \
 && cd /regexr \
 && npm install -g gulp \
 && npm install \
 && rm -rf /tmp/*

WORKDIR /regexr
EXPOSE 3000

ENTRYPOINT "gulp"
