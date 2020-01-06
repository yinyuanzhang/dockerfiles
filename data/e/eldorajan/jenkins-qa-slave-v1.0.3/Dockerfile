FROM openjdk:8-jdk-alpine

RUN apk upgrade --update

RUN apk add --no-cache bash wget curl ca-certificates

RUN \
# Use latest stable repos
echo "http://nl.alpinelinux.org/alpine/edge/main" > /etc/apk/repositories && \
echo "http://nl.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories

RUN apk add --no-cache git maven jq curl firefox-esr chromium chromium-chromedriver nss freetype harfbuzz
RUN apk add --no-cache python3 python-dev py-pip build-base openssh openssh-server supervisor busybox-extras

RUN chmod a+x /usr/bin/firefox
RUN chmod a+x /usr/bin/chromium-browser

COPY geckodriver.sh geckodriver.sh
RUN chmod a+x geckodriver.sh
RUN sh geckodriver.sh

ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk/
ENV M2_HOME /usr/share/maven
ENV CHROME_BIN /usr/bin/chromium-browser

RUN export JAVA_HOME
RUN export M2_HOME
RUN export CHROME_BIN

RUN pip3 install redis
RUN pip3 install boto3
RUN pip3 install awscli
RUN pip3 install Faker

RUN apk update && apk upgrade \ && echo @latest-stable http://nl.alpinelinux.org/alpine/latest-stable/community >> /etc/apk/repositories \ && echo @latest-stable http://nl.alpinelinux.org/alpine/latest-stable/main >> /etc/apk/repositories \ && rm -rf /var/lib/apt/lists/* \ /var/cache/apk/* \ /usr/share/man \ /tmp/*

ADD supervisor.conf /etc/supervisor.conf

EXPOSE 22
EXPOSE 9515

CMD ["supervisord", "-c", "/etc/supervisor.conf"]
