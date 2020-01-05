FROM openjdk:8-jdk-alpine

RUN apk upgrade --update

RUN apk add --no-cache bash
RUN apk add --no-cache wget
RUN apk add --no-cache curl

RUN apk --no-cache add ca-certificates
RUN echo -e "http://nl.alpinelinux.org/alpine/v3.9/main\nhttp://nl.alpinelinux.org/alpine/v3.9/community" > /etc/apk/repositories

RUN \
# Use edge repos
echo "http://dl-cdn.alpinelinux.org/alpine/edge/main" > /etc/apk/repositories && \
echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories && \
echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories


RUN apk add --no-cache git

RUN apk add --no-cache maven

RUN \
# Install Firefox
apk update && apk upgrade && \
apk add firefox xvfb dbus ttf-freefont fontconfig && \
rm -rf /var/cache/apk/*

RUN \
# Create firefox + xvfb runner
mv /usr/bin/firefox /usr/bin/firefox-origin && \
echo $'#!/usr/bin/env sh\n\
Xvfb :0 -screen 0 1920x1080x24 -ac +extension GLX +render -noreset & \n\
DISPLAY=:0.0 firefox-origin $@ \n\
killall Xvfb' > /usr/bin/firefox && \
chmod +x /usr/bin/firefox

RUN apk add --no-cache chromium
RUN apk add --no-cache chromium-chromedriver

COPY ./geckodriver /usr/local/bin/
RUN chmod a+x /usr/local/bin/geckodriver

COPY ./chromedriver /usr/local/bin/
RUN chmod a+x /usr/local/bin/chromedriver

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
ENV M2_HOME /usr/share/maven
ENV CHROME_BIN /usr/bin/chromium-browser

RUN export JAVA_HOME
RUN export M2_HOME
RUN export CHROME_BIN

RUN apk add --no-cache python3
RUN apk add --no-cache python-dev
RUN apk add --no-cache py-pip
RUN apk add --no-cache bash build-base
RUN pip3 install redis
RUN pip3 install boto3
RUN pip3 install awscli

RUN apk add --no-cache openssh
RUN apk add --no-cache openssh-server
RUN apk add supervisor
ADD supervisor.conf /etc/supervisor.conf

EXPOSE 22

CMD ["supervisord", "-c", "/etc/supervisor.conf"]
