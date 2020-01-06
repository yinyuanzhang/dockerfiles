FROM node:12.9.1-alpine

MAINTAINER David Hazinski <david@dhaz.in>

RUN npm install -g @beaker/homebase@2.0.8 && rm -rf /root/.npm

ENV HOMEBASE_CONFIG=/etc/homebase/config.yml

VOLUME ["/etc/homebase"]

EXPOSE 80 443 3282 8089

ENTRYPOINT ["homebase"]
