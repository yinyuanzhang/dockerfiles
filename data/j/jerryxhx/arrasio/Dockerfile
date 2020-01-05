# arrasio

FROM alpine:3.8
MAINTAINER FAN VINGA<fanalcest@gmail.com>

RUN apk --no-cache add git nodejs nodejs-npm       && \
    git clone https://github.com/minthantsin/arras.io.git --depth 1 && \
    cd  arras.io && \
    npm install
    
COPY config.json /arras.io/

EXPOSE 8080

USER chat
ENV USER=chat

VOLUME /arras.io/bin
VOLUME /arras.io/logs

CMD cd arras.io && \ 
    npm start
