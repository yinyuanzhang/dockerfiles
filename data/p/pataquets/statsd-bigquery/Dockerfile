FROM node:6

RUN \
  cd /opt && \
  npm install \
    statsd@0.8.0 \
    big-stats@0.2.47

ENTRYPOINT [ "/usr/local/bin/node", "/opt/node_modules/statsd/stats.js" ]
CMD [ "/statsd-config/config.js" ]
