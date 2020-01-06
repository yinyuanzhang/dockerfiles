FROM node:alpine
MAINTAINER NHibiki https://github.com/NHibiki

RUN apk add --no-cache \
        screen \
    && apk add --no-cache --virtual .build-deps \
        git \
    && git clone https://github.com/NHibiki/NekoBlog.git \
    && git clone -b story https://github.com/NHibiki/NekoBlogTheme.git NekoBlog/themes/story \
    && apk del .build-deps \
    && cd NekoBlog \
    && npm install \
    && echo -e "cd NekoBlog \nscreen -dmS nb node app \ncd .." > /rund.sh \
    && echo -e "cd NekoBlog \nnode app \ncd .." > /run.sh \
    && chmod a+x /*.sh

EXPOSE 80 443

CMD [ "/run.sh" ]
