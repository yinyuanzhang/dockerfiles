FROM node

RUN \
  cd /opt && \
  npm install \
    statsd@0.8.0 \
    git://github.com/markkimsal/statsd-elasticsearch-backend.git

ENTRYPOINT [ "/usr/local/bin/node", "/opt/node_modules/statsd/stats.js" ]
CMD [ "/statsd-config/config.js" ]
