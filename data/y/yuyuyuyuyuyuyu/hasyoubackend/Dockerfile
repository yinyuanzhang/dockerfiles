FROM carsharing/alpine-oraclejdk8-bash
MAINTAINER yuyuyuyuyuyuyu

EXPOSE 8028

VOLUME /tmp

RUN mkdir /root/.m2

COPY . /root/hasyou
WORKDIR /root/hasyou

RUN ./mvnw package && ./mvnw install
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo "Asia/Shanghai" > /etc/timezone

CMD ./mvnw spring-boot:run
