FROM alpine:3.10

MAINTAINER Pulkit Jalan "<pulkit1990@gmail.com>"

RUN apk add --update stunnel ca-certificates

ADD ./stunnel.sh /stunnel.sh
RUN chmod +x /stunnel.sh

ENTRYPOINT ["/stunnel.sh"]