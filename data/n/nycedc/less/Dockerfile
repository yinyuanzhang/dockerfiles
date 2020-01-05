FROM mhart/alpine-node:6.16
LABEL maintainer.1="alehman@edc.nyc"
LABEL maintainer.2="aho@edc.nyc"

# install less compiler
RUN npm install -g less less-plugin-autoprefix

WORKDIR /app

ENTRYPOINT [ "lessc" ]