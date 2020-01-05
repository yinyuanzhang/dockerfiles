FROM java:jre
MAINTAINER "Vadim Isaev" <vadim.o.isaev@gmail.com>

ADD https://github.com/yui/yuicompressor/releases/download/v2.4.8/yuicompressor-2.4.8.jar /usr/share/java/yuicompressor-2.4.8.jar

VOLUME /src
WORKDIR /src


COPY cmd.sh /cmd.sh
CMD ["/cmd.sh"]
