FROM blairguk/node-sass-alpine:8.11.0

USER root

ENV TZ=Asia/Shanghai

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN npm install -g @vue/cli
