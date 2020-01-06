FROM busybox

ADD https://github.com/upfluence/etcdenv/releases/download/v0.1.2/etcdenv-linux-amd64-0.1.2 /usr/bin/etcdenv
RUN chmod +x /usr/bin/etcdenv

ADD https://s3.amazonaws.com/upfluence-common/statsd-1.0.0 /usr/bin/statsd
RUN chmod +x /usr/bin/statsd
RUN rm -rf /tmp/*

EXPOSE 8125

ENV DEBUG false

CMD etcdenv -n /environments/global -s http://172.17.42.1:4001 statsd
