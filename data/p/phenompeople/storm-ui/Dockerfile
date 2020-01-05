FROM phenompeople/apache-storm:1.2.2
LABEL maintainer="rajesh.jonnalagadda@phenompeople.com" \
      version="1.2.2"
EXPOSE 8881 8000
COPY *-server.sh /opt/deployment/
RUN mkdir -p ${STORM_HOME}/logs && \
    touch ${STORM_HOME}/logs/storm-ui.out && \
    chown -R phenom:phenom ${STORM_HOME}
USER phenom
ENTRYPOINT ["/opt/deployment/start-server.sh"]