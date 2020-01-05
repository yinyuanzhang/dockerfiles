FROM mhart/alpine-node:13.5.0

RUN apk add --no-cache make gcc g++ python

VOLUME /src

COPY runner.sh /usr/bin

RUN npm install -g gulp@3.9.1

WORKDIR /src

CMD ["gulp"]
ENTRYPOINT ["/usr/bin/runner.sh"]
