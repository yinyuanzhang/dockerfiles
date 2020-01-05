FROM alpine:3.5

MAINTAINER Ianus IT GmbH <info@ianus-it.de>

RUN apk add --update postgrey make &&\
    cpan -i NetAddr::IP &&\
    apk del make &&\
    rm -rf /var/cache/apk/*

CMD ["postgrey", "--inet", "0.0.0.0:10023", "--delay", "50", "--user", "postgrey", "--group", "postgrey"]
