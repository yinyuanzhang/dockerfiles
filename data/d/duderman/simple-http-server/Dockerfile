FROM mhart/alpine-node

RUN npm install -g http-server

WORKDIR /site

VOLUME /site

EXPOSE  8080

CMD ["http-server", "--cors", "-p8080", "/site"]
