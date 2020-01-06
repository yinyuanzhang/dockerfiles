FROM alpine:edge
MAINTAINER Sinan Goo 

RUN apk update 
RUN apk --no-cache add git
RUN git clone --branch 1.1.4 https://github.com/nasoym/bss.git

RUN apk --no-cache add socat bash jq curl sed openssl

ENV AUTHENTICATE 0

WORKDIR /bss
COPY handlers/ /bss/handlers/

EXPOSE 8080

CMD ["./run.sh"]


