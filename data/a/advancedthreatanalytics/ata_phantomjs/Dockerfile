FROM node:8

RUN apt-get update && \
     apt-get install -y curl bzip2 libfreetype6 libfontconfig

COPY package.json /opt/app/package.json
WORKDIR /opt/app

RUN yarn install \
    && mkdir -p /opt/images

ENV PATH=/opt/app/node_modules/phantomjs-prebuilt/lib/phantom/bin:$PATH
CMD ["node", "index.js"]

COPY ./scripts/ /opt/app
