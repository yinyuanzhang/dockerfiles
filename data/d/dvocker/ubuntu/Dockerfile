FROM ubuntu:14.04

MAINTAINER vladimir@drizheruk.com.ua

COPY bin /opt/bin
COPY etc /etc

RUN chmod +x /opt/bin/setup.sh && sleep 1 && /opt/bin/setup.sh && sleep 1 && rm -rf /opt/bin/setup.sh

CMD ["/usr/local/bin/supervisord", "-n"]
