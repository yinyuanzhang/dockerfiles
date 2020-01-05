FROM node

MAINTAINER Timo Pagel <dependencycheckmaintainer@timo-pagel.de>
RUN npm install -g eslint && npm install -g eslint-plugin-scanjs-rules && npm install -g eslint-plugin-no-unsafe-innerhtml && npm install -g babel-eslint 

RUN useradd --home /eslint -ms /bin/bash dockeruser && mkdir /reports && chown -R dockeruser:dockeruser /reports

COPY .eslintrc /eslint

USER dockeruser
VOLUME "/reports"
WORKDIR /reports


