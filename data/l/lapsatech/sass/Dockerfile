FROM ruby:2.2
MAINTAINER "Vadim Isaev" <vadim.o.isaev@gmail.com>

RUN gem install sass

VOLUME /src
WORKDIR /src
VOLUME /target

COPY cmd.sh /cmd.sh
CMD ["/cmd.sh"]
