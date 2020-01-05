FROM ubuntu:14.04.2

RUN apt-get update && \
    apt-get install -y curl && \
    curl -sL https://deb.nodesource.com/setup_0.12 | sudo -E bash -
RUN apt-get update && \
    apt-get install -y libzmq-dev build-essential nodejs

RUN npm config set strict-ssl false && npm install -g ponte bunyan

EXPOSE 3000
EXPOSE 1883
EXPOSE 5683

CMD ponte -v | bunyan
