FROM java:alpine

EXPOSE 8048

VOLUME /tmp

RUN mkdir /root/.m2

COPY . /root/file_backend
WORKDIR /root/file_backend

RUN ./mvnw package && ./mvnw install
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo "Asia/Shanghai" > /etc/timezone

CMD ./mvnw spring-boot:run
