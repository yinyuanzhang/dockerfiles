FROM node:10.4.1-alpine

# set env
ENV NODE_ENV=development

# set timezone, add tini and add express-generator
RUN apk add --update --no-cache tzdata tini && \
    cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \
    echo "Asia/Tokyo" > /etc/timezone && \
    apk del tzdata && \
    yarn global add @angular/cli@6.0.0

# Tini is now available at /sbin/tini
ENTRYPOINT [ "/sbin/tini", "--" ]

WORKDIR /my-app

EXPOSE 4200

CMD [ "node" ]