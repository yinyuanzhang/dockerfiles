
FROM ubuntu:latest

RUN apt-get update \
	&& apt-get install -y --no-install-recommends wget curl ca-certificates unzip libssl1.0.0
COPY ./bedrockserver.sh /usr/bin/bedrockserver.sh

ADD https://minecraft.azureedge.net/bin-linux/bedrock-server-1.14.1.4.zip /tmp/brserver.zip

RUN mkdir /opt/mcbedrock/ -p
RUN unzip /tmp/brserver.zip -d /opt/mcbedrock/

WORKDIR /opt/mcbedrock
EXPOSE 19133
EXPOSE 19132
CMD ["bash", "-c", "/usr/bin/bedrockserver.sh"]
