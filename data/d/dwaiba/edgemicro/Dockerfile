FROM mhart/alpine-node:latest
MAINTAINER dwaiba <dwai@cloudgear.io>

COPY configure.sh /tmp/configure.sh
RUN chmod +x /tmp/configure.sh

RUN npm install -g edgemicro@2.5.16

CMD ["edgemicro", "start"]

EXPOSE 8000
