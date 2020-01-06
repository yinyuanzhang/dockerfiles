FROM ubuntu:bionic
MAINTAINER Ajeeth.Samuel@gmail.com

ENV RELEASE v0.8.0

RUN apt-get update && \
	apt-get install -y unzip && \
	apt-get clean

WORKDIR /
RUN mkdir /app
ADD https://github.com/gophish/gophish/releases/download/$RELEASE/gophish-$RELEASE-linux-64bit.zip /app/
WORKDIR /app
RUN unzip /app/gophish-$RELEASE-linux-64bit.zip && rm /app/gophish-$RELEASE-linux-64bit.zip
RUN sed -i "s|127.0.0.1|0.0.0.0|g" config.json
RUN sed -i "s|gophish.db|database/gophish.db|g" config.json
RUN chmod +x ./gophish

VOLUME ["/app/database"]
EXPOSE 3333 80
ENTRYPOINT ["./gophish"]
