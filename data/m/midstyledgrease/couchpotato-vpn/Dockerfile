FROM linuxserver/couchpotato:latest

RUN apk add --no-cache openvpn
COPY pia /pia
WORKDIR /pia
COPY run.sh /usr/local/bin/run.sh

ENV REGION="US East"
ENTRYPOINT ["run.sh"]
