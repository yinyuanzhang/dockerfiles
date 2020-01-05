FROM java:alpine

EXPOSE 8028

VOLUME /tmp

RUN mkdir /root/.m2

COPY . /root/cloud-file
WORKDIR /root/cloud-file

RUN ./mvnw package && ./mvnw install
RUN apk --no-cache add tzdata  && \
    ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo "Asia/Shanghai" > /etc/timezone

CMD ./mvnw spring-boot:run
