FROM golang

MAINTAINER Eric Carlson "eric@ds-do.com"

RUN git clone https://github.com/bitly/oauth2_proxy.git /go/src/app

RUN go get -d -v github.com/bitly/oauth2_proxy
RUN go install -v github.com/bitly/oauth2_proxy

VOLUME /conf

EXPOSE 4180

CMD ["oauth2_proxy", "-config", "/conf/oauth2_proxy.cfg"]
