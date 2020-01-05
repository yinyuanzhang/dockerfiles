FROM openjdk:8
RUN git clone https://github.com/Netflix/Hystrix.git \
    && cd Hystrix/hystrix-dashboard \
    && ../gradlew build
WORKDIR /Hystrix/hystrix-dashboard
EXPOSE 7979
CMD ../gradlew jettyRun
