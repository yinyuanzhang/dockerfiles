FROM maven:3.3.3-jdk-8 as build

MAINTAINER Yiannis Mouchakis <gmouchakis@iit.demokritos.gr>

RUN git clone https://github.com/semagrow/sevod-scraper.git /sevod-scraper && \
    cd /sevod-scraper && \
    mvn clean package && \
    mkdir -p /dist && \
    tar xvf assembly/target/sevod-scraper-*-dist.tar.gz -C /dist

FROM openjdk:8-jre-alpine

ENV PATH /sevod-scraper/bin:$PATH

COPY --from=build /dist /sevod-scraper

WORKDIR /sevod-scraper

ENTRYPOINT ["sh", "./bin/sevod-scraper.sh"]

