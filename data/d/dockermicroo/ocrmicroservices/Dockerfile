FROM java:openjdk-8u45-jdk

RUN mkdir /app

WORKDIR /app

ADD . /app

ENV JAVA_ENV=PRODUCTION

EXPOSE 8080

CMD ["java", "-server", "-cp", "bookings/target/classes:bookings/target/dependency/*", "com.kumuluz.ee.EeApplication"]