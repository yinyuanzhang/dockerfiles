FROM node:alpine

LABEL org.label-schema.usage="https://github.com/smutdose/now/blob/master/README.md"
LABEL org.label-schema.url="https://hub.docker.com/r/smutdose/now"
LABEL org.label-schema.vcs-url="https://github.com/smutdose/now "
LABEL org.label-schema.version="15.4.0"
LABEL org.label-schema.schema-version="1.0"

RUN npm --global --unsafe-perm install now && \
    npm_config_loglevel=error npm cache clean --force

VOLUME ["/root/.now"]

ENTRYPOINT ["now"]
