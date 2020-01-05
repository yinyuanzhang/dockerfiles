FROM node:alpine
MAINTAINER SFoxDev <admin@sfoxdev.com>

ENV DEBIAN_FRONTEND="noninteractive" \
    LC_ALL="C.UTF-8" \
    LANG="en_US.UTF-8" \
    LANGUAGE="en_US.UTF-8"

RUN npm install -g redis-commander ; \
    echo '{}' > /root/.redis-commander ;

ENTRYPOINT ["redis-commander"]

EXPOSE 8081
