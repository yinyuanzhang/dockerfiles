FROM openjdk:8-alpine
COPY PhantomBot-2.4.2.zip /usr/local/bin/
COPY beta-panel.zip /usr/local/bin/
WORKDIR /usr/local/bin
RUN apk add bash openssl unzip \
    && unzip /usr/local/bin/PhantomBot-2.4.2.zip -d /usr/local/bin/ \
    && mv /usr/local/bin/PhantomBot-2.4.2 /usr/local/bin/phantombot \
    && chmod u+x /usr/local/bin/phantombot/launch-service.sh /usr/local/bin/phantombot/launch.sh \
    && unzip /usr/local/bin/beta-panel.zip -d /usr/local/bin/phantombot/web/ \
    && apk del unzip \
    && rm -rf /usr/local/bin/PhantomBot-2.4.2.zip /usr/local/bin/beta-panel.zip /tmp/* /var/tmp/*
EXPOSE 25000 25001 25002 25003 25004
CMD /usr/local/bin/phantombot/launch-service.sh
