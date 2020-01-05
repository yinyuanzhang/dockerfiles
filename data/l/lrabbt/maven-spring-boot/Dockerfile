FROM maven:3.5

MAINTAINER Breno Brandão <lrabbt@gmail.com>

RUN mkdir /app

# Adding run script
COPY run.sh /
RUN ["chmod", "+x", "/run.sh"]

WORKDIR /app

VOLUME /app

EXPOSE 8080

CMD ["sh", "/run.sh"]
