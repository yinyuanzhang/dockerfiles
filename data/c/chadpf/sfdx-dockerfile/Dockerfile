FROM alpine
RUN apk update
RUN apk add bash
RUN apk add --update nodejs nodejs-npm
RUN apk add openssh
RUN apk add git
RUN apk add jq
RUN apk add openjdk8
RUN npm install sfdx-cli --global
RUN npm update --global sfdx-cli
RUN sfdx --version
RUN sfdx plugins --core
RUN apk add apache-ant --update-cache \
    --repository http://dl-cdn.alpinelinux.org/alpine/edge/community/ \
    --allow-untrusted
ENV ANT_HOME /usr/share/java/apache-ant
ENV PATH $PATH:$ANT_HOME/bin