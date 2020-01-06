FROM openjdk:8-alpine 

ENV MIRTH_CONNECT_VERSION 3.6.1.b220

# Mirth Connect is run with user `connect`, uid = 1000
# If you bind mount a volume from the host or a data container, 
# ensure you use the same uid
RUN adduser -D -u 1000 mirth

# grab gosu for easy step-down from root
COPY --from=gosu/assets /opt/gosu/ /opt/gosu
RUN /opt/gosu/gosu.install.sh && rm -rf /opt/gosu

VOLUME /opt/mirth-connect/appdata

RUN \
  cd /tmp && \
  wget http://downloads.mirthcorp.com/connect/$MIRTH_CONNECT_VERSION/mirthconnect-$MIRTH_CONNECT_VERSION-unix.tar.gz && \
  tar xvzf mirthconnect-$MIRTH_CONNECT_VERSION-unix.tar.gz && \
  rm -f mirthconnect-$MIRTH_CONNECT_VERSION-unix.tar.gz && \
  mv Mirth\ Connect/* /opt/mirth-connect/ && \
  chown -R mirth /opt/mirth-connect

WORKDIR /opt/mirth-connect

EXPOSE 8080 8443

COPY docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["java", "-jar", "mirth-server-launcher.jar"]

