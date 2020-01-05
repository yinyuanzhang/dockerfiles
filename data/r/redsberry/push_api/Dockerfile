#--------------------------------------------------------------------------------------------------------#
# docker build --tag node .
# docker run -dit -p 4300:4300 --entrypoint=/bin/bash --name node node
# docker run -dit -p 4300:4300 -v /e/docker/node/tmp:/data/tmp --entrypoint=/bin/bash --name node node
# docker exec -it node bash
#--------------------------------------------------------------------------------------------------------#
FROM node:8.16.0-alpine

# copy run modules
WORKDIR /redsberry
ADD ./dist/src.tar ./
COPY ./dist/config.js ./conf/
COPY ./dist/authenticated.js ./conf/

RUN apk add python make
RUN npm install --silent && npm audit fix
RUN npm install -g pm2@latest

EXPOSE 4300

# ENTRYPOINT [ "pm2-runtime" ]
# CMD [ "start", "./ngpush.js", "--name=push",  "-i",  "2", ]
# docker에서 pm2를 실행시킬때는 pm2-runtime명령을 사용한다.
