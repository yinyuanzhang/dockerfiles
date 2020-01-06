FROM qnib/terminal:fd22

# statsd
RUN echo "2015-09-10";dnf clean all && \
    dnf install -y statsd python-pip && \
    pip install statsd
ADD opt/qnib/bin/restart_statsd.sh /opt/qnib/bin/
ADD etc/statsd/config.js /etc/statsd/config.js
ADD etc/consul.d/check_statsd.json /etc/consul.d/
ADD opt/qnib/statsd/config.js /opt/qnib/statsd/
ADD etc/supervisord.d/statsd.ini /etc/supervisord.d/
